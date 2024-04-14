import uvicorn
from fastapi import FastAPI

from app.routers.routers import router as v1_router

app = FastAPI()

app.include_router(v1_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
