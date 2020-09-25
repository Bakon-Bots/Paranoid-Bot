import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv('./.env')

client = commands.Bot(command_prefix=os.getenv('PREFIX'))

@client.event
async def on_ready():
  print('hello!')

@client.event
async def on_message_delete(message):
  print(message)
  message_log = client.get_channel(757793206384721950)
  await message_log.send(f'\'{message.content}\' was deleted in {message.channel}.')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))