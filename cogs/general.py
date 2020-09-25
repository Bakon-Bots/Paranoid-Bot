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
  
def setup(client):
  client.add_cog(General(client))