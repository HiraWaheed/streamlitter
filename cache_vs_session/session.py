import streamlit as st
import pandas as pd
import numpy as np

#if session state is used, the random data generated persists across a session for a user. 
# 1 session = 1 app view instance in the browser.
def generate_random():
    return pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

if "df" not in st.session_state:
    st.session_state.df = generate_random()

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)