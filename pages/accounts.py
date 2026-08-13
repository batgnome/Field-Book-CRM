import streamlit as st
from db.accounts import get_accounts, create_account

if "user" not in st.session_state:
    st.session_state.user = None


st.title("Accounts")
accounts = get_accounts() #-> table
if accounts.empty:
    st.info("No accounts found.")
else:
    st.dataframe(accounts,hide_index=True,
                 use_container_width=True)
# from pages.create_address import create_address_form
# from pages.create_contact import create_contact_form, drop_down_contacts


with st.form("Create an account"):
    st.write("Welcome! Create account here:")

   
    company = st.text_input("company")
    primaryContactId = st.text_input("primary Contact Id")
    submitted = st.form_submit_button("Submit")

    st.selectbox("Select a contact", options=["none"])
    # contactid = drop_down_contacts()
    # from pages.create_address import create_address_form
    # from pages.create_contact import create_contact_form
if submitted:
    company = company.strip()
    if not company:
        st.error("Please fill in all required fields.")
    else:
        create_account(company,primaryContactId)
        st.rerun()

def create_account_form():
    with st.form("Create a new  account"):
        st.write("Welcome! Create account here:")

    #     company = st.text_input("company")
    #     primaryContactId = st.text_input("primary Contact Id")
    #     submitted = st.form_submit_button("Submit")

    #     if submitted:
    #         company = company.strip()
    #         if not company:
    #             st.error("Please fill in all required fields.")
    #         else:
    #             create_account(company,primaryContactId)
    #             st.rerun()
    pass
st.button("create a new account", on_click=create_account_form)

# sub_pages = [
#     st.Page("pages/create_account.py"),
#     st.Page("pages/create_contact.py"),
#     st.Page("pages/show_accounts.py")]