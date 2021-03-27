from pydantic import BaseSettings


class Settings(BaseSettings):
    api_v1: str = 'v1'
