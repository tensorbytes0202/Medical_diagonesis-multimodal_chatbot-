from fastapi import APIRouter, UploadFile, File
import shutil
from app.services.skin_service import predict_skin

router = APIRouter()

@router.post("/")
async def predict_image(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    disease, confidence = predict_skin(path)
    return {
        "disease": disease,
        "confidence": confidence
    }