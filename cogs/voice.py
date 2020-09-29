import discord
from discord.ext import commands

class Voice(commands.Cog):
  def __init__(self, client):
    self.client = client

  #? Join

  #? Leave

  #? Play

  #? Pause

  #? Stop

  #? move to channel

def setup(client):
  client.add_cog(Voice(client))