import streamlit as st
import pandas as pd
import numpy as np

# if the cache_data decorator is used, the random data generated persists/is cached across all users.
@st.cache_data
def generate_random():
    return pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

if "df" not in st.session_state:
    st.session_state.df = generate_random()

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)