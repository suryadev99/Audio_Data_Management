import os

MONGO_HOST = os.environ.get("MONGO_HOST", None)
MONGO_PORT = os.environ.get("MONGO_PORT", None)
MONGO_DB = os.environ.get("MONGO_DB", None)
MONGO_USER = os.environ.get("MONGO_USER", None)
MONGO_PASS = os.environ.get("MONGO_PASS", None)
DB_URI = os.environ.get("DB_URI", None)
