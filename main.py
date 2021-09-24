import discord
from records import passkey
from keywords import *

client = discord.Client()

@client.event
async def on_ready():
    print(client.user,' up and Running...')

@client.event
async def on_message(message):
   
    if message.author == client.user:
        return
    if message.content.lower() in greeting:
        await message.channel.send(send_greeting(message.content.lower()))

    if message.content.startswith('Howdy'):
        await message.channel.send('Wassup  !')


client.run(passkey())

