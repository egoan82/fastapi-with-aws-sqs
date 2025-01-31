import os
from enum import Enum
from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()


class EnvironmentEnum(str, Enum):
    PRODUCTION = "production"
    LOCAL = "local"
    DEVELOPMENT = "devel"
    STAGING = "staging"


class GlobalConfig(BaseSettings):
    title: str = "FastAPI with aws SQS"
    description: str = "FastAPI with aws SQS"
    root_path: str = "/routes/v1"
    docs_url: str = "/docs"
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    version: str = "1.0.0"
    allowed_hosts: List[str] = Field(default_factory=lambda: ["*"])
    debug: bool = True
    testing: bool = False
    timezone: str = "UTC"
    environment: EnvironmentEnum = EnvironmentEnum.LOCAL

    aws_key_id: str = os.environ.get("AWS_ACCESS_KEY_ID", "")
    aws_secret_key: str = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
    aws_region: str = os.environ.get("AWS_REGION", "")
    localstack_url: str = os.environ.get("LOCALSTACK_URL", "")
    sqs_queue_url: str = os.environ.get("SQS_QUEUE_URL", "")

    exclude_urls: List[str] = Field(default_factory=lambda: ["/docs", "/redoc", "/openapi.json"])

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

@lru_cache()
def get_configuration() -> GlobalConfig:
    return GlobalConfig()

settings = get_configuration()