# Imports
from slackbot.bot import Bot, respond_to, listen_to, default_reply
import re
import logging
import sys
from requests import post
from json import dumps
import config
from discord import Webhook, RequestsWebhookAdapter

# logging config
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

@default_reply
def my_default_handler(message):
    logger.info('default reply - message not understood')
    message.reply('This command has not been coded. Ask a leader or check the command list')

@respond_to('announce (.*) (.*)', re.IGNORECASE)
def stats(message, announcement=None, code=None):
    if code == config.announce_code:
        message.reply('Announcing your announcement: ' + str(announcement))
        logger.info('announce command')

        # Slack
        slack_data = {
                     'text': str(announcement),
                     'username': 'Dev Club',
                     'icon_emoji': ':dev-club:'
                     }
        logger.debug('create slack data')

        response = post(config.SLACK,
                        data=dumps(slack_data),
                        headers={'Content-Type': 'application/json'}
                        )
        logger.debug('send slack data through slack webhook')

        # Discord
        webhook = Webhook.partial(config.WEBHOOK_ID, config.WEBHOOK_TOKEN,adapter=RequestsWebhookAdapter())
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

# run the bot
if __name__ == "__main__":
    main()
