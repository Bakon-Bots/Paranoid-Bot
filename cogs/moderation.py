import discord
from discord.ext import commands

class Moderation(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member:discord.Member, *, reason):
    await ctx.send('Not set up yet.')

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member:discord.Member, *, reason):
    await ctx.send('Not set up yet.')

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
    await ctx.send('Not set up yet.')

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx,amount: int):
    await ctx.send('Clear')

def setup(client):
  client.add_cog(Moderation(client))