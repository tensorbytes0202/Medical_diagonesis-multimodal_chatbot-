from fastapi import FastAPI
from app.routes import predict_text
from app.routes import predict_skin   # 👈 ADD THIS

app = FastAPI()

app.include_router(predict_text.router)
app.include_router(predict_skin.router)  # 👈 ADD THIS