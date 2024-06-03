from flask import Flask ,jsonify,request
import random 
'''
app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The way to get started is to quit talking and begin doing. - Walt Disney"
]

@app.route('/quote',methods=['GET'])
def get_quotes():
    return jsonify({'quote':random.choice(quotes)})

if __name__ == '__main__':
    app.run(debug=True)
'''

app = Flask(__name__)

@app.route('/square',methods=['GET'])

def calc_square():
    number = request.args.get('number')
    if not number:
        return jsonify({'Error':'Number parameter is missing'}),400
    try:
        number = float(number)
    except ValueError:
        return jsonify({'Error':'Invalid number fromat'}),400
    square =  number ** 2
    return jsonify({'input': number,'square':square})

if __name__ == '__main__':
    app.run(debug=True)

#other version
'''
app = Flask(__name__)

@app.route('/square/<float:num>',methods=['GET'])
def calc_square(num):

    squre = num ** 2
    return jsonify({'input':num, 'square': squre})
   
if __name__ =='__main__':
    app.run(debug=True)
'''