# bot.py
import logging
import discord
from discord.ext import commands
from config import BOT_TOKEN
from tasks.gh_integration import fetch_github_issues

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)d:%(funcName)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    handlers=[
                        logging.FileHandler('githootza.log'),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger('discord')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

bot = commands.Bot(command_prefix="?",intents=intents)

@bot.event
async def on_ready():
    logger.info(f'logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="commands"))

@bot.command()
async def get_issues(ctx, repo_owner: str, repo_name: str):

    issues = fetch_github_issues(repo_owner, repo_name)

    for issue in issues:
        await ctx.send(f"Issue {issue['number']}: {issue['title']}")

async def start_bot():
    await bot.start(BOT_TOKEN)

