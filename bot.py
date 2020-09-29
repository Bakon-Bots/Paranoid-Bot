import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=commands.when_mentioned_or('--'), owner_id=372496578499575828)

#TODO: SET ALL MESSAGES TO EMBEDS.
#TODO: ERROR MESSAGES!
#TODO: REMOVE LICENSE AND CODE_OF_CONDUCT.md
#TODO: ADD LOAD, UNLOAD, RELOAD COMMAND FOR COGS REFER TO DISCORDBOT.PY
#TODO: ADD MORE LOGGING
#TODO: USE BRIEF TO ADD A BRIEF MESSAGE NEXT TO THE COMMAND WHEN USER DOES !HELP

@client.event
async def on_ready():
  print('PyBot loaded!')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['TOKEN'])