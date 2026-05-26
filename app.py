from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, "templates"),
            static_folder=os.path.join(BASE_DIR, "static"))

CORS(app)

logging.basicConfig(level=logging.DEBUG)

try:
    model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
    vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))
    logging.info("Model and vectorizer loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model or vectorizer: {e}")
    model = None
    vectorizer = None

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None or vectorizer is None:
            return jsonify({"error": "Model not loaded properly"}), 500

        data = request.get_json()
        
        if not data or "message" not in data:
            return jsonify({"error": "Invalid input"}), 400

        user_input = data["message"]
        logging.debug(f"Received input: {user_input}")

        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]

        logging.debug(f"Prediction: {prediction}")

        return jsonify({"reply": str(prediction)})

    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": "An error occurred during prediction."}), 500


if __name__ == "__main__":
    app.run(debug=True)