from flask import Flask ,jsonify,request

app = Flask(__name__)

@app.route('/square/<float:num>',methods=['GET'])
def calc_square(num):
    squre = num ** 2
    return jsonify({'input':num, 'square': squre})

@app.route('/cube/<int:num>',methods=['GET'])
def calc_cube(num):
    cube = num ** 3
    return jsonify({'input':num,'cube':cube})

if __name__ == '__main__':
    app.run(debug=True)