# Imports
import requests
from json import dumps

def slackwebhook(message, SLACK):

    slack_data = {
                 'text': str(message),
                 'username': 'Dev Club',
                 'icon_emoji': ':dev-club:'
                 }

    response = post(config.SLACK,
                    data=dumps(slack_data),
                    headers={'Content-Type': 'application/json'}
                    )

