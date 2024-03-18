from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_url: str = "postgres"
    db_echo: bool = True

    # Reading secret file ".env"
    model_config = SettingsConfigDict(env_file=".env")  # There are db_url, db_url_test


settings = Settings()
