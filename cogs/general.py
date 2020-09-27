import discord
from discord.ext import commands

class General(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['ver', 'version'])
  async def v(self, ctx):
    await ctx.send('Bot version: 1.0.5')

  @commands.command(aliases=['ping'])
  async def p(self, ctx):
    await ctx.send(f'Pong. Bot latency: {round(self.client.latency * 1000)}ms')

  @commands.command(aliases=['type', 'typeof'])
  async def tof(self, ctx, *, arg):
    if arg == 'p' or arg == 'ping': await ctx.send('Function: ping() --returns bots latency.')
    elif arg == 'v' or arg == 'ver' or arg == 'version': await ctx.send('Function: version() --returns bots version.')
    elif arg == 'mdy' or arg == 'mondayyear' or ctx == 'monthdayyearnow': await ctx.send('Function: monthdayyear() --returns the current month day, year')
    elif arg == 't' or arg == 'time' or arg == 'timenow': await ctx.send('Function: time() --returns the current time in Hour:Min:Sec')
    elif arg == 'kick': await ctx.send('Function: kick(user, reason) --kicks specified user.')
    elif arg == 'ban': await ctx.send('Function: ban(user, reason) --bans specified user.')
    elif arg == 'unban': await ctx.send('Function: unban(user) --unbans specified user.')
  
def setup(client):
  client.add_cog(General(client))