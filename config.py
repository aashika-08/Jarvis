import os
from dotenv import load_dotenv

# Load environment variable from .env file
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")