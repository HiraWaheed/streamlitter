import streamlit as st

books_page = st.Page("books.py", title="Books Page", icon="📚")
search = st.Page("search.py", title="Search Book Page", icon="🔍")
borrow = st.Page("borrow.py", title="Borrow Book Page", icon="📖")
st.sidebar.image("static/library.jpg")
pg = st.navigation([books_page, search, borrow])


pg.run()