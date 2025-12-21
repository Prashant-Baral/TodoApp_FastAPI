from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT:str = "PRODUCTION"
    JWT_SECRET:str
    JWT_ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int=10
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache() #so that all of this is only loaded once
def get_settings():
    return Settings()
settings = get_settings()