import os
from dhooks import Webhook, Embed, File

image2_path = 'cs-bp1-nova-obavestenja.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN1')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[BP main page link - click here -](https://cs.elfak.ni.ac.rs/nastava/course/view.php?id=4)**",
        color=0x3498DB
    )

    embed.set_image(url="attachment://cs-bp1-nova-obavestenja.png")
    file = File(image2_path, name="cs-bp1-nova-obavestenja.png")
    hook.send("@everyone 📢 BP", embed=embed, file=file)
