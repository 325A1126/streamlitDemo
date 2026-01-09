import streamlit as st
from random import randint

#答え
if "ans" not in st.session_state:
    st.session_state.ans = [randint(0, 9) for _ in range(3)]

#挑戦回数をカウント
if "cnt3" not in st.session_state:
    st.session_state.cnt3 = 0

#履歴
if "history" not in st.session_state:
    st.session_state.history = []
    
#タイトル
st.title("数当てゲーム(アプリ版)")

#入力
a = st.number_input("1桁目(0～9)", min_value = 0, max_value = 9, step = 1)
b = st.number_input("2桁目(0～9)", min_value = 0, max_value = 9, step = 1)
c = st.number_input("3桁目(0～9)", min_value = 0, max_value = 9, step = 1)

nums = [a, b, c]

#ボタン
judge = st.button("判定")
reset = st.button("リセット")

#リセット
if reset:
    st.session_state.ans = [randint(0, 9) for _ in range(3)]
    st.session_state.cnt3 = 0
    st.session_state.history = []
    
#判定
elif judge:
    ans = st.session_state.ans
    cnt1 = 0
    cnt2 = 0
    st.session_state.cnt3 += 1
    
    for n in range(3):
        if ans[n] == nums[n]:
            cnt1 += 1
        else:
            cnt2 += 1
            
    if cnt1 == 3:
        st.write("正解です")
        st.image("omedetou.png", width= 200)
    else:
        st.session_state.history.append(f"{st.session_state.cnt3}回目：{nums}　→　{cnt1}ヒット{cnt2}ボール")
        st.write(f"{cnt1}  ヒット  {cnt2}  ボール")


#挑戦回数の表示       
st.write(f'挑戦回数：{st.session_state.cnt3}回')

# 履歴表示
st.subheader("判定履歴")
if st.session_state.history:
    for h in st.session_state.history:
        st.write(h)
else:
    st.write("まだ履歴はありません")
