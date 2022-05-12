import discord
import json
from calendario import Calendario 

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    classes = Calendario().main()
    if message.content.startswith('$aula'):
        await message.channel.send(f'Próxima aula: {classes[0]}\nVocê quer as próximas datas? Digite "$datas".')
    if message.content.startswith('$datas'):
        await message.channel.send(f'{classes[1]}\n{classes[2]}\n{classes[3]}\n')
   
   
with open('discord_token.json', 'r') as token_json:
    TOKEN = json.load(token_json)
client.run(TOKEN)
