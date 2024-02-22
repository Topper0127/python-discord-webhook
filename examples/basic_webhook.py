from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="your url", content="First msg")
response = webhook.execute()
