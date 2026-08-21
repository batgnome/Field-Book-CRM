import streamlit as st
from db.accounts import create_account,get_account,update_account
from db.contacts import get_contacts


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
        
        contacts = get_contacts()
        print(contacts)
        contact_options = {
            int(row["contactid"]): f"{row['fname']} {row['lname']}"
            for _, row in contacts.iterrows()
        }

        primaryContactId = st.selectbox(
            "Primary Contact",
            options=[None] + list(contact_options.keys()),
            format_func=lambda contact_id: (
                "None" if contact_id is None
                else contact_options[contact_id]
            )
        )
        # show_create_contact_form()
    
    if acctid:
        if submitted:
            company = company.strip()
            if not company:
                st.error("Please fill in all required fields.")
            else:
                update_account(acctid, company,primaryContactId)
                st.rerun()
    else:
        if submitted:
            company = company.strip()
            if not company:
                st.error("Please fill in all required fields.")
            else:
                create_account(company,primaryContactId)
                st.rerun()