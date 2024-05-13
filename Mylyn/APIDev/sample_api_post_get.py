from flask import Flask,jsonify,request 

app = Flask(__name__)

# Dummy list of books
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

# Route to get all books
@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)


# Route to add a new book
@app.route('/books',methods=['POST'])
def add_books():
    new_book = request.json 
    books.append(new_book)
    return jsonify({"message":"Book added!!","book":new_book}),201

if __name__ =='__main__':
    app.run(debug=True)