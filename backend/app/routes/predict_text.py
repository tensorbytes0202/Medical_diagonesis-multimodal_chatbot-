from fastapi import APIRouter
from app.services.text_service import predict_disease

router = APIRouter()

@router.post("/predict-text")
def predict_text(symptoms: str):
    disease, confidence = predict_disease(symptoms)

    return {
        "predicted_disease": disease,
        "confidence": round(confidence, 2)
    }