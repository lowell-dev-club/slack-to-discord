# Imports
from log import logger
from discord import Webhook, RequestsWebhookAdapter

def discordwebhook(message, WEBHOOK_ID, WEBHOOK_TOKEN):
    webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())
    logger.debug('create discord webhook data')

    webhook.send(message)
    logger.debug('send announcement through discord webhook')
