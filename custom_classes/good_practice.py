# Pattern 1: Define your class in a separate module
import streamlit as st
from my_class import MyClass #MyClass doesn't get redefined with each run

if "my_instance" not in st.session_state:
  st.session_state.my_instance = MyClass("foo", "bar")

# Displays True on every rerun
st.write(isinstance(st.session_state.my_instance, MyClass))

st.button("Rerun")