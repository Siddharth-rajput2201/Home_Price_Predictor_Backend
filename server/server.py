from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names_Bangalore', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

# @app.route('/get_location_names_Delhi', methods=['GET'])
# def default_response():
#     response = jsonify({
#         'locations': 'Under Construction'
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

@app.route('/predict_home_price_Bangalore', methods=['GET','POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(host='192.168.0.102')