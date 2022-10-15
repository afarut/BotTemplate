import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent

BOT_TOKEN = os.environ["TOKEN"]
ADMIN = os.environ["ADMIN"]

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}