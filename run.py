# Imports
import re
from log import logger
from json import dumps
from config import announce_code, SLACK, WEBHOOK_ID, WEBHOOK_TOKEN
from discord import Webhook, RequestsWebhookAdapter
from slackbot.bot import Bot, respond_to, listen_to, default_reply
from slackwebhook import slackwebhook

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
        slackwebhook(announcement)

        # Discord
        webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())
        logger.debug('create discord webhook data')
        webhook.send(announcement)
        logger.debug('send announcement through discord webhook')

    else:
        my_default_handler(message)

# Main function
def main():
    print('----------------------------')
    print(' Lowell Dev CLub Bot Online')
    print('----------------------------')
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    main()
