from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/hello/<name>',methods=['GET'])

def hello(name):
    return f"Hello,{name}!!!"


if __name__=='__main__':
    app.run(debug=True)