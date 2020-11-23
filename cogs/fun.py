import discord
from discord.ext import commands
import requests as rq


class Fun(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(description='Returns current ISS position.', brief='Current location of the ISS')
  async def iss(self, ctx):
    response = rq.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status
    data = response.json()
    longi = data['iss_position']['longitude']
    lat = data['iss_position']['latitude']

    await ctx.send(f'ISS current latitude is {lat} and longitude is {longi}')


def setup(client):
  client.add_cog(Fun(client))
