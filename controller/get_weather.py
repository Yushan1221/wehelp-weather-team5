from fastapi import *
from models import weather_api
router = APIRouter()

@router.get("/api/weather")
async def get_weather():
    res = await weather_api()
    