import streamlit as st
from db.accounts import create_account

def create_account_form():
    with st.form("Create an account"):
        st.write("Welcome! Create account here:")

    
        company = st.text_input("company")
        primaryContactId = st.text_input("primary Contact Id")
        submitted = st.form_submit_button("Submit")

        st.selectbox("Primary Contact", options=["none"])
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