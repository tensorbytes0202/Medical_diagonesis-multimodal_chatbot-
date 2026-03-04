import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "text_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))

def predict_disease(symptoms: str):
    symptoms_vectorized = vectorizer.transform([symptoms])
    prediction = model.predict(symptoms_vectorized)[0]
    confidence = max(model.predict_proba(symptoms_vectorized)[0])

    return prediction, float(confidence)