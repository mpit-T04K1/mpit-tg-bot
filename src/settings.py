from functools import cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    BOT_TOKEN: str
    REGISTRATION_URL: str
    DATABASE_PATH: str = "database/database.db"

    @cached_property
    def sqlite_url(self):
        return f"sqlite:///{self.DATABASE_PATH}"


settings = Settings()  # type: ignore
