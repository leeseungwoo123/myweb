import streamlit as st

from random import *


영어=['q','w','e','r','t','y','u','i','o','p','a','s','d','f',
    'g','h','j','k','l','z','x','c','v','b','n','m']

max_attempts = 7



words = ["invulnerable", "substantive", "equivocal", "hereditary", "negligible","inadvertent","homogenize","predisposed","disseminate","ephemera","equanimity","tranquilizer","destitution","acquiesce","proliferate","conservation","pneumonoultramicroscopicsilicovolcanoconiosis","floccinaucinihilipilification"]

if 'word' not in st.session_state:
    st.session_state.word = choice(words)


입력=st.text_input('입력', max_chars=1)
btn_1=st.button('추측')


if 'attempts' not in st.session_state:
        
    st.session_state.attempts = 0
        
    st.session_state.guessed_letters = []
        
    st.session_state.display_word = "_" * len(st.session_state.word)



def guess_letter(입력):


    if 입력 not in 영어:
        st.warning("소문자 영어를 입력하세요.")



    else:
        if 입력 in st.session_state.guessed_letters:

            st.warning("이미 추측한 글자입니다.")

        elif 입력 in st.session_state.word:

            st.session_state.guessed_letters.append(입력)

            st.session_state.display_word = "".join(

            [c if c in st.session_state.guessed_letters else "_" for 
             c in st.session_state.word])

        else:

            st.session_state.guessed_letters.append(입력)

            st.session_state.attempts += 1
           




if btn_1:
    if 입력:
        guess_letter(입력)
    else:
        st.warning("글자를 입력")

if st.session_state.attempts==0:
                img=st.image('8.png')
elif st.session_state.attempts==1:
                img=st.image('7.png')
elif st.session_state.attempts==2:
                img=st.image('6.png')
elif st.session_state.attempts==3:
                img=st.image('5.png')
elif st.session_state.attempts==4:
                img=st.image('4.png')
elif st.session_state.attempts==5:
                img=st.image('3.png')
elif st.session_state.attempts==6:
                img=st.image('2.png')
elif st.session_state.attempts==7:
                img=st.image('1.png')

if st.session_state.attempts >= max_attempts:

    st.header("실패") 

    st.write('정답:   '+st.session_state.word)

    st.button("다시 시작", on_click=lambda: st.session_state.clear())

elif "_" not in st.session_state.display_word:

    st.header("정답을 맞췄습니다.")

    st.button("다시 시작", on_click=lambda: st.session_state.clear())



st.header("단어: "+ " ".join(st.session_state.display_word))

st.write(f"남은 기회: {7-st.session_state.attempts}")

st.write("추측한 글자: ", " ".join(st.session_state.guessed_letters))











