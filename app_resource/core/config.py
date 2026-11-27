from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

class SettingsMB(BaseSettings):
    APP_NAME: str = "hii_learn"
    APP_ENV: Literal[
        "development",
        "testing",
        "production"
    ] = "development"
     
    DEBUG: bool = True

    DATABASE_URL: str
    TEST_DATABASE_URL: str

    SECRET_KEY: SecretStr
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    PASSWORD_RESET_TOKEN_EXPIRE_MINUTES: int = 15
    EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES: int = 30

    FRONTEND_URL: str = "http://localhost:5173"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = SettingsMB()  # type: ignore[call-arg]
