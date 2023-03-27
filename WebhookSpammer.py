from discord_webhook import DiscordWebhook

webhook = input("wehook url : ")
text = input("text : ")

while(True):
    webhook = DiscordWebhook(url=webhook, rate_limit_retry=True, content=text)
    response = webhook.execute()