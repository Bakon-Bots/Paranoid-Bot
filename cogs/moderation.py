import discord
from discord.ext import commands

#TODO: SET ALL MESSAGES TO EMBEDS.

class Moderation(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(description='Kicks a user. Must have Kick memebers permission.')
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member:discord.Member, *, reason):
    await ctx.send('Not set up yet.')

  @commands.command(description='Bans a user. Must have Ban members permission')
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member:discord.Member, *, reason):
    await ctx.send('Not set up yet.')

  @commands.command(description='Unbans a user. Must have Ban members permission')
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
    await ctx.send('Not set up yet.')

  @commands.command(description='Clears a set of messages. Must have manage messages permission')
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx,amount: int):
    await ctx.send('Clear')

def setup(client):
  client.add_cog(Moderation(client))