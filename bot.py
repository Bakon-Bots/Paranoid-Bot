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
async def on_message_edit(before, after):
  message_embed = discord.Embed(title=f'Message edited in {before.channel.mention} sent by {before.author.mention}')
  messagelog = client.get_channel(757793206384721950)
  print(before)
  print(after)
  await messagelog.send(f'```Message sent by {before.author.mention} edited in {before.channel.mention} \nBefore: \'{before.content}\' \nAfter: \'{after.content}\'```')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))