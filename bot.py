import discord
import logging
import sys
from discord.ext import commands
from cogs import music, error, meta, tips
import config


bot = commands.Bot(command_prefix=cfg["prefix"])


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")


COGS = [music.Music, error.CommandErrorHandler, meta.Meta, tips.Tips]


def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot))  # Initialize the cog and add it to the bot


def run():
    add_cogs(bot)
    bot.run(config.BOT_USER_TOKEN)
