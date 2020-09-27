import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='--', owner_id=372496578499575828)

#TODO: SET ALL MESSAGES TO EMBEDS.
# ! CREATE AN UPDATE COMMAND THAT SIMPLY RETURNS 'UPDATING BOT...' WAIT(RANDOM NUM > 5 BUT < 20) SEND 'BOT UPDATED.'

@client.event
async def on_ready():
  print('PyBot loaded!')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['TOKEN'])