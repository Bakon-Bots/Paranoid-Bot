import discord
from discord.ext import commands

class Moderation(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def kick(self, ctx, member:discord.Member, *, reason):
    await ctx.send('Not set up yet.')

  @commands.command()
  async def ban(self, ctx, member: discord.Member, *, reason):
    await ctx.send('Not set up yet.')

  @commands.command()
  async def unban(self, ctx, *, member):
    await ctx.send('Not set up yet.')

def setup(client):
  client.add_cog(Moderation(client))