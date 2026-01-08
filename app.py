import streamlit as st
from random import randint

if "ans" not in st.session_state:
    st.session_state.ans = [randint(0, 9) for _ in range(3)]

st.title("数当てゲーム(アプリ版)")

a = st.number_input("1桁目(0～9)", min_value = 0, max_value = 9, step = 1)
b = st.number_input("2桁目(0～9)", min_value = 0, max_value = 9, step = 1)
c = st.number_input("3桁目(0～9)", min_value = 0, max_value = 9, step = 1)

nums = [a, b, c]

if st.button("判定"):
    ans = st.session_state.ans
    cnt1 = 0
    cnt2 = 0
    for n in range(3):
        if ans[n] == nums[n]:
            cnt1 += 1
        else:
            cnt2 += 1
            
    if cnt1 == 3:
        st.write("正解です")
        st.image("omedetou.png", width= 200)
    else:
        st.write(f"{cnt1}  ヒット  {cnt2}  ボール")
        
if st.button("変更"):
    st.session_state.ans = [randint(0, 9) for _ in range(3)]