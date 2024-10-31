import streamlit as st









pages={' ':[st.Page('login_page.py',title='A'),
            st.Page('page1.py',title='B'),
            st.Page('easy.py',title='C'),
        st.Page('b.py',title='B페이지')], }

pg=st.navigation(pages)
pg.run()




