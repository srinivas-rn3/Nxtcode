
class Dog:
    
    #Class variable
    species = "Canis familiaris"

    #Intializer /Intance  variable
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    # Instance  method 
    def bark(self):
        print(f"{self.name} says woof!")
    
#Create instance of the Dog class
dog1 = Dog("Buddy",3)
dog2 = Dog("Max",5)
dog3 = Dog("Meenu",7)

print(f"{dog1.name} is {dog1.age} years old.") 
print(f"{dog2.name} is {dog2.age} years old")
print(f"{dog3.name} is {dog3.age} years old")

#Calling instance method
dog1.bark()
dog2.bark()
dog3.bark()

'''
class Task:
    def __init__(self,description,due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Completed"if self.is_completed else "Not Completed"
        return f"{self.description} (Due:{self.due_date}) - {status}"

class ToDolist:
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)
#example usage
task1 = Task("Finish project","2024-02-01")

task2 = Task("Go to the gym","2024-02-05")
task2.mark_completed()

todo_list= ToDolist()
todo_list.add_task(task1)
todo_list.add_task(task2)

todo_list.display_tasks()
'''
'''
import json

filename = r"C:\Users\srini\OneDrive\Documents\Boooks_26jan.json"

class Book:
    def __init__(self,title,author,genre):
        self.title = title 
        self.author = author 
        self.genre = genre 
        self.avialble = True

    def __str__(self):
        return  f"Title: {self.title},Author: {self.author},Genre: {self.genre}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def remove_book(self,title):
        for  book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return 
        print(f"Book '{title}' not found in the library. ")

    def lend_book(self,title):
        for book in self.books:
            if book.title.lower == title.lower():
                if book.available:
                    book.available = False 
                    print(f"Book '{book.title}' has been lent.")
                    return 
                else:
                    print(f"Book '{book.title}' is already availble.")
                    return 
        print(f"Book '{title}' not found in the library.")
    
    def return_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"Book '{book.title}' has been returned")
                else:
                    print(f"Book'{book.title}' is already availble.")
                    return
        print(f"Book '{title}' not found  in the library.")

    def display_available_book(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(book)
        else:
            print("No books available in the library.")
    
    def save_to_file(self,filename):
        with open(filename,'w') as  file:
            json.dump([book.__dict__ for book in self.books],file)

    def load_from_file(self,filename):
        with open(filename,'r') as file:
            data = json.load(file)
            self.books = [Book(**book_data) for book_data in data]

def main():
            library = Library()
            #Load existing data from file(if any)
            try:
                library.load_from_file(filename)
                print("Existing data loaded  sucessfully.")
            except FileNotFoundError:
                print("File Not Found!!!")
                
            while True:
                print("\nLibrary Managment System Menu:")
                print("1. Add Book")
                print("2. Remove Book")
                print("3. Lend Book")
                print("4. Return Book")
                print("5. Display  Avialble Books")
                print("6. Save Data to File")
                print("7.Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    title = input("Enter  book title: ")
                    author = input("Enter book author: ")
                    genre = input("Enter book genre: ")
                    library.add_book(Book(title,author,genre))
                    
                elif choice == '2':
                    title = input("Enter book title to remove: ")
                    library.remove_book(title)
                elif choice  == '3':
                    title = input("Enter the book title to lend: ")
                    library.lend_book(title)
                elif  choice == "4":
                    title = input("Enter the book title to return: ")
                    library.return_book(title)
                elif choice == "5":
                    library.display_available_book()
                elif choice == "6":
                    library.save_to_file(filename)
                    print("Data is Saved to file sucessfully.")
                elif choice  == "7":
                    print("Existing program.")
                    break 
                else:
                    print("Invalid choice.Please enter a number 1 and 7.")
                
if __name__ =='__main__':
    main()
'''