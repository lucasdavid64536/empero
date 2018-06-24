#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import logging
import discord
from discord.ext import commands
import asyncio
import os

logging.basicConfig(level='INFO')
bot = commands.Bot(command_prefix='-')
bot.remove_command('help')


@bot.listen()
async def on_ready():
          print(f'Logging in as... {bot.user.name}')
          await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='-announce <message>'))

def guild_owner_only():
    def check(ctx):
        return ctx.guild and ctx.guild.owner == ctx.author
    return commands.check(check)


@commands.cooldown(1, 60, commands.BucketType.user)
@guild_owner_only()
@bot.command()
async def announce(ctx, *, message):
    async def maybe_send(member):
        try:
            await member.send(message)
            await ctx.message.delete()
        finally:
            return

    await asyncio.gather(*[maybe_send(m) for m in ctx.guild.members])

@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        return await ctx.send('Cool down, people don`t like when you spam DM them, right?', delete_after=5)

@bot.command()
async def invite(ctx):
    await ctx.send(f'Invite **{ctx.me.name}** here!: https://discordapp.com/oauth2/authorize?client_id=460403067196538880&permissions=201603158&scope=bot')



@commands.cooldown(1, 5, commands.BucketType.user)  
@bot.command()
async def help(ctx):
    """Help"""
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=discord.Colour.blue())
    em.set_author(name="Announce Help")
    em.add_field(name="**announce**", value='DMs all player with a message (Guild Owner only)', inline=False)
    em.add_field(name="**invite**", value='Returns the BOT invite link', inline=False)
    em.set_thumbnail(url=ctx.me.avatar_url)
    msg = await ctx.send(embed=em)

bot.run(os.getenv("TOKEN"))
