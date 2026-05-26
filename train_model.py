import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Expanded training data
symptoms = [
    "fever cough sore throat body ache",              # flu
    "runny nose sneezing headache",                   # cold
    "chest pain shortness of breath cough",           # pneumonia
    "stomach pain diarrhea vomiting",                 # food poisoning
    "headache nausea sensitivity to light",           # migraine
    "itchy eyes sneezing runny nose",                 # allergy
    "joint pain fatigue weight loss",                 # arthritis
    "bloating nausea constipation stomach pain",      # indigestion
    "fever rash swollen glands",                      # measles
    "fatigue dry skin weight gain cold intolerance",  # hypothyroidism
    "night sweats cough fever weight loss",           # tuberculosis
    "muscle pain chills sweating high fever",         # malaria
    "increased thirst frequent urination fatigue",    # diabetes
    "anxiety insomnia rapid heartbeat chest tightness", # anxiety disorder
    "memory loss confusion disorientation",           # Alzheimer’s
    "sore throat runny nose cough mild fever",        # viral infection
    "abdominal cramps vomiting diarrhea",             # stomach flu
    "loss of smell fatigue dry cough",                # COVID-19
    "pain during urination frequent urination",       # urinary tract infection
    "dizziness blurred vision headache",              # hypertension
]

labels = [
    "flu",
    "cold",
    "pneumonia",
    "food poisoning",
    "migraine",
    "allergy",
    "arthritis",
    "indigestion",
    "measles",
    "hypothyroidism",
    "tuberculosis",
    "malaria",
    "diabetes",
    "anxiety disorder",
    "alzheimer's",
    "viral infection",
    "stomach flu",
    "covid-19",
    "urinary tract infection",
    "hypertension",
]

# Vectorize the symptoms
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(symptoms)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Save model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model and vectorizer saved successfully.")
