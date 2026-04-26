from utils import books, issued_books

def return_book():
    book_code = input("Enter book code: ")
    damaged_input = input("Is book damaged? (yes/no): ")

    damaged = True if damaged_input.lower() == "yes" else False

    if book_code in books:
        result = books[book_code]
        print("Book Returned Successfully")
    else:
        print("Book not found")