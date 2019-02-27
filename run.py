# Imports
import re
import logging
from sys import stdout
from json import dumps
from requests import post
from config import announce_code, SLACK, WEBHOOK_ID, WEBHOOK_TOKEN
from discord import Webhook, RequestsWebhookAdapter
from slackbot.bot import Bot, respond_to, listen_to, default_reply

# logging config
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler(stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

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
        slack_data = {
                     'text': str(announcement),
                     'username': 'Dev Club',
                     'icon_emoji': ':dev-club:'
                     }
        logger.debug('create slack data')

        response = post(SLACK,
                        data=dumps(slack_data),
                        headers={'Content-Type': 'application/json'}
                        )
        logger.debug('send slack data through slack webhook')

        # Discord
        webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())
        logger.debug('create discord webhook data')
        webhook.send(announcement)
        logger.debug('send announcement through discord webhook')

# Main function
def main():
    print('----------------------------')
    print(' Lowell Dev CLub Bot Online')
    print('----------------------------')
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    main()
