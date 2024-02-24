from discord_webhook import DiscordEmbed, DiscordWebhook

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1210308309102501989/i-gYUMErI0VHVi5jlV2fMczwGkawiuV2CKG9hr3obUC-m4MFPUlGesQlqvBELxdb-ITZ")

# create embed object for webhook
embed = DiscordEmbed(
    title="Oh , My hero Liberpool", description="You can got your tickets", color=242424
)



# set author
embed.set_author(name="Author Name", url="author url", icon_url="author icon url")

# set image
embed.set_image(url="your image url")

# set thumbnail
embed.set_thumbnail(url="your thumbnail url")

# set footer
embed.set_footer(text="Enjoy yourself")

# set timestamp (default is now)
embed.set_timestamp()

# add fields to embed
embed.add_embed_field(name="Field 1", value="Lorem ipsum")
embed.add_embed_field(name="Field 2", value="dolor sit")

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()
