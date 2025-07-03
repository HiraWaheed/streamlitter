# Defining an Enum class to represent a fixed set of options or values.
# by default Enum coercion is enforced which considers the classes defined as Enum different. 
from enum import Enum
import streamlit as st

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

selected_colors = set(st.multiselect("Pick colors", options=Color))

if selected_colors == {Color.RED, Color.GREEN}:
    st.write("Hooray, you found the color YELLOW!")