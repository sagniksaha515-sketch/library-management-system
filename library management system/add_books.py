from utils import books
def add():
    book_code = input("Enter book code: ")
    book_name = input("Enter book name: ")

    books[book_code] = book_name
    print("Book added successfully")