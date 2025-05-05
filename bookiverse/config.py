import os
from dotenv import load_dotenv
load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_URL = os.getenv("DB_URL")
DB_USER = os.getenv("DB_USER")
DB_PWD = os.getenv("DB_PWD")
DB_PORT = os.getenv("DB_PORT")

# DB_NAME="bookiverse"
# DB_URL="localhost"
# DB_USER="root"
# DB_PWD="kashif"
# DB_PORT=3306