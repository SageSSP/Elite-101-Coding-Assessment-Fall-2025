# David Parker

from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# Available books
def view_available_books(library_books):
    print("Available Books: \n")
    for book in library_books:
        if book["available"]:
            print(f"ID: {book["id"]}")
            print(f"Title: {book["title"]}")
            print(f"Author: {book["author"]}")
            print("\n-----------------------\n")

# -------- Level 2 --------
# Author or genre search
def search_books(library_books):
    term = input("Enter author or genre to search: ").lower()
    print("Search Results: \n")
    for book in library_books:
        if book("author").lower() == term or book("genre").lower() == term:
            print(f"ID: {book["id"]}")
            print(f"Title: {book["title"]}")
            print(f"Author: {book["author"]}")
            print("\n-----------------------\n")

# -------- Level 3 --------
# Book checkout
def checkout_book(library_books):
    book_id = input("Enter the ID of the book you would like to check out:")
    for book in library_books:
        if book["id"] == book_id:
            if book["available"] == True:
                book["available"] = False
                due = datetime.today() + timedelta(weeks=2)
                book["due_date"] = due.strftime("%Y-%m-%d")
                book["checkouts"] += 1
                print(f"You have successfully checked out {book["title"]}.")
                print("Due date:", book["due_date"])
            else:
                print("Sorry, this book is already checked out.")
                return
    print("Book ID not found.")

# -------- Level 4 --------
# Book return
def return_book(library_books):
    book_id = input("Enter the ID of the book to return:")
    for book in library_books:
        if book["id"] == book_id:
            book("available") = True
            book("due_date") = None
            print(f"You have successfully returned {book["title"]}.")
            return
    print("Book ID not found.")

# TODO: Create a function to list all overdue books
# Overdue books
def view_overdue_books(library_books):
    print("Overdue Books: \n")
    today = datetime.today()
    for book in library_books:
        if book["available"] == False and book("due_date") is not None:
            due = datetime.striptime(book["due_date"], "%Y-%m-%d")
            if due < today:
                print(f"{book["title"]} was due on {book["due_date"]}.")
                found = True
    if not found:
        print("No overdue books.")

# -------- Level 5 --------
class Book:
    def __init__(self, id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

    def checkout(self):
        if self.available:
            self.available = False
            due = datetime.today() + timedelta(weeks=2)
            self.due_date = due.strftime("%Y-%m-%d")
            self.checkouts += 1
            print(f"You have successfully checked out {self.title}.")
            print("Due date:", self.due_date)
        else:
            print("Sorry, this book is already checked out.")

    def return_book(self):
        self.available = True
        self.due_date = None
        print(f"You have successfully returned {self.title}.")

    def is_overdue(self):
        if not self.available and self.due_date:
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            return due < datetime.today()
        return False
    
# Library
books = [
    Book("B1", "The Lightning Theif", "Rick Riordan", "Fantasy", True, None, 2),
    Book("B2", "To Kill a Mockingbird", "Harper Lee", "Historical", False, "2025-11-01", 5),
    Book("B3", "The Great Gatsby", "F. Scott Fitzgerald", "Classic", True, None, 3),
    Book("B4", "1984", "George Orwell", "Dystopian", True, None, 4),
    Book("B5", "Pride and Prejudice", "Jane Austen", "Romance", True, None, 6),
    Book("B6", "The Hobbit", "J.R.R. Tolkien", "Fantasy", False, "2025-11-10", 8),
    Book("B7", "Fahrenheit 451", "Ray Bradbury", "Science Fiction", True, None, 1),
    Book("B8", "The Catcher in the Rye", "J.D. Salinger", "Coming-of-Age", False, "2025-11-12", 3)
]

# Menu
while True:
    print("\nLibrary Menu:")
    print("1. View Available Books")
    print("2. Search Books by Author or Genre")
    print("3. Checkout a Book")
    print("4. Return a Book")
    print("5. View Overdue Books")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        for book in books:
            if book.available:
                print(f"{book.id}: {book.title} by {book.author}")
    
    elif choice == "2":
        term = input("Enter author or genre to search: ").lower()
        print("Search Results: \n")
        for book in books:
            if book.author.lower() == term or book.genre.lower() == term:
                print(f"{book.id}: {book.title} by {book.author}")
    
    elif choice == "3":
        book_id = input("Enter the ID of the book you would like to check out:")
        for book in books:
            if book.id == book_id:
                book.checkout()
                break
        else:
            print("Book ID not found.")
    
    elif choice == "4":
        book_id = input("Enter the ID of the book to return:")
        for book in books:
            if book.id == book_id:
                book.return_book()
                break
        else:
            print("Book ID not found.")

    elif choice == "5":
        print("Overdue Books: \n")
        found = False
        for book in books:
            if book.is_overdue():
                print(f"{book.title} was due on {book.due_date}.")
                found = True
        if not found:
            print("No overdue books.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")