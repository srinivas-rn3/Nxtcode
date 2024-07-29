from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/hello/<name>',methods=['GET'])

def hello(name):
    return f"Hello,{name}!!!"


#
@app.route('/hello/dog',methods=['GET'])
def dog_sound():
        return f"Boaw!!!"


    
@app.route('/fib/<int:num>',methods=['GET'])
def fib_it(num):
    a,b,= 0,1
    fib_se = []
    for _ in range(num):
        fib_se.append(a)
        a,b = b,a+b 
    return jsonify({'message': 'fibannaic series','numbers':num,'output':fib_se})

if __name__ == '__main__':
    app.run(debug=True)