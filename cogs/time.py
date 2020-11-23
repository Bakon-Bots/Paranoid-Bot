import discord
from discord.ext import commands
from datetime import datetime

#TODO: SET ALL MESSAGES TO EMBEDS.

class Time(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['mondayyear', 'monthdayyearnow'], description='Gets the current time in Month Day, Year form.', brief='Current Month:Day:Year')
  async def mdy(self, ctx): # ? Month day, year format
    await ctx.send('yes '+datetime.strftime(datetime.now(), '%b %d, %Y'))
    
  @commands.command(aliases=['time', 'timenow'], description='Gets the current time in Hour:Minute:Second form.', brief='Current Time in Hour:Minute:Second')
  async def t(self, ctx): # ? Hour:Minute:Second format
    await ctx.send(datetime.strftime(datetime.now(), '%I:%M:%S'))

def setup(client):
  client.add_cog(Time(client))