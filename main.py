import discord
from records import passkey

client = discord.Client()

@client.event
async def on_ready():
    print(client.user,' up and Running...')

@client.event
async def on_message(message):
   
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Wassup  !')


client.run(passkey())

