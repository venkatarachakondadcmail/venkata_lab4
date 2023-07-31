from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)
model = joblib.load('fish_weight_model.pkl')



@app.route('/predict', methods=['POST'])
def predict_weight():
    # Load the traned model
    
    data = request.get_json()
    length_ver = data['LengthVer']
    length_dia = data['LengthDia']
    length_cro = data['LengthCro']
    height = data['Height']
    width = data['Width']

    prediction_data = [[length_ver, length_dia, length_cro, height, width]]
    prediction = model.predict(prediction_data)[0]

    return jsonify({'predicted_weight': prediction})

if __name__ == '__main__':
    app.run(port=8000, debug=True)

