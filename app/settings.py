from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM: str

    class Config:
        env_file = ".env"


settings = Settings()