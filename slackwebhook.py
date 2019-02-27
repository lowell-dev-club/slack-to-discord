# Imports
from log import logger
from json import dumps
from requests import post

def slackwebhook(message, SLACK):

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
