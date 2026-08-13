# # streamlit_app.py

# import streamlit as st

# # Initialize connection.
# conn = st.connection("neon", type="sql")

# # Perform query.
# df = conn.query('SELECT * FROM accounts;', ttl="10m")

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.company} has a :{row.company}:")
import streamlit as st
if "user" not in st.session_state:
    st.session_state.user = None
st.header("Welcome to the Streamlit App")
if st.session_state.user is None:
    
    pages = [
        st.Page("pages/login.py"),
    
        st.Page("pages/signup.py")
    ]
else:
    pages = [
        st.Page("pages/test.py"),
        st.Page("pages/logout.py"),
        st.Page("pages/profile.py"),
        st.Page("pages/account_main.py")
    ]
pg = st.navigation(pages,position="top")


pg.run()