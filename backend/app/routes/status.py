from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def check_status():
    return {"status": "API is running properly ✅"}