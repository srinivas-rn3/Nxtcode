import json

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Available: {self.available}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def lend_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"Book '{book.title}' has been lent.")
                    return
                else:
                    print(f"Book '{book.title}' is not available for lending.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"Book '{book.title}' has been returned.")
                    return
                else:
                    print(f"Book '{book.title}' is already available.")
                    return
        print(f"Book '{title}' not found in the library.")

    def display_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(book)
        else:
            print("No books available in the library.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.books = [Book(**book_data) for book_data in data]

def main():
    library = Library()

    # Load existing data from file (if any)
    try:
        library.load_from_file("library_books.json")
        print("Existing data loaded successfully.")
    except FileNotFoundError:
        print("No existing data found.")

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Display Available Books")
        print("6. Save Data to File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            library.add_book(Book(title, author, genre))

        elif choice == '2':
            title = input("Enter book title to remove: ")
            library.remove_book(title)

        elif choice == '3':
            title = input("Enter book title to lend: ")
            library.lend_book(title)

        elif choice == '4':
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == '5':
            library.display_available_books()

        elif choice == '6':
            library.save_to_file("library_books.json")
            print("Data saved to file successfully.")

        elif choice == '7':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
