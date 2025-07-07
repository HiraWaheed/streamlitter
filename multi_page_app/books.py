import streamlit as st
from csv_handler import add_book_to_csv, get_books_list
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
        response = add_book_to_csv(title, author, genre, book_image)
        if response:
            st.write("Book with details", (title,author,genre) , "added")
        else:
            st.write("Failed to add book. Please try again.")

try:
    df = get_books_list()  
    if df:
        custom_headers = ["Title", "Author", "Genre"]
        formatted_data = [dict(zip(custom_headers, row)) for row in df]
        
        st.title("List of Books Available")
        st.dataframe(formatted_data)  

except Exception as e:
    st.error(f"An error occurred while fetching the books list: {e}")
    st.write("Please ensure the CSV file is correctly set up and accessible.")