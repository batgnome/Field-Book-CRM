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
pages = [
    st.Page("pages/login"),
    st.Page("pages/test.py")
]
pg = st.navigation(pages)

pg.run()