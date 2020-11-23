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

  
  @commands.command(name='help', description='The help command!')
  async def help_command(self, ctx, cog='all'):
    help_embed = discord.Embed(
      title='Help',
      color=0xffffff
    )
    help_embed.set_thumbnail(url=self.client.user.avatar_url)
    help_embed.set_footer(
      text=f'Requested by {ctx.message.author.name}',
      icon_url=self.client.user.avatar_url
    )

    # Get a list of all cogs
    cogs = [c for c in self.client.cogs.keys()]

    if cog == 'all':
      for cog in cogs:

        cog_commands = self.client.get_cog(cog).get_commands()
        commands_list = ''
        for comm in cog_commands:
          commands_list += f'**{comm.name}** - *{comm.description}*\n'

          # Add the cog's details to the embed.
          help_embed.add_field(
            name=cog,
            value=commands_list,
            inline=False
            )
        pass
    else:
      # If the cog was specified
      lower_cogs = [c.lower() for c in cogs]

      # If the cog actually exists.
      if cog.lower() in lower_cogs:
        commands_list = self.client.get_cog_commands(cogs[ lower_cogs.index(cog.lower()) ])
        help_text=''
        
        # Format
        for command in commands_list:
          help_text += f'```{command.name}```\n' \
            f'**{command.description}**\n\n'
            
          help_text += f'**Aliases :** `{"`, `".join(command.aliases)}`\n\n' if len(command.aliases) > 0 else help_text += '\n'

          help_text += f'Format: `@{self.client.user.name}#{self.client.user.discriminator}' \
            f' {command.name} {command.usage if command.usage is not None else ""}`\n\n'

        help_embed.description = help_text
      else:
        # Notify the user of invalid cog and finish the command
        await ctx.send('Invalid cog specified.\nUse `help` command to list all cogs.')

    await ctx.send(embed=help_embed)


def setup(client):
  client.add_cog(General(client))