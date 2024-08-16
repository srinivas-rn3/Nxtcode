from flask import Flask,jsonify,request

app = Flask(__name__)

# In-memory storage for user profiles
users = {}

@app.route('/user',methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = len(users)+1
    name = data.get('name')
    email = data.get('email')
    age  = data.get('age')
    
    if not name or not email  or not age:
        return jsonify({'error':'Name , email , and age are required'}),400
    users[user_id] = {
        'id': user_id,
        'name': name,
        'email': email,
        'age':age
    }
    return jsonify(users[user_id]),201
@app.route('/user/<int:user_id>',methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error':'User not found'}),400
if __name__ == '__main__':
    app.run(debug=True)
        