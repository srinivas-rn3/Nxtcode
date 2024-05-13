from flask import Flask,jsonify 
app = Flask(__name__)
# Define a simple route
@app.route('/hello',methods=['GET'])
def hello1():
    return jsonify({'message':'Hello world!'})

if __name__ == '__main__':
    app.run(debug=True)