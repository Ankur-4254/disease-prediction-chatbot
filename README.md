# Disease Predictor Chatbot

A Flask-based web application that predicts diseases based on user-provided symptoms using a machine learning model.

## Features

- **Symptom-based Disease Prediction**: Input symptoms and get predicted diseases
- **Web Interface**: Clean, responsive web UI
- **Voice Input Support**: Voice-to-text functionality for symptoms
- **Machine Learning Model**: Trained on common symptom-disease mappings
- **RESTful API**: JSON-based API for predictions

## Project Structure

```
Disease-Predictor-Chatbot-Flat/
├── app.py                 # Main Flask application
├── train_model.py         # Script to train the ML model
├── model.pkl             # Trained machine learning model
├── vectorizer.pkl        # Text vectorizer for symptoms
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html       # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css    # CSS styles
│   └── js/
│       └── script.js    # JavaScript functionality
└── README.md            # This file
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or download the project** to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd Disease-Predictor-Chatbot-Flat
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. **Use the chatbot**:
   - Type symptoms in the input field
   - Click "Send" or press Enter
   - Use the voice button (🎤) for voice input
   - View the predicted disease in the chat

## API Usage

The application provides a REST API endpoint for predictions:

**Endpoint**: `POST /predict`

**Request Body**:
```json
{
  "message": "fever cough sore throat"
}
```

**Response**:
```json
{
  "reply": "flu"
}
```

**Example using curl**:
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"message":"fever cough sore throat"}' \
  http://127.0.0.1:5000/predict
```

## Training the Model

If you want to retrain the model with new data:

1. **Modify the training data** in `train_model.py`
2. **Run the training script**:
   ```bash
   python train_model.py
   ```
3. **Restart the Flask application**

## Supported Diseases

The current model can predict:
- Flu
- Cold
- Pneumonia
- Food poisoning
- Migraine
- Allergy
- Arthritis
- Indigestion
- Measles
- Hypothyroidism
- Tuberculosis
- Malaria
- Diabetes
- Anxiety disorder
- Alzheimer's
- Viral infection
- Stomach flu
- COVID-19
- Urinary tract infection
- Hypertension

## Troubleshooting

- **Port already in use**: Change the port in `app.py` or kill the existing process
- **Model loading errors**: Ensure `model.pkl` and `vectorizer.pkl` exist
- **Dependency issues**: Reinstall requirements with `pip install -r requirements.txt`

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn (Naive Bayes classifier)
- **Frontend**: HTML, CSS, JavaScript
- **Voice Recognition**: Web Speech API
- **Data Serialization**: joblib

## License

This project is open source and available under the MIT License.
