# Imports
import re
import discord
import logging
import threading
from sys import stdout
from json import dumps
from config import announce_code, WEBHOOK_ID_ANNOUNCE, WEBHOOK_TOKEN_ANNOUNCE, SLACK_ANNOUNCMENT, BOT_USER_TOKEN
from discord.ext import commands
from slackbot.bot import Bot, respond_to, listen_to, default_reply
from webhooks.slackwebhook import slackwebhook
from webhooks.discordwebhook import discordwebhook

# logging config
logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler(stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

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
        slackwebhook(announcement, SLACK_ANNOUNCMENT)
        # Discord
        discordwebhook(
            announcement,
            WEBHOOK_ID_ANNOUNCE,
            WEBHOOK_TOKEN_ANNOUNCE)

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


# Main functions
def slack_run():
    print('aa')
    logger.info('----------------------------------')
    logger.info(' Lowell Dev CLub Slack Bot Online')
    logger.info('----------------------------------')
    slackbot = Bot()
    slackbot.run()


if __name__ == '__main__':
    slack_run()
