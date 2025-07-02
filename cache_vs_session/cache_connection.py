import streamlit as st
import time

# This function will cache resource loading to avoid reloading it on every interaction. 
@st.cache_resource
def load_heavy_resource():
    st.write("Loading heavy resource... (this should only run once)")
    time.sleep(5)  
    return "Heavy Resource Loaded"

if st.button("Load Resource"):
    resource = load_heavy_resource()
    st.success(resource)