import streamlit as st
from db.accounts import get_accounts,delete_account#,edit_account
def show_accounts():
    if "user" not in st.session_state:
        st.session_state.user = None


    st.title("All Accounts")
    accounts = get_accounts() #-> table
    if accounts.empty:
        st.info("No accounts found.")
    else:
        for _, account in accounts.iterrows():
            company_1, status_2, archived_3, edit_button, delete_button,  = st.columns([4, 2, 2, 1, 1])

            company_1.write(account["company"])
            status_2.write(account["status"])
            archived_3.write(account["archived"])
            

            if edit_button.button("Edit", key=f"edit_{account['acctid']}"):
                st.session_state.selected_account = account["acctid"]
                st.session_state.account_view = "edit"
                st.rerun()

            if delete_button.button("Delete", key=f"delete_{account['acctid']}"):
                restult = delete_account(account["acctid"])
                st.rerun()
