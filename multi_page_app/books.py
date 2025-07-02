import streamlit as st
 
st.markdown("# Books page  📚")
st.sidebar.markdown("# Books page 📚")

add_books_form = st.form("books_form")
with add_books_form:
    title = st.text_input("Book Title", key="book_title")
    author = st.text_input("Author", key="author")
    genre = st.text_input("Genre", key="genre")
    book_image = st.file_uploader("Upload Book Cover", type=["jpg", "png"], key="book_cover")
    submitted = st.form_submit_button("Add book")
    if submitted:
        st.write("Book with details", (title,author,genre) , "added")

