from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from dependencies.aws_sqs import listen_sqs
from routes.router import router

app = FastAPI(
    title=settings.title,
    description=settings.description,
    version=settings.version,
    debug=settings.debug,
    docs_url=settings.docs_url,
    openapi_url=settings.openapi_url,
    redoc_url=settings.redoc_url,
    root_path=settings.root_path,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"FastAPI": "Aws with sqs"}


if __name__ == "__main__":
    listen_sqs()