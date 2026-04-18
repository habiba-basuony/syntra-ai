from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GROQ_API_KEY: str = ""
    APP_NAME: str = "Syntra.AI"
    DEBUG: bool = True

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
