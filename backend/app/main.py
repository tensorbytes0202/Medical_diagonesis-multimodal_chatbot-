from fastapi import FastAPI
from app.routes import chatbot, predict_text, predict_image, ocr, status

app = FastAPI(title="Multimodal AI Healthcare System")

app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(predict_text.router, prefix="/predict-text", tags=["Text"])
app.include_router(predict_image.router, prefix="/predict-image", tags=["Skin"])
app.include_router(ocr.router, prefix="/ocr", tags=["OCR"])
app.include_router(status.router, prefix="/status", tags=["Status"])