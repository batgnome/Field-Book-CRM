import streamlit as st
from db.accounts import create_account,get_account


def create_update_account_form(acctid=None):
    if acctid == None:
        title ="Create an account"
    else:
        title ="Update an account"
        account = get_account(acctid)
    with st.form(title):
        st.write("Welcome! " + title+ " here:")

    
        
        if acctid:
            company = st.text_input("company",account["company"])
            primaryContactId = st.text_input("primary Contact Id",account["primarycontactid"])
            
        else:
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