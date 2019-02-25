# Imports
from slackbot.bot import Bot, respond_to, listen_to, default_reply
import re
import logging
import sys
from requests import post
from json import dumps
import config

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
    message.reply('Announcing your announcement')
    logger.info('announce command')

    slack_data = {
                 'text': '',
                 'username': 'Dev Club',
                 'icon_emoji': ':dev-club:'
                 }

    response = post(config.SLACK,
                    data=dumps(slack_data),
                    headers={'Content-Type': 'application/json'}
                    )

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
