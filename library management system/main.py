from add_books import add
from show_books import show
from issue_book import issue
from return_book import return_book

def main():
    while True:
        print("\n--- Library System ---")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            show()
        elif choice == "3":
            issue()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()