# Work with Python 3.6
import discord

TOKEN = 'NzQ0MzkyMDE2OTA5MzAzODU5.XzijFg.a3VUXQfapP8HezDsDPNr_i84fBo'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    print(message.author)

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        channel = message.channel
        await channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)