import discord
from discord.ext import commands
from datetime import datetime

class Time(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['mondayyear', 'monthdayyearnow'])
  async def mdy(self, ctx): # Month day, year format
    await ctx.send(datetime.strftime(datetime.now(), '%b %d, %Y'))
  @commands.command(aliases=['time', 'timenow'])
  async def t(self, ctx): # Hour:Minute:Second format
    await ctx.send(datetime.strftime(datetime.now(), '%I:%M:%S'))

def setup(client):
  client.add_cog(Time(client))