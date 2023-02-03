from discord_webhook import DiscordWebhook, DiscordEmbed
import os

webhook_id = "1070949976269656104"
webhook_token = "BjQ2Vh9rjwJR9XoM3nit51Vr3VJqjpS2E3Whrr5ZLGyYZrUYXDKwMx5VUiUN9-eiC5dA"


def createWebHook(fileURL):
    directory = os.fsencode("images")

    webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}")    

    embed = DiscordEmbed(title='Notice!',description='@everyone', color='0x992d22', url=fileURL)
    embeds = [embed]

    i=0
    for file in os.listdir(directory):
        embeds.append(DiscordEmbed(url=fileURL))
        filename = os.fsdecode(file)
        with open(f"images/{filename}", "rb") as f:
            print(filename)
            webhook.add_file(file=f.read(), filename=f'{filename}')
        embeds[i].set_image(url=f'attachment://{filename}')
        webhook.add_embed(embeds[i])
        if i==2:
            break
        i+=1

    response = webhook.execute(remove_files=True)
    return response



