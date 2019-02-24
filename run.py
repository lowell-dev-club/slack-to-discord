# Imports
from slackbot.bot import Bot, respond_to, listen_to, default_reply
import re
import logging

logging.getLogger().addHandler(logging.StreamHandler())

@default_reply
def my_default_handler(message):
    message.reply('This command has not been coded. Ask a leader or check the command list')

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')

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
