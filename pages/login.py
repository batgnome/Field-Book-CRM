import streamlit as st
from services.auth import authenticate
with st.form("Login"):
    email = st.text_input("Email")
    password = st.text_input("Password",type="password")

    submitted = st.form_submit_button("Submit")

if submitted:
    user = authenticate(email, password)
    if user:
        st.success("Login successful")
    else:
        st.error("Invalid email or password")