from contextlib import asynccontextmanager

from fastapi import FastAPI
from api import router as api_router
from core.config import settings
import uvicorn

from core.models import db_helper


# Base.metadata.create_all(bind=engine)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()
main_app = FastAPI(debug=True, lifespan=lifespan)
main_app.include_router(api_router, prefix=settings.api.api_prefix)

@main_app.get("/")
def root():
    return {"message": "Server is running 🚀"}

if __name__ == "__main__":
    uvicorn.run("main:main_app", reload=True, host=settings.run.host, port=settings.run.port)