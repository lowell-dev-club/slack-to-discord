# Imports
from slackbot.bot import Bot, respond_to, listen_to, default_reply
import re
import logging
import sys

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

@respond_to('hi', re.IGNORECASE)
def hi(message):
    logger.info('Hi command')
    message.reply('Hello there!')

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
