from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)
model = joblib.load('fish_weight_model.pkl')

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_weight():
    # Load the traned model
    data = request.get_json()
    print('daaaatttt', data)
    length_ver = data['length_ver']
    length_dia = data['length_dia']
    length_cro = data['length_cro']
    height = data['height']
    width = data['width']

    prediction_data = [[length_ver, length_dia, length_cro, height, width]]
    prediction = model.predict(prediction_data)[0]

    return jsonify({'predicted_weight': prediction})

if __name__ == '__main__':
    app.run(debug=True, port= 8000)

