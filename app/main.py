from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from app.api import router as api_router
from app.core.config import settings
import uvicorn

from app.core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


main_app = FastAPI(
    title=settings.project_name,
    debug=True,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
main_app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("app.main:main_app", reload=True, host=settings.run.host, port=settings.run.port)
