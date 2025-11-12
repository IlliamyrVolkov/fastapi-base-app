from fastapi import FastAPI
from api import router as api_router
from core.config import settings
import uvicorn


# Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/")
def root():
    return {"message": "Server is running 🚀"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host=settings.run.host, port=settings.run.port)