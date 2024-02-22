from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1210308309102501989/i-gYUMErI0VHVi5jlV2fMczwGkawiuV2CKG9hr3obUC-m4MFPUlGesQlqvBELxdb-ITZ", content="First msg")
response = webhook.execute()
