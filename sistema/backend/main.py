from fastapi import FastAPI
from config import settings


app = FastAPI()
print(settings.database_url)

@app.get("/health")
async def read_health():
    return {"status": "healthy"}