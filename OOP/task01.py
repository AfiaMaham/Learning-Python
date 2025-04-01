
import pandas as pd

books = []
members = []
data = ""
class Library:
    def addBooks(self):
        title = input("Enter title: ")
        author = input("Enter author name: ")
        publisher = input("Enter publisher name: ")
        isbn = input("Enter ISBN number:")
        new_book = {'title': title, 'author': author, 'publisher': publisher, 'isbn': isbn}
        books.append(new_book)
        print("Book added successfully")

    def removeBooks(self):
        name = input("Enter name of book to remove: ")
        for book in books:
            if book["title"] == name:
                books.remove(book)
                print("Book removed successfully")
                return
            print("Book not found")

    def searchBooks(self):
        name = input("Enter name of book to search: ") 
        for book in books:
            if book["title"] == name:
                print(f"Name: {book['title']} | Author: {book['author']} | Publisher: {book['publisher']} | ISBN: {book['isbn']}")
                return
            print("Book not found")

    def displayBooks(self):
        data = pd.DataFrame(books)
        print(data)

class Member:
    def __init__(self, name, cnic, member_id):
        self.name = name
        self.cnic = cnic
        self.member_id = member_id
        self.borrowed_books = []
        
    def borrowBook(self):
        book_name = input("Enter the name of the book to borrow: ")
        for book in books:
            if book["title"] == book_name:
                self.borrowed_books.append(book)
                books.remove(book)
                print("Book borrowed successfully")
                return
        print("Book not available")
    
    def returnBook(self):
        book_name = input("Enter the name of the book to return: ")
        for book in self.borrowed_books:
            if book["title"] == book_name:
                books.append(book)
                self.borrowed_books.remove(book)
                print("Book returned successfully")
                return
        print("You have not borrowed this book")

library = Library()
print("Welcome to Library")

while True:
    person = input("""Choose one option:
                1- Admin
                2- Student
                3- Exit""")
    if person == "1":
        while True:
            choice = input("""Choose one option:
                    1- Add Book
                    2- Remove Book
                    3- Display Books
                    4- Exit""")
            if choice == "1":
                library.addBooks()
            elif choice == "2":
                library.removeBooks()
            elif choice == "3":
                library.displayBooks()
            elif choice == "4":
                break
    elif person == "2":
        name = input("Enter your name: ")
        cnic = input("Enter your CNIC: ")
        member_id = input("Enter your ID: ")
        student = Member(name, cnic, member_id)
        members.append(student)
        
        while True:
            choice = input("""Select option:
                    1- Search Book
                    2- Borrow Book
                    3- Return Book
                    4- Exit""")
            if choice == "1":
                library.searchBooks()
            elif choice == "2":
                student.borrowBook()
            elif choice == "3":
                student.returnBook()
            elif choice == "4":
                break
    elif person == "3":
        break