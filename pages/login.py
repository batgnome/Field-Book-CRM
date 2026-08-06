import streamlit as st
from services.auth import authenticate

if "user" not in st.session_state:
    st.session_state.user = None

with st.form("Login"):
    email = st.text_input("Email")
    password = st.text_input("Password",type="password")

    submitted = st.form_submit_button("Submit")

if submitted:
    user = authenticate(email, password)
    if user:
        st.success("Login successful")
        st.session_state.user = {"email": email}
        st.rerun()
    else:
        st.error("Invalid email or password")