from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()


DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

SECRET_AUTH = os.environ.get('SECRET_AUTH')


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    @property
    def DATABASE_URL_asyncpg(self):
        return f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    @property
    def DATABASE_URL_psycopg(self):
        return f'postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    # model_config = SettingsConfigDict(env_file='.env')
    

settings = Settings()