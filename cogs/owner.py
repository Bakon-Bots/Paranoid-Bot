import discord
from discord.ext import commands
from cogs.moderation import ban_dict
import asyncio

#TODO: SET ALL MESSAGES TO EMBEDS.
namelist = {}

class Owner(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command(description='Only for bot owner.', brief='Only the bot owner can use this.')
  async def c(self, ctx):

    def check(ms):
      return ms.channel == ctx.message.channel and ms.author == ctx.message.author

    if ctx.author.id == 372496578499575828:
      await ctx.send('```Are you sure you want to close the Connection?```')
      msg = await self.client.wait_for('message', check=check)
      
      if msg.content == 'yes' or msg.content == 'Yes':
        close_em = discord.Embed(title='Closing Connection.', description='WARNING: Closing the bot will shut it down in all servers. Shutting down.', color=0xfc0303)
        close_em.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=close_em)
        await self.client.close()

      else:
        await ctx.send('```Returning.```')
        return

    else: await ctx.send('```You dont have permissions to use that command.```')

  @commands.command(description='Creates a list, set, or tuple.', brief='Owner only.')
  async def setf(self, ctx, type, name, *args):
    global namelist
    def check(ms):
      return ms.channel == ctx.message.channel and ms.author == ctx.message.author

    if ctx.author.id == 372496578499575828:
      if type == 'list':
        await ctx.send(f'```Created new list! Use -getf {name} to get contents of {name}.```')
        namelist[name] = list(args)
      elif type == 'set':
        await ctx.send(f'```Created new Set! Use -getf {name} to get contents of {name}.```')
        namelist[name] = set(args)
      elif type == 'tuple':
        await ctx.send(f'```Created new tuple! Use -getf {name} to get contents of {name}.```')
        namelist[name] = tuple(args)
      else:
        await ctx.send(f'```Not a vaild type. [list, set] is supported.```')
    else: await ctx.send('Attempt to use owner only command.')

  @commands.command(description='Returns a list, set, or tuple.', brief='Gets a list, set, or tuple!')
  async def getf(self, ctx, name):
    global namelist
    if name not in namelist:
      await ctx.send(f'```Couldn\'t find a list or set with the name {name}.```')
    else:
      await ctx.send(f'```Here you go! {namelist[name]}.```')

  @commands.command(description='Starts a for loop and sends the contents to the channel', brief='Owner only.')
  async def startfor(self, ctx, *args):
    def check(ms):
      return ms.channel == ctx.message.channel and ms.author == ctx.message.author

    if ctx.author.id == 372496578499575828:
      li = []
      for arg in args:
        li.append(arg)
      for ran in li:
        await asyncio.sleep(1)
        await ctx.send(f'Uhhhhh... {ran}')
    else: await ctx.send('```Attempt to use owner only command.```')

def setup(client):
  client.add_cog(Owner(client))