# Imports
from slackclient import SlackClient
from config import BOT_USER_TOKEN

# Create Slack Client object
slack_client = SlackClient(BOT_USER_TOKEN)

# Check if connection was succesful
bool = slack_client.rtm_connect(with_team_state=False)

if __name__ == '__main__' and bool == True:
    pass
