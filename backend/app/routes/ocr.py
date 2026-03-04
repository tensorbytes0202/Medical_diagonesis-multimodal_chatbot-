from fastapi import APIRouter, UploadFile, File
import shutil
from app.services.ocr_service import extract_text

router = APIRouter()

@router.post("/")
async def ocr_image(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(path)
    return {"extracted_text": text}