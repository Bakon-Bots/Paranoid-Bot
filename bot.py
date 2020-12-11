import discord
from discord.ext import commands
import os


Paranoid = commands.Bot(
  command_prefix=commands.when_mentioned_or('--'),
  owner_id=372496578499575828,
  description='Main Paranoid Alpha Bot',
  case_insensitive=True,
)

# TODO: SET ALL MESSAGES TO EMBEDS.
# TODO: ERROR MESSAGES!
# TODO: ADD MORE LOGGING


@Paranoid.event
async def on_ready():
  print('Paranoid loaded!')


@Paranoid.command(brief='Loads a certain module.')
async def load(ctx, extension):
  Paranoid.load_extension(f'Cogs.{extension}')
  await ctx.send(f'Loaded "{extension}"')
@load.error
async def load_error(ctx, err):
  if isinstance(err, commands.ExtensionAlreadyLoaded):
    await print('Cog is already loaded.')
  

@Paranoid.command(brief='Unloads a certain module')
async def unload(ctx, extension):
  Paranoid.unload_extension(f'Cogs.{extension}')
  await ctx.send(f'Unloading "{extension}" will cause it\'s functions to be unavailable.')
  await ctx.send(f'"{extension}" already unloaded.')
  

@Paranoid.command(brief='Reloads a certain module')
async def reload(ctx, extension):
  Paranoid.unload_extension(f'Cogs.{extension}')
  Paranoid.load_extension(f'Cogs.{extension}')
  await ctx.send(f'Reloaded "{extension}"')  


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    Paranoid.load_extension(f'cogs.{filename[:-3]}')


Paranoid.run(os.environ["TOKEN"])