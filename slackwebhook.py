# Imports
from requests import post
from log import logger
from config import SLACK

def slackwebhook(message):

    slack_data = {
                 'text': str(message),
                 'username': 'Dev Club',
                 'icon_emoji': ':dev-club:'
                 }
    logger.debug('create slack data')

    response = post(SLACK,
                    data=dumps(slack_data),
                    headers={'Content-Type': 'application/json'}
                    )
    logger.debug('send slack data through slack webhook')
