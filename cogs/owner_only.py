import discord
from discord.ext import commands

class Owner_Only(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['c'])
  async def close(self, ctx):
    if ctx.author.id == 372496578499575828:
      close_em = discord.Embed(title='Closing Connection.', description='WARNING: Closing the bot will shut it down in all servers. Shutting down.', color=0xfc0303)
      close_em.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
      await ctx.send(embed=close_em)
      await self.client.close()
    else: await ctx.send('You dont have permissions to use that command.')

def setup(client):
  client.add_cog(Owner_Only(client))