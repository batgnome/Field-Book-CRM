import streamlit as st
from db.users import create_user
from services.auth import register_user


with st.form("Sign Up"):
    st.write("Welcome! Create account here:")
    userFname = st.text_input("First Name")
    userLname = st.text_input("Last Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone number")
    role = st.selectbox("Role", ["Sales", "Manager"])
    password = st.text_input("Password", type="password")
    repassword = st.text_input("Reenter password", type="password")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not userFname or not userLname or not email or not password:
        st.error("Please fill in all required fields.")
    elif password != repassword:
        st.error("Passwords do not match.")
    else:
        register_user(
            userFname
            ,userLname
            ,email
            ,phone
            ,role
            ,password
        )

    # userId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # userFname varchar NOT NULL,
    # userLname varchar NOT NULL,
    # email varchar NOT NULL UNIQUE,
    # phone varchar,
    # role varchar NOT NULL,
    # passwordHash varchar NOT NULL,
    # createdAt timestamp DEFAULT now(),
    # deleted boolean DEFAULT false
    # email = st.text_input("Email")
    # password = st.text_input("Password")