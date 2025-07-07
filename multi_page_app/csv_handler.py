import csv
import os
import streamlit as st

def add_book_to_csv(title, author, genre, book_image):
    """Add a book to the CSV file."""
    path = st.secrets[os.environ.get("DB_CONN", "Not Found")]["csv_path"]
    with open(path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([title, author, genre, book_image.name if book_image else ""])
    return True

def get_books_list():
    """Get the list of books from the CSV file."""
    path = st.secrets[os.environ.get("DB_CONN", "Not Found")]["csv_path"]
    books = []
    if os.path.exists(path):
        with open(path, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                books.append(row)
    return books