from utils import books

def show():
    if len(books) == 0:
        print("No books available")
    else:
        print("\nAvailable Books:")
        for book_id, book_name in books.items():  
            print(f"{book_id} : {book_name}")