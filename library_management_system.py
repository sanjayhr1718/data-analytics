class Library:
    def __init__(self, book_list):
        self.books = book_list

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f" - {book}")

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"\n'{book_name}' has been added to the library.")

    def issue_book(self, book_name, user):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"\n'{book_name}' has been issued to {user}.")
        else:
            print(f"\nSorry, '{book_name}' is not available or already issued.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"\nThank you for returning '{book_name}'.")

def main():
    library_books = ["Python Programming", "Data Structures", "Artificial Intelligence", "Quantum Computing"]
    library = Library(library_books)

    while True:
        print("\n--- Library Management System ---")
        print("1. Display Books")
        print("2. Add a Book")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)
        elif choice == '3':
            book_name = input("Enter the name of the book to issue: ")
            user_name = input("Enter the user's name: ")
            library.issue_book(book_name, user_name)
        elif choice == '4':
            book_name = input("Enter the name of the book to return: ")
            library.return_book(book_name)
        elif choice == '5':
            print("\nExiting the Library Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
