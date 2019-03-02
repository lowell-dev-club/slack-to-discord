# Imports
import re
from log import logger
from config import announce_code, WEBHOOK_ID_ANNOUNCE, WEBHOOK_TOKEN_ANNOUNCE, SLACK_ANNOUNCMENT
from slackbot.bot import Bot, respond_to, listen_to, default_reply
from slackwebhook import slackwebhook
from discordwebhook import discordwebhook
import discord
from discord.ext import commands
from json import dumps

# Slack bot
@default_reply
def my_default_handler(message):
    logger.info('default reply - message not understood')
    message.reply('This command has not been coded. Ask a leader or check the command list')

@respond_to('announce (.*) (.*)', re.IGNORECASE)
def stats(message, announcement=None, code=None):

    if code == announce_code:
        message.reply('Announcing your announcement: ' + str(announcement))
        logger.info('announce command')

        # Slack
        slackwebhook(announcement, SLACK_ANNOUNCMENT)
        # Discord
        discordwebhook(announcement, WEBHOOK_ID_ANNOUNCE, WEBHOOK_TOKEN_ANNOUNCE)

    else:
        my_default_handler(message)

@listen_to('!info', re.IGNORECASE)
def information(message):
    true = 'true'
    attachments = [
    {
        "fallback": "Required plain-text summary of the attachment.",
        "pretext": "Info command",
        'color': '#59afe1',
        "fields": [
                {
                    "title": "Author",
                    "value": "Rafael Cenzano",
                    "short": true
                },
                {
                    "title": "Help",
                    "value": "!help to get command list",
                    "short": true
                },
                {
                    "title": "Why is this a bot?",
                    "value": "I can communicate on Slack and Discord to close the gap of the two communities",
                    "short": true
                }
        ]
    }]
    message.send_webapi('', dumps(attachments))

# Discord bot
discordbot = commands.Bot(command_prefix='$', description='A bot that plays music.')
discordbot.remove_command('help')

@discordbot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------')

@discordbot.command()
async def info(ctx):
    embed = discord.Embed(title="Dev Club", 
                          description="Lowell Dev Club bot.", 
                          color=0x59afe1)

    # give info about you here
    embed.add_field(name="Author", 
                    value="Enchanter77#0730")

    # give command help
    embed.add_field(name="Help", 
                    value="!help to get command list")

    # give description
    embed.add_field(name="Why is this a bot?",
                    value="I can communicate on Slack and Discord to close the gap of the two communities")

    await ctx.send(embed=embed)

@discordbot.command()
async def help(ctx):
    embed = discord.Embed(title="Dev Club", 
                          description="Lowell Dev Club bot", 
                          color=0xeee657)

    embed.add_field(name="!info", 
                    value="Gives a little info about the bot", 
                    inline=False)

    embed.add_field(name="!help", 
                    value="Gives this message", 
                    inline=False)

    await ctx.send(embed=embed)

# Main function
def main():
    print('----------------------------')
    print(' Lowell Dev CLub Bot Online')
    print('----------------------------')
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    main()
