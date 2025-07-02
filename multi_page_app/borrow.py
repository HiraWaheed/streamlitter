import streamlit as st
import time

st.markdown("# Borrow Page")
st.sidebar.markdown("# Borrow Page")

# Non-fragment part: Simulate a long loading or tracking counter
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1
st.write(f"🔁 App rerun count: {st.session_state.counter}")

# Non-fragment part: Simulate expensive processing
with st.spinner("Simulating expensive load..."):
    time.sleep(1)

# Fragment part
@st.fragment()
def toggle_and_text():
    borrow_count = st.slider("How many books do you need to borrow?", 0, 2, 5)
    st.write("I want to borrow", borrow_count, "books")
    
toggle_and_text()

st.button("Borrow Book")