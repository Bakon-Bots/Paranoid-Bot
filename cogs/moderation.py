import discord
from discord.ext import commands
from random import random
import math

#TODO: SET ALL MESSAGES TO EMBEDS.

ban_dict = dict()
warn_case = list()

class Moderation(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command(description='Kicks a user. Must have Kick memebers permission.', brief='Kicks a user')
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.Member, *, reason='No reason specified.'):
    await member.kick(reason=reason)
    await ctx.send(f'{member} was kicked. Reason: {reason}.')


  @commands.command(description='Bans a user. Must have Ban members permission', brief='Bans a user')
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member:discord.Member, *, reason):
    global ban_dict
    ban_dict[member.name] = reason
    await member.ban(reason=reason)
    await ctx.send(f'{member} was banned by {ctx.author}. Reason: {reason}.')


  @commands.command(description='Unbans a user. Must have Ban members permission', brief='Unbans a user')
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discrim = member.split('#')
    for ban_entry in banned_users:
      user = ban_entry.user
      
      if (user.name, user.discriminator) == (member_name, member_discrim):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.mention}.')
        return


  @commands.command(description='Clears a set of messages. Must have manage messages permission', brief='Purges messages younger than 2 weeks')
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount:int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Purged {amount} messages.')
  @clear.error
  async def clear_error(self, ctx, err):
    if isinstance(err, commands.MissingRequiredArgument):
      clear_err = discord.Embed(title=f'Clear', description=f'Use -clear <amount>', color=0xa83291)
      await ctx.send(embed=clear_err)


  @commands.command()
  async def warn(self, ctx, user:discord.Member, *, reason):
    global warn_case
    ran = str(random() * 4).replace('.', '')
    warn_case[ran] = f'{user} warned by {ctx.author}.\n\nReason: {reason}'

    warn = discord.Embed(title=f'Warned {user}', color=0xfcba03)
    warn.add_field(value=f'\n\nUse -getwarn {ran} to retrieve the warn.')
    await ctx.message.delete()
    await ctx.send(embed=warn)

  @warn.error
  async def warn_err(self, ctx, err):
    await ctx.send(err)
    if isinstance(err, commands.MissingRequiredArgument):
      #warn_err = discord.Embed(title=f'Warning', description=f'Use -warn <user> <reason>', color=0xfcba03)
      #await ctx.message.delete()
      await ctx.send('Use -warn <user> <reason>')#embed=warn_err)


  @commands.command()
  async def getwarn(self, ctx, pernum):
    global warn_case

    if pernum in warn_case:
      warn = warn_case[pernum]
      warn = discord.Embed(title='Warning', description=f'{warn}', color=0xfcba03)
      await ctx.send(embed=warn)

    else: await ctx.send(f'```Could not find a warning with case number {casenum}.```')

def setup(client):
  client.add_cog(Moderation(client))