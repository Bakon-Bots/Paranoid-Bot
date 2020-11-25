import discord
import time
from discord.ext import commands
import datetime

# TODO: SET ALL MESSAGES TO EMBEDS.

start_time = time.time()
#say = discord.get_channel(760617208489050164)

class General(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['ver', 'version'], description='clients current version', brief='clients version')
  async def v(self, ctx):
    ver = discord.Embed(description='Version: 0.0.12', color=0x000)
    await ctx.send(embed=ver)

  @commands.command(aliases=['ping'], description='clients current ping', brief='clients ping')
  async def p(self, ctx):
    ping = discord.Embed(description=f'Pong. client latency: {round(self.client.latency * 1000)}ms', color=0xffffff)
    await ctx.send(embed=ping)

  @commands.command(
    description='Shows the clients current uptime.',
    brief='clients Uptime',
    aliases=['uptm', 'uptime']
    )
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

  @commands.command(
    description='Info about client. More to come.',
    brief='Info about client'
  )
  async def info(self, ctx):
    info = discord.Embed(title='Paranoid',
    description='This is the main discord bot.\nVersion = 0.0.12',
    color=0x00b7ff)
    # ? 'This is only the test client. Please never use this for your sake. Use the offical client: Pyclient - Main.'
    await ctx.send(embed=info)


def setup(client):
  client.add_cog(General(client))