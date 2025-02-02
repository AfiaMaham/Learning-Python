
import streamlit as st

if "books" not in st.session_state:
    st.session_state["books"] = []

class Library:
    def addBooks(self):
        title = st.text_input("Enter title: ")
        author = st.text_input("Enter author name: ")
        publisher = st.text_input("Enter publisher name: ")
        isbn = st.number_input("Enter ISBN number:", step=1, format="%d")
        status = "Available"

        if st.button("Add"):
            new_book = {'title': title, 'author': author, 'publisher': publisher, 'isbn': isbn, 'status': status}
            st.session_state["books"].append(new_book)
            st.success("Book added successfully")

    def removeBooks(self):
        name = st.text_input("Enter name of book to remove: ")
        if st.button("Remove"):
            books = st.session_state["books"]
            for book in books:
                if book["title"].lower() == name.lower():
                    books.remove(book)
                    st.success("Book removed successfully")
                    return
            st.warning("Book not found")

    def borrowBooks(self):
        name = st.text_input("Enter name of book to borrow: ")
        if st.button("Borrow"):
            books = st.session_state["books"]
            for book in books:
                if book["title"].lower() == name.lower():
                    if book["status"] == "Available":
                        book["status"] = "Borrowed"
                        st.success("You have borrowed the book. Return within 3 weeks.")
                    else:
                        st.warning("Already borrowed by someone")
                    return
            st.warning("Book not found")

    def returnBooks(self):
        name = st.text_input("Enter name of book to return: ")
        if st.button("Return"):
            books = st.session_state["books"]
            for book in books:
                if book["title"].lower() == name.lower():
                    if book["status"] == "Borrowed":
                        book["status"] = "Available"
                        st.success("Thank you for returning the book.")
                    else:
                        st.warning("This book was not borrowed")
                    return
            st.warning("Book not found")

    def searchBooks(self):
        name = st.text_input("Enter name of book to search: ")
        if st.button("Search"):
            books = st.session_state["books"]
            for book in books:
                if book["title"].lower() == name.lower():
                    st.text(f"Name: {book['title']} | Author: {book['author']} | Publisher: {book['publisher']} | ISBN: {book['isbn']} | Status: {book['status']}")
                    return
            st.warning("Book not found")

    def displayBooks(self):
        if st.button("Display"):
            books = st.session_state["books"]
            if len(books) != 0:
                for book in books:
                    st.text(f"Name: {book['title']} | Author: {book['author']} | Publisher: {book['publisher']} | ISBN: {book['isbn']} | Status: {book['status']}")
            else:
                st.warning("No books available")


obj = Library()
st.title("Welcome to Library")

person = st.selectbox("Select any option", ("", "Admin", "Student"))
if person == "Admin":
    choice = st.selectbox("Select your choice", ("", "Add", "Remove", "Display"))
    if choice == "Add":
        obj.addBooks()
    elif choice == "Remove":
        obj.removeBooks()
    elif choice == "Display":
        obj.displayBooks()
else:
    choice = st.selectbox("Select your choice", ("", "Search", "Borrow", "Return"))
    if choice == "Search":
        obj.searchBooks()
    elif choice == "Borrow":
        obj.borrowBooks()
    elif choice == "Return":
        obj.returnBooks()


