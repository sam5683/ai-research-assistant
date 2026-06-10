from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):

    GEMINI_API_KEY: str
    GROQ_API_KEY: str
    DATABASE_URL: str = ""


    DEBUG: bool = True
    ENVIRONMENT: str = "development"

    UPLOAD_FOLDER: str = "./uploads"
    MAX_UPLOAD_SIZE: int = 52428800

    VECTOR_DIMENSION: int = 768

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()    