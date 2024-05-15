from flask import Flask,jsonify,request 

app = Flask(__name__)

# Dummy list of books
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen"},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger"}
]

# Route to get all books
@app.route("/books",methods=["GET"])
def get_books():
    return jsonify(books)

# Route to get a single book by ID
@app.route("/books/<int:book_id>",methods=["GET"])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id),None)
    if book:
        return jsonify(book)
    return jsonify({"message":"Book not found"}),404

# Route to add a new book
@app.route("/books",methods=["POST"])
def add_book():
    new_book = request.json
    if not new_book  or 'title' not in  new_book or 'author' not in  new_book:
        return jsonify({"Message":"Invalid book data!!"}),400
    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify({"message":"Book is addded sucessfully","book":new_book}),201

# Route to update an existing book
@app.route("/books/<int:book_id>",methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id),None)
    if not book:
        return jsonify({"message":"Book not found!!"}),404
    data = request.json
    if 'title' in data:
        book['title'] = data['title']
    if 'author' in data:
        book['author'] = data['author']
    return jsonify({"message":"Book updated successfully", "book":book})

# Route to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)