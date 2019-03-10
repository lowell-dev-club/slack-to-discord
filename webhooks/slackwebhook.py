# Imports
from requests import post
from json import dumps


def slackwebhook(message, SLACK, logger):

    slack_data = {
        'text': str(message),
        'username': 'Dev Club',
        'icon_emoji': ':dev-club:'
    }
    logger.debug('created slack data')

    response = post(SLACK,
                    data=dumps(slack_data),
                    headers={'Content-Type': 'application/json'}
                    )
    logger.info('announcement sent on slack webhook')
