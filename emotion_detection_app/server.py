from flask import Flask, request, jsonify
from emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'Input text cannot be blank'}), 400

    result = emotion_predictor(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
