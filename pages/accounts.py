import streamlit as st
from db.accounts import get_accounts
if "user" not in st.session_state:
    st.session_state.user = None


st.title("Accounts")
accounts = get_accounts() #-> table
if accounts.empty:
    st.info("No accounts found.")
else:
    st.dataframe(accounts,hide_index=True,
                 use_container_width=True)

