from flask import Flask,jsonify,request 

import requests 


app = Flask(__name__) 

@app.route('/weather',methods=['GET'])
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if not lat or not lon:
        return jsonify({"Error":"latitude and longtitude parameters are required!!"}),404
    
    api_key = '47d244805373d83af4de0b0f073b1d73'
    url='https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code  == 200:  
        data = response.json()
        weather = {
            'location':data['name'],
            'temperature':data['main']['temp'],
            'decription':data['weather'][0]['description']

        }
        return jsonify(weather)
    else:
        return jsonify({'error':'Failed to fetch the data'}),response.status_code
    
if __name__ == '__main__':
    app.run(debug=True)
    
'''
to run 
http://localhost:5000/weather?lat=40.7128&lon=74.0060

New York City, USA:

Latitude: 40.7128
Longitude: -74.0060
London, UK:

Latitude: 51.5074
Longitude: -0.1278
'''