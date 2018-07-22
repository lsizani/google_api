from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=str(env_path))


class Settings:
    def __init__(self):
        pass

    @classmethod
    def get_api_key(cls):
        return os.getenv('GOOGLE_API_KEY')

    @classmethod
    def get_api_url(cls):
        return os.getenv('GOOGLE_API_URL')
