import os
from dotenv import load_dotenv

# Load variables from .env (optional, useful for production)
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///superheroes.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
