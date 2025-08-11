from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field

load_dotenv()

class Settings(BaseSettings):
    postgres_url: str = Field()
    redis_url: str = Field()

ENVS = Settings()



