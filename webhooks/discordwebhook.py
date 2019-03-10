# Imports
from discord import Webhook, RequestsWebhookAdapter


def discordwebhook(message, WEBHOOK_ID, WEBHOOK_TOKEN, logger):

    webhook = Webhook.partial(WEBHOOK_ID,
                              WEBHOOK_TOKEN,
                              adapter=RequestsWebhookAdapter())

    logger.debug('create discord webhook data')

    webhook.send(message)
    logger.info('announcement sent through discord webhook')
