# bot.py
import discord
from discord.ext import commands
from config import BOT_TOKEN

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(BOT_TOKEN)
