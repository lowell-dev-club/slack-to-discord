# Imports
import re
from log import logger
from config import announce_code, WEBHOOK_ID_ANNOUNCE, WEBHOOK_TOKEN_ANNOUNCE, SLACK_ANNOUNCMENT
from slackbot.bot import Bot, respond_to, listen_to, default_reply
from slackwebhook import slackwebhook
from discordwebhook import discordwebhook

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
        slackwebhook(announcement, SLACK_ANNOUNCMENT)
        # Discord
        discordwebhook(announcement, WEBHOOK_ID_ANNOUNCE, WEBHOOK_TOKEN_ANNOUNCE)

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
