# bot.py
import discord
from discord.ext import commands
from config import BOT_TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def get_issues(ctx, repo_owner: str, repo_name: str):
    from tasks.github_integration import fetch_github_issues

    issues = fetch_github_issues(repo_owner, repo_name)

    for issue in issues:
        await ctx.send(f"Issue {issue['number']}: {issue['title']}")


bot.run(BOT_TOKEN)
