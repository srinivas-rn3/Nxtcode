class Book:
    def __init__(self,title,author,genre):
        self.title = title 
        self.author = author
        self.genre = genre 

    def __repr__(self):
        return f"Book(title='{self.title}',author='{self.author}',genre='{self.genre}')"
    
# Create a list of Book objects
books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
    Book("To Kill a Mockingbird", "Harper Lee", "Classics"),
    Book("1984", "George Orwell", "Dystopian"),
    Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
]
# Use map to create a list of book titles 
titles  = list(map(lambda book:book.title,books))

# Use join  to concate titles into a string
title_string = " ,".join(titles)

# Print the result 
print(f"Book Titles: {title_string}")

# Use repr  to get a string representation  of each book
books_repr =  list(map(repr,books))

# Use join to concat repr  strings into a  string 
books_string = "\n".join(books_repr)

#print the result
print(f"\nBook Objects:\n{books_string}")

