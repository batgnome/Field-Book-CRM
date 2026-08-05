import streamlit as st


conn = st.connection("neon", type="sql")

with st.form("Login"):
    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
    email = st.text_input("Email")

    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(f"hello {fname} {lname}")