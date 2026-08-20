import streamlit as st
from db.accounts import get_accounts,delete_account, get_account
from utilities.util import display_value
def show_accounts():
    if "user" not in st.session_state:
        st.session_state.user = None


    st.title("All Accounts")
    accounts = get_accounts() #-> table
    if accounts.empty:
        st.info("No accounts found.")
    else:
        comp_title, status_title, archived_title, edit_title, del_title=st.columns([4,2,2,1,1])
        comp_title.write("Company Name") 
        status_title.write("Status")
        archived_title.write("Archived?")
        edit_title.write("Edit") 
        del_title.write("Delete")        
        for _, account in accounts.iterrows():
            company_1, status_2, archived_3, edit_button, delete_button,  = st.columns([4, 2, 2, 1, 1])

            # company_1.write(account["company"])
            if company_1.button(account["company"], key=f"view_{account['acctid']}"):
                st.session_state.selected_account = account["acctid"]
                st.session_state.account_view = "view"
                st.rerun()

            status_2.write(account["status"])
            archived_3.write(account["archived"])
            

            if edit_button.button("Edit", key=f"edit_{account['acctid']}"):
                st.session_state.selected_account = account["acctid"]
                st.session_state.account_view = "edit"
                st.rerun()

            if delete_button.button("Delete", key=f"delete_{account['acctid']}"):
                restult = delete_account(account["acctid"])
                st.rerun()

def show_account(acctid):
    account = get_account(acctid)

    if account.empty:
        st.info("Account not found.")
        return

    st.title(account["company"])

    company_title, company = st.columns([2, 5])
    company_title.write("Company")
    company.write(display_value(account["company"]))

    status_title, status = st.columns([2, 5])
    status_title.write("Status")
    status.write(display_value(account["status"]))

    created_title, created = st.columns([2, 5])
    created_title.write("Created")
    created.write(display_value(account["created_at"]))

    address_title, address = st.columns([2, 5])
    address_title.write("Address")

    street = display_value(account["address"], "")
    city = display_value(account["city"], "")
    state = display_value(account["state"], "")
    zipcode = display_value(account["zip"], "")

    city_state_zip = " ".join(
        value for value in [city, state, zipcode] if value
    )

    full_address = ", ".join(
        value for value in [street, city_state_zip] if value
    )

    address.write(full_address or "—")

    contact_title, contact = st.columns([2, 5])
    contact_title.write("Primary Contact")

    first_name = display_value(account["fname"], "")
    last_name = display_value(account["lname"], "")
    full_name = " ".join(
        value for value in [first_name, last_name] if value
    )

    contact.write(full_name or "—")

    edit_button, delete_button = st.columns(2)

    if edit_button.button("Edit", key=f"edit_{account['acctid']}"):
        st.session_state.selected_account = int(account["acctid"])
        st.session_state.account_view = "edit"
        st.rerun()

    if delete_button.button("Delete", key=f"delete_{account['acctid']}"):
        delete_account(account["acctid"])
        st.rerun()