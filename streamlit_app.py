import streamlit as st
pages = [
    st.page("pages/login.py"),
    st.page("pages/test.py"),
    st.page("pages/signup.py")
]
pg = st.navigation(pages)

pg.run()