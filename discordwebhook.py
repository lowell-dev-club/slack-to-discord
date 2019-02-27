# Imports
from log import logger
from config import WEBHOOK_ID, WEBHOOK_TOKEN
from discord import Webhook, RequestsWebhookAdapter

def discordwebhook(message):
    webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())
    logger.debug('create discord webhook data')

    webhook.send(message)
    logger.debug('send announcement through discord webhook')
