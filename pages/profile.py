import streamlit as st
from db.users import get_user_by_email

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is not None:
    user = get_user_by_email(st.session_state.user["email"])
    st.write(f"Welcome {user[0].first_name} {user[0].last_name}!")