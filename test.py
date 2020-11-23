

@client.command(name='help', description='Help on commands!', aliases=['h'], usage='cog')
async def help(ctx, cog='all'):
  help_embed = discord.Embed(
    title='Help',
    color=0xffffff
  )
  help_embed.set_thumbnail(url=client.user.avatar_url)
  help_embed.set_footer(
    text=f'Requested by {ctx.author.name}',
    icon_url=client.user.avatar_url
  )

  cogs = [cog for cog in client.cogs.keys()]

  if cog == 'all':
    for cog in cogs:
      # Get a list of all commands under each cog

      cog_commands = client.get_cog(cog).get_commands()
      commands_list = ''
      for comm in cog_commands:
        commands_list += f'**{comm.name}** - *{comm.description}*\n'

      # Add the cog's details to the embed.

      help_embed.add_field(
        name=cog,
        value=commands_list,
        inline=False
      )

      # Also added a blank field '\u200b' is a whitespace character.
    pass
  else:
    # If the cog was specified.
    lower_cogs = [cog.lower() for cog in cogs]

    # Check to make sure it exists.
    if cog.lower() in lower_cogs:
      commands_list = client.get_cog(cogs[lower_cogs.index(cog.lower())]).get_commands()
      help_text = ''

      # Formatting the embed.
      for command in commands_list:
        help_text += f'```{command.name}```\n'\
          f'**{command.description}**\n\n'

        if len(command.aliases) > 0:
          help_text += f'**Aliases :** `{"`, `".join(command.aliases)}`\n\n'
        else: help_text += '\n'

        help_text+=f'Format: `@{client.user.name}#{client.user.discriminator}'\
          f' {command.name} {command.usage if command.usage is not None else ""}`\n\n'
      
      help_embed.description = help_text
    else:
      await ctx.send('Invaild cog specified.\nUse `help` command to list all cogs')

  await ctx.send(embed=help_embed)