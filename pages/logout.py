import streamlit as st
if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is not None:
    st.success("You have been logged out")
    st.session_state.user = None    
    st.rerun()