from flask  import Flask,request,jsonify 

app = Flask(__name__)

@app.route("/add",methods=['Post'])
def add():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        # Extract the two numbers from the data
        num1 = data.get('num1')
        num2 = data.get('num2')
          # Ensure both numbers are provided
        if num1 is None or num2  is None:
            return jsonify({'error':'Both num1 and num2 are required!!'})
          
        #calculate
        result = num1 + num2 
          
        # Return the result as JSON
        return jsonify({'num1':num1,'num2':num2,'Sum':result})
    
    except Exception as e:
        return jsonify({'Error':str(e)}),500
    
if __name__ =='__main__':
    app.run(debug=True)