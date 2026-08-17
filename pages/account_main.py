import streamlit as st
from components.accounts.create_account import create_update_account_form
from components.accounts.show_accounts import show_accounts


st.title("Accounts")

if "account_view" not in st.session_state:
    st.session_state.account_view = "accounts"

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Create Account"):
        st.session_state.account_view = "create"

with col2:
    if st.button("Show Accounts"):
        st.session_state.account_view = "accounts"




if st.session_state.account_view == "create":
    create_update_account_form()

elif st.session_state.account_view == "accounts":
    show_accounts()
elif st.session_state.account_view == "edit":
    create_update_account_form(st.session_state.selected_account)