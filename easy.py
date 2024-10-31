import streamlit as st
import time
import streamlit as st

st.title("hangman")


a = "about"

입력=st.text_input("입력")


ABC=str(입력)

if a[0]==ABC:
    w0=a[0]
    
if a[1]==ABC:
    w1=a[1]
    
if a[2]==ABC:
    w2=a[2]
    
if a[3]==ABC:
    st.write(a[3])

st.write(w0+w1+w2)


