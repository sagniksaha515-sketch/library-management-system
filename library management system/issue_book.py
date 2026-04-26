"""from utils import issue_book

def isuue():
    student_name = input("Enter student name: ")
    book_code = input("Enter book code: ")
    weeks = int(input("Enter number of weeks: "))

    result = issue_book(student_name, book_code, weeks)

    if isinstance(result, str):
        print(result)
    else:
        print("Book Issued Successfully")
        print(f"Issue Date: {result['issue_date']}")
        print(f"Return Date: {result['return_date']}")
        print(f"Price: {result['price']} Rs")"""""
          
from utils import books,issued_books

def issue():
    book_id = input("Enter Book ID to issue: ")

    if book_id in books:

        try:
            weeks = int(input("For how many weeks? (1-4): "))
        except ValueError:
            print("Please enter a valid number")
            return

        # Pricing table
        price_chart = {
            1: 10,
            2: 20,
            3: 25,   # discount
            4: 35    # more discount
        }

        if weeks not in price_chart:
            print("Invalid duration. Choose between 1 to 4 weeks.")
            return

        price = price_chart[weeks]

    
        books[book_id] = books.pop(book_id)

        print("Book issued successfully")
        print(f"Duration: {weeks} week(s)")
        print(f"Total Price: ₹{price}")

    else:
        print("Book not available")