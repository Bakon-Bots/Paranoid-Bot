import discord
from discord.ext import commands

#TODO: SET ALL MESSAGES TO EMBEDS.

class Logging(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_message_delete(self, message):
    messagelog = self.client.get_channel(786730020030119938)
    deleted = discord.Embed(
        description=f"Message deleted in {message.channel.mention}", color=0x4287f5
    ).set_author(name=message.author, url=discord.Embed.Empty, icon_url=message.author.avatar_url)

    deleted.add_field(name="Message", value=message.content)
    deleted.timestamp = message.created_at
    await messagelog.send(embed=deleted)

  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    messagelog = self.client.get_channel(786730020030119938)
    print(before)
    print(after)
    edit = discord.Embed(
        description=f"Message edited in {before.channel.mention}", color=0x00b7ff
    ).set_author(name=before.author, url=discord.Embed.Empty, icon_url=before.author.avatar_url)

    edit.add_field(name="Old", value=before.content)
    edit.add_field(name="New", value=after.content)
    edit.timestamp = before.created_at
    await messagelog.send(embed=edit)

def setup(client):
  client.add_cog(Logging(client))