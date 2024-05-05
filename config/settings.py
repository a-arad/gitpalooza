import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPEN_ISSUES_CHANNEL_ID = int(os.getenv("OPEN_ISSUES_CHANNEL_ID"))
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
