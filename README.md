# PyBot

Currently in development. Expect many many bugs to appear.

# Commands


# Code
```Python
import discord, time
from discord.ext import commands
import datetime

#TODO: SET ALL MESSAGES TO EMBEDS.

start_time = time.time()

class General(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['ver', 'version'], description='Bots current version')
  async def v(self, ctx):
    await ctx.send('Bot version: 1.0.20')

  @commands.command(aliases=['ping'], description='Bots current ping')
  async def p(self, ctx):
    await ctx.send(f'Pong. Bot latency: {round(self.client.latency * 1000)}ms')

  #@commands.command(aliases=['uptm', 'uptime'])
  #async def ut(self, ctx):
  #  await ctx.send(f'Bot uptime: {self.client.uptime}')

  @commands.command(aliases=['uptm', 'uptime'], description='Bots uptime.')
  async def ut(self, ctx):
      current_time = time.time()
      difference = int(round(current_time - start_time))
      text = str(datetime.timedelta(seconds=difference))
      embed = discord.Embed(color=0x00fbff)
      embed.add_field(name="Uptime", value=text)
      try:
          await ctx.send(embed=embed)
      except discord.HTTPException:
          await ctx.send("Current uptime: " + text)
  
def setup(client):
  client.add_cog(General(client))
```
