# Imports
import logging
from discord import Webhook, RequestsWebhookAdapter


def discordwebhook(message, WEBHOOK_ID, WEBHOOK_TOKEN):
    webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())
    logging.debug('create discord webhook data')

    webhook.send(message)
    logging.debug('send announcement through discord webhook')
