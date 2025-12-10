import discord
import random
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def flip_logic(self):
        result = ["Heads", "Tails"]
        return random.choice(result)

    @commands.command(name="flip")
    async def flip_prefix(self, ctx):
        result = await self.flip_logic()
        await ctx.send(result)

    @discord.slash_command(name="flip")
    async def flip_slash(self, ctx):
        result = await self.flip_logic()
        await ctx.respond(result)


def setup(bot):
    bot.add_cog(Fun(bot))
