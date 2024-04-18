import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  database_hostname: str = 'localHost'
  database_port: str  = '5432'
  database_password: str = 'Okanlawon.11'
  database_name: str = 'bookshelves'
  database_username: str = 'postgres'
  secret_key: str = 'jhscjkdlifudiosdusdulho'
  algorithm: str = 'HS256'
  access_token_expire_minutes: int = 60
    
  class config:
    env_file = ".env"

setting = Settings()