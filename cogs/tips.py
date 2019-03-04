from discord.ext import commands
import discord
import random


class Tips:
    """Commands for providing tips about using the bot."""

    def __init__(self, bot):
        self.bot = bot
        self.tips = ["Only admins and the song requester can immediately skip songs. Everybody else will have to vote!",
                     f"You can check out my source code here: https://github.com/lowell-dev-club/slack-to-discord"]

    @commands.command()
    async def tip(self, ctx):
        """Get a random tip about using the bot."""
        index = random.randrange(len(self.tips))
        await ctx.send(f"**Tip #{index+1}:** {self.tips[index]}")
