import discord
from discord.ext import commands


class Math(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(description='Add many numbers together.', brief='Add many numbers together.')
  async def add(self, ctx, *args):
    num = 0
    for number in args: num += int(number)
    await ctx.send(f'{num}')

  @commands.command(description='Subtract many numbers together.', brief='Subtract many numbers together.')
  async def sub(self, ctx, *args):
    num = 0
    for number in args: num -= int(number)
    await ctx.send(f'{num}')

  @commands.command(description='Multiply many numbers together.', brief='Multiply many numbers together.')
  async def mult(self, ctx, *args):
    num = 1
    for number in args: num *= int(number)
    await ctx.send(f'{num}')

  @commands.command(description='Divide many numbers together.', brief='Divide many numbers together.')
  async def div(self, ctx, *args):
    try:
      num = 0
      for number in args: num /= int(number)
      await ctx.send(f'{num}')
    except ZeroDivisionError:
      await ctx.send(f'Attept to divide by 0.')

  @commands.command(description='Modulo one num by another.', brief='Modulo one num by another.')
  async def mod(self, ctx, one, two):
    await ctx.send(f'{one % two}')


def setup(client):
  client.add_cog(Math(client))