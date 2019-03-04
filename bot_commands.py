# Imports
import random

"""
File for command code
"""
def tip():
    """Get a random tip about using the bot."""
    tips = ["Only admins and the song requester can immediately skip songs. Everybody else will have to vote!",
           f"You can check out my source code here: https://github.com/lowell-dev-club/slack-to-discord"]
    index = random.randrange(len(tips))
    return (f"**Tip #{index+1}:** {tips[index]})

def 
