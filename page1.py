import streamlit as st

st.set_page_config(page_title="hangman")
st.title("hangman")
img=st.image('1.png')


btn_a=st.button('easy')
btn_b=st.button('normal')
btn_c=st.button('hard')

if btn_a:
    st.switch_page('easy.py')








