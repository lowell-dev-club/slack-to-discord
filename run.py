# Imports
import re
import discord
import log
import time
import asyncio
import threading
from sys import stdout
from json import dumps
from config import announce_code, WEBHOOK_ID_ANNOUNCE, WEBHOOK_TOKEN_ANNOUNCE, SLACK_ANNOUNCMENT, DISCORD_BOT_USER_TOKEN
from discord.ext import commands
from slackbot.bot import Bot, respond_to, listen_to, default_reply
from webhooks.slackwebhook import slackwebhook
from webhooks.discordwebhook import discordwebhook

logger = log.logging_config(__name__)

# Slack bot
@default_reply
def my_default_handler(message):
    logger.info('default reply - message not understood')
    message.reply(
        'This command has not been coded. Ask a leader or check the command list')


@respond_to('announce (.*) (.*)', re.IGNORECASE)
def stats(message, announcement=None, code=None):

    if code == announce_code:
        message.reply('Announcing your announcement: ' + str(announcement))
        logger.info('announce command')

        # Slack
        slackwebhook(announcement,
                     SLACK_ANNOUNCMENT,
                     logger)
        # Discord
        discordwebhook(
            announcement,
            WEBHOOK_ID_ANNOUNCE,
            WEBHOOK_TOKEN_ANNOUNCE,
            logger)

    else:
        my_default_handler(message)


@listen_to('!info', re.IGNORECASE)
def information(message):
    true = 'true'
    attachments = [{"fallback": "Required plain-text summary of the attachment.",
                    "pretext": "Info command",
                    'color': '#59afe1',
                    "fields": [{"title": "Author",
                                "value": "Rafael Cenzano",
                                "short": true},
                               {"title": "Help",
                                "value": "!help to get command list",
                                "short": true},
                               {"title": "Why is this a bot?",
                                "value": "I can communicate on Slack and Discord to close the gap of the two communities",
                                "short": true}]}]
    message.send_webapi('', dumps(attachments))
    logger.info('Slack info command')

@listen_to('!ping', re.IGNORECASE)
def ping_test(message):
    pingtime = time.time()
    message.send('Pinging...')
    ping = time.time() - pingtime
    message.send(f'Pong, {ping} seconds')
    logger.info(f'Ping command - ping at : {ping}')


# Main functions
def slack_run():
    logger.info('----------------------------------')
    logger.info(' Lowell Dev CLub Slack Bot Online')
    logger.info('----------------------------------')
    slackbot = Bot()
    slackbot.run()


bot = commands.Bot(command_prefix='!', description='Dev Club bot for music')


@bot.event
async def on_ready():
    logger.info('------------------------------------')
    logger.info(' Lowell Dev CLub Discord Bot Online')
    logger.info('------------------------------------')
    # await bot.change_presence(game=discord.Game(name="Use !que <song>"))
    # await bot.join_voice_channel(549804955305902110)

@bot.command(pass_context=True, description='hello command')
async def hello(ctx):
    await ctx.send('Hello')

@bot.command(pass_context=True, description='bot info')
async def info(ctx):
    embed = discord.Embed(title="Info Command", description="info command", color=0x59afe1)
    embed.add_field(name="Author", value="Rafael Cenzano", inline=False)
    embed.add_field(name="Help", value="!help to get command list", inline=False)
    embed.add_field(name="Why is this a bot?", value="I can communicate on Slack and Discord to close the gap of the two communities", inline=False)
    await ctx.send(embed=embed)


@bot.command(pass_context=True, description='check bot ping')
async def ping(ctx):
    pingtime = time.time()
    e = discord.Embed(title="Pinging...", colour=0x59afe1)
    await ctx.send(embed=e)
    ping = time.time() - pingtime
    complete = f"Pong, {ping} seconds"
    em = discord.Embed(title=complete, colour=0x59afe1)
    await ctx.send(embed=em)


@bot.command(pass_context=True, description='que songs')
async def que(ctx):
    pass


@bot.command(pass_context=True, description='play que')
async def play(ctx):
    #vc = ctx.message.author.voice.voice_channel
    # print(vc)
    # vc = await ctx.join_voice_channel('554249697515274244')
    # await bot.join_voice_channel('554249697515274244')
    #channel = discord.utils.get(
    #    ctx.message.server.channels,
    #    type=ChannelType.voice)
    voice = await ctx.join_voice_channel('554249697515274244')
    player = vc.create_ffmpeg_player('song.mp3', after=lambda: print('done'))
    player.start()
    while not player.is_done():
        await asyncio.sleep(1)
    # disconnect after the player has finished
    player.stop()
    await vc.disconnect()


if __name__ == '__main__':
    slack_run()
    #bot.run(DISCORD_BOT_USER_TOKEN)
