import discord
from discord.ext import commands

class General(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['ver', 'version'])
  async def v(self, ctx):
    await ctx.send('Okay the version is 1.0.0')

  @commands.command(aliases=['ping'])
  async def p(self, ctx):
    await ctx.send(f'Pong. Bot latency: {round(self.client.latency * 1000)}ms')

  @commands.command(aliases=['type', 'typeof'])
  async def tof(self, ctx):
    if ctx == 'p' or ctx == 'ping':
      await ctx.send('Function: ping() --returns bots latency.')
      print('yes')
    elif ctx == 'v' or ctx == 'ver' or ctx == 'version': await ctx.send('Function: version() --returns bots version.')
    elif ctx == 'mdy' or ctx == 'mondayyear' or ctx == 'monthdayyearnow': await ctx.send('Function: monthdayyear() --returns the current month day, year')
    elif ctx == 't' or ctx == 'time' or ctx == 'timenow': await ctx.send('Function: time() --returns the current time in Hour:Min:Sec')
    elif ctx == 'kick': await ctx.send('Function: kick(user, reason) --kicks specified user.')
    elif ctx == 'ban': await ctx.send('Function: ban(user, reason) --bans specified user.')
    elif ctx == 'unban': await ctx.send('Function: unban(user) --unbans specified user.')
  
def setup(client):
  client.add_cog(General(client))