import discord
import requests
import json


def get_memes():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']


class MyClient(discord.Client):  # classe para interagir com a api do discord.
    async def on_ready(self):  # on_ready()função quando logar.
        print('Logged on {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            await message.channel.send(get_memes())


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTM1MDE2ODczMTI0NjEzNzM1NA.GtiNUX.'
           'VcZOQ8xeTDsmnLWe8o0TXBiVNdRrMJRFQ7vDaE')
