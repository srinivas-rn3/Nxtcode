from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate',methods=['POST'])
def calc():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        # Extract the operation and the two numbers
        operation = data.get('operation')
        num1 = data.get('num1')
        num2 = data.get('num2')
        # Ensure all required fields are provided
        if operation is None or num1 is None or num2 is None:
            return jsonify({'error':'Operation,num1, and num2 are required'}),400
        
        # Perform the calculation based on the operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2 
        elif operation =='multiply':
            result  = num1 * num2 
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error':'Division by zero error'}),400
            result = num1 / num2 
        else:
            return jsonify({'error':'Invalid opertation.Choose from add,subtract,mulitply and divide'}),400
        
        # Return the result as JSON
        return jsonify({'operation':operation,'num1':num1,'num2':num2,'result':result})
    
    except Exception as e:
        return jsonify({'error':str(e)}),500

if __name__ == '__main__':
    app.run(debug=True)