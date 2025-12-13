import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def purge_logic(self, channel: discord.TextChannel, amount: int):
        await channel.purge(limit=amount + 1)

    @discord.slash_command(name="purge", description="Delete a number of messages")
    @commands.has_permissions(manage_messages=True)
    async def purge_slash(self, ctx: discord.ApplicationContext, amount: int):
        await self.purge_logic(ctx.channel, amount)
        await ctx.respond(f"🧹 Deleted {amount} messages.", ephemeral=True)


def setup(bot):
    bot.add_cog(Admin(bot))
