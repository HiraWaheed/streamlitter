import streamlit as st
import os

conn = os.environ.get("DB_CONN", "Not Found")
st.write("Connection established for:", conn)

conn_value = st.secrets[conn]
st.write("Connection value from secrets:", conn_value)
