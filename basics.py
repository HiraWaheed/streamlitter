import streamlit as st
import numpy as np
import pandas as pd
import time
st.text_input("Your name", key="name")
st.text_input("Your age", key="age")
st.spinner("Loading...")
# You can access the value at any point with:
st.session_state.name
st.session_state.age

st.echo("echooooo")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Letter', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Rate your experience',
    1, 5, (2)
)

left_column, middle, right_column = st.columns(3)

with left_column:
    st.text_input("Type something in the column", key="left_input")
    if st.button('Submit'):
        st.write(f"You typed: {st.session_state.left_input}")

    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        chart_data


        df = pd.DataFrame({
            'first column': [1, 2, 3, 4],
            'second column': [10, 20, 30, 40]
            })

        option = st.selectbox(
            'Which number do you like best?',
            chart_data['a'])

        'You selected: ', option

with middle:
    st.button('Press it!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
