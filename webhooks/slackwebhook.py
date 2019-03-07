# Imports
import asyncio
import aiohttp
import logging
from json import dumps

async def slackwebhook(message, SLACK):

    slack_data = {
                 'text': str(message),
                 'username': 'Dev Club',
                 'icon_emoji': ':dev-club:'
                 }
    logging.debug('create slack data')

    async with aiohttp.ClientSession() as session:
        async with session.post(SLACK, data=dumps(slack_data), headers={'Content-Type': 'application/json'}) as resp:
            logging.info(await resp.text())

    logging.debug('send slack data through slack webhook')
