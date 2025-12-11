import discord
import random
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def flip_logic(self):
        result = ["Heads", "Tails"]
        return random.choice(result)

    async def roll_logic(self, max_value: int = 6) -> int:
        return random.randint(1, max_value)

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


def setup(bot):
    bot.add_cog(Fun(bot))
