from fastapi import APIRouter
from pydantic import BaseModel
from app.services.text_service import chatbot_response

router = APIRouter()

class ChatInput(BaseModel):
    message: str

@router.post("/")
async def chat(data: ChatInput):
    reply = chatbot_response(data.message)
    return {"reply": reply}