import os
from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.environ.get("DB_NAME")
DB_URL = os.environ.get("DB_URL")
DB_USER = os.environ.get("DB_USER")
DB_PWD = os.environ.get("DB_PWD")
DB_PORT = os.environ.get("DB_PORT")

# DB_NAME="hr2"
# DB_URL="localhost"
# DB_USER="root"
# DB_PWD="kashif"
# DB_PORT=3306