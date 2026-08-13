import streamlit as st
from db.accounts import get_accounts#,delete_account,edit_account
def show_accounts():
    if "user" not in st.session_state:
        st.session_state.user = None


    st.title("All Accounts")
    accounts = get_accounts() #-> table
    if accounts.empty:
        st.info("No accounts found.")
    else:
        for _, account in accounts.iterrows():
            col1, col2, col3, col4 = st.columns([4, 2, 1, 1])

            col1.write(account["company"])
            col2.write(account["status"])

            if col3.button("Edit", key=f"edit_{account['acctid']}"):
                st.session_state.selected_account = account["acctid"]
                st.session_state.account_view = "edit"

            if col4.button("Delete", key=f"delete_{account['acctid']}"):
                # delete_account(account["acctid"])
                st.rerun()
