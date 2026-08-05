import streamlit as st
from services.auth import authenticate
with st.form("Login"):
    email = st.text_input("Email")
    password = st.text_input("Password")

    submitted = st.form_submit_button("Submit")

if submitted:
    authenticate(email, password)