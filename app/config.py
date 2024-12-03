# app/config.py

import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://<username>:<password>@<hostname>:<port>/<database_name>")
    SECRET_KEY = os.getenv("SECRET_KEY", "YOUR_SECRET_KEY_HERE")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()