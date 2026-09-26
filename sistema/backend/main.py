from fastapi import FastAPI
from sqlalchemy import text

from database import engine

app = FastAPI()


@app.get("/health")
async def read_health():
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))
    return {"status": "healthy", "database": "ok"}