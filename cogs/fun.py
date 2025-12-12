import discord
import random
from discord.ext import commands
import requests

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def flip_logic(self):
        result = ["Heads", "Tails"]
        return random.choice(result)

    async def roll_logic(self, max_value: int = 6) -> int:
        return random.randint(1, max_value)
    

    async def get_quote(self):
        response = requests.get('https://zenquotes.io/api/quotes/')
        data = response.json()
        return data[0]["q"]

    @commands.command(name="roll")
    async def roll_prefix(self, ctx, max_value: int = 6):
        result = await self.roll_logic(max_value)
        await ctx.send(f"You rolled a **{result}**")

    @discord.slash_command(name="roll")
    async def roll_slash(self, ctx: discord.ApplicationContext, max_value: int = 6):
        result = await self.roll_logic(max_value)
        await ctx.respond(f"You rolled a **{result}**")

    @commands.command(name="flip")
    async def flip_prefix(self, ctx):
        result = await self.flip_logic()
        await ctx.send(result)

    @discord.slash_command(name="flip")
    async def flip_slash(self, ctx):
        result = await self.flip_logic()
        await ctx.respond(result)
    
    @commands.command(name="quote")
    async def get_quote_prefix(self, ctx):
        quote = await self.get_quote()
        await ctx.send(quote)

    @discord.slash_command(name="quote")
    async def get_quote_slash(self, ctx):
        quote = await self.get_quote()
        await ctx.respond(quote)
    


def setup(bot):
    bot.add_cog(Fun(bot))
