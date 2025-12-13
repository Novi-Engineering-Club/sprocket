import discord
from discord.ext import commands
import os  # default module
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
load_dotenv()  # load all the variables from the env file
bot = commands.Bot(command_prefix="s,", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")


@bot.slash_command(name="contact", description="Contact Novi Engineering Club")
async def contact(ctx: discord.ApplicationContext):
    await ctx.respond("Insta: @noviengineeringig \n Email: noviengineeringig@gmail.com")


# Load cogs
cogs_list = ["fun", "admin"]

for cog in cogs_list:
    bot.load_extension(f"cogs.{cog}")

bot.run(os.getenv("DISCORD_TOKEN"))
