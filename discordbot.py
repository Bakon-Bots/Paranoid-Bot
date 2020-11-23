import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='—')

user_logs = client.get_channel(757793133072482304)
  
@client.event
async def on_ready():
  on_loaded = client.get_channel(757798667607474317)
  await on_loaded.send('PyBot : Loaded.')

#@client.event
#async def on_command_error(ctx, err):
#  if isinstance(err, commands.MissingRequiredArgument):
#    await ctx.send('Please pass in all required args.')
#  if isinstance(err, commands.ExtensionAlreadyLoaded):
#    await ctx.send('Cog is already loaded.')

@client.event
async def on_member_join(member):
  print(f'Member {member} joined!')

@client.event
async def on_member_remove(member):
  print(f'Member {member} left!')

@client.event
async def on_message_delete(message):
  print(f'{message.content} deleted')
  message_logs = client.get_channel(757793206384721950)
  await message_logs.send(f'"{message.content}" was deleted in {message.channel.name}.')

@client.event
async def on_user_update(before, after):
  await client.send_message(user_logs, f'Before {before} After {after}')

# Commands
@client.command(aliases=['ver', 'version'])
async def v(ctx):
  await ctx.send('1.0.0')
  
#@client.command(aliases=['ping'])
#async def p(ctx):
#  await ctx.send(f'Pong. Bot latency: {round(client.latency * 1000)}ms')
  
@client.command(aliases=['purge'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f'Purged {amount} messages.')
  
@clear.error
async def clear_err(ctx, err):
  if isinstance(err, commands.MissingRequiredArgument):
    await ctx.send('Please pass in all required args.')

@client.command()
async def kick(ctx, member : discord.Member, *, reason='No reason specified.'):
  await member.kick(reason=reason)
  await ctx.send(f'{member} was kicked. Reason: {reason}.')
  
@client.command()
async def ban(ctx, member : discord.Member, *, reason='No reason specified.'):
  await member.ban(reason=reason)
  await ctx.send(f'{member} was banned. Reason: {reason}.')
  
@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discrim = member.split('#')
  for ban_entry in banned_users:
    user = ban_entry.user
    
    if (user.name, user.discriminator) == (member_name, member_discrim):
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanned {user.mention}')
      return
  
@client.command()
async def load(ctx, extension):
  client.load_extension(f'Cogs.{extension}')
  await ctx.send(f'Loaded "{extension}"')
@load.error
async def load_error(ctx, err):
  if isinstance(err, commands.ExtensionAlreadyLoaded):
    await print('Cog is already loaded.')
  
@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'Cogs.{extension}')
  await ctx.send(f'Unloading "{extension}" will cause it\'s functions to be unavailable.')
  await ctx.send(f'"{extension}" already unloaded.')
  
@client.command()
async def reload(ctx, extension):
  client.unload_extension(f'Cogs.{extension}')
  client.load_extension(f'Cogs.{extension}')
  await ctx.send(f'Reloaded "{extension}"')  

for file_name in os.listdir('./Cogs'):
  if file_name.endswith('.py'):
    client.load_extension(f'Cogs.{file_name[:-3]}')
  
client.run('NzU3NzYzNDM0NzAyOTYyNzM4.X2lIMQ.MfsIiYPcKEKar-nMlL_n-r5I5sM')