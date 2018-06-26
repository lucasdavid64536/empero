#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
import random
from discord.ext import commands
import logging
import traceback
import asyncio
import os
from discord import opus



logging.basicConfig(level='INFO')
bot = commands.Bot(command_prefix='e?')
bot.load_extension("admin")
bot.remove_command('help')
bot.load_extension("music")
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True
    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass
    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
load_opus_lib()


@bot.listen()
async def on_error(message, event, *args, **kwargs):
    await ctx.send(':o: | You __don`t__ have acces to this command!')
    

@bot.command(name='8ball')
async def l8ball(ctx):
    await ctx.send(random.choice(['● It is certain.', '● It is decidedly so.', '● Without a doubt.', '● Yes - definitely.', '● You may rely on it', '● As I see it, yes.', '● Most likely.', '● Outlook good.', '● Yes.', '● Signs point to yes.', '● Reply hazy, try again', '● Ask again later.', '● Better not tell you now.', '● Cannot predict now.', '● Concentrate and ask again.', '● Don`t count on it.', '● My reply is no.', '● My sources say no', '● Outlook not so good.', '● Very doubtful.' ]))

    
@commands.cooldown(1, 5, commands.BucketType.user) 
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, reason = None):
    if member is None:
        await ctx.send(":x: | Please provide a user to kick")
    if member != ctx.author:
        await member.send(f'You just got kicked by **{ctx.message.author}** on ** {ctx.guild.name}** for **{reason}**')
        await member.kick()
        await ctx.send(f':white_check_mark: | **{member}** just got kicked.')
    if reason is none:
        await member.send(f'You just got kicked by **{ctx.message.author}** on ** {ctx.guild.name}** for no reason')
        await member.kick()
        await ctx.send(f':white_check_mark: | **{member}** just got kicked.')





@commands.cooldown(1, 5, commands.BucketType.user)     
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, reason = None):
    if member is None:
        await ctx.send(":x: | Please provide a user to ban")
    if member != ctx.author and member != ctx.bot.user:
        await member.send(f'You just got banned by **{ctx.message.author}** on ** {ctx.guild.name}** for **{reason}** ')
        await member.ban()
        await ctx.send(f':white_check_mark: | **{member}** just got banned.')
    if reason is None:
        await member.send(f'You just got banned by **{ctx.message.author}** on ** {ctx.guild.name}** for no reason')
        await member.ban()
        await ctx.send(f':white_check_mark: | **{member}** just got banned.')
        
@bot.listen()
async def on_ready():
          print('Logging in as', bot.user.name)
          await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='e?help'))

            
         
            

@commands.cooldown(1, 5, commands.BucketType.user)  
@bot.command()
async def help(ctx):
    """Help"""
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=discord.Colour.blue())
    em.set_author(name="Empero Help")
    em.add_field(name="**help**", value='Normal commands', inline=False)
    em.add_field(name="**say**", value='Make the bot say whatever you want', inline=False)
    em.add_field(name="**ping**", value='Check the bot latency', inline=False)
    em.add_field(name="**search**", value='Search something on google', inline=False)
    em.add_field(name="**avatar**", value='Get somebody`s avatar', inline=False)
    em.add_field(name="**8ball**", value='Ask the Magic 8-Ball', inline=False)
    em.add_field(name="**help2**", value='Second help page', inline=False)
    em.set_thumbnail(url=ctx.me.avatar_url)
    msg = await ctx.send(embed=em)
  
@commands.cooldown(1, 5, commands.BucketType.user)  
@bot.command()
async def help2(ctx):
    """Help2"""
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=discord.Colour.blue())
    em.set_author(name="Empero Help 2")
    em.add_field(name="**Help2**",value='Member commands', inline=False)
    em.add_field(name="**playerinfo @<member>**", value="""See somebody`s info
[NOTE: This works by: e?pinfo [id/nickname/name/@name]""", inline=False)
    em.add_field(name="**serverinfo**", value="""Get all the informations(In the server)
[NOTE: e?sinfo works too]""", inline=False)
    em.add_field(name="**botinfo**", value="""Get all the bot information
[NOTE: e?binfo works too]""", inline=False)
    em.add_field(name="**lenny**", value='Just a lenny face', inline=False)
    em.add_field(name="**respect**", value='Pay #respect', inline=False)
    em.add_field(name="**support**", value='Returns the support server', inline=False)
    em.add_field(name="**help3**", value='3rd page', inline=False)
    em.set_thumbnail(url=ctx.me.avatar_url)
    msg = await ctx.send(embed=em)
 
@commands.cooldown(1, 5, commands.BucketType.user)  
@bot.command()
async def help3(ctx):
    """Help3"""
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=discord.Colour.blue())
    em.set_author(name="Empero Help 3")
    em.add_field(name="**Help3**",value='Admin commands', inline=False)
    em.add_field(name="**kick**", value='Kicks a member (works only if the members has the Kick permission)', inline=False)
    em.add_field(name="**ban**", value='Bans a member (works only if the members has the Ban permission)', inline=False)
    em.add_field(name="**mass**", value='Send a message to all the members in a guild (BOT Owner only)', inline=False)
    em.add_field(name="**help4**", value='4th page', inline=False)
    em.set_thumbnail(url=ctx.me.avatar_url)
    msg = await ctx.send(embed=em)
 

@commands.cooldown(1, 5, commands.BucketType.user)  
@bot.command()
async def help4(ctx):
    """Help3"""
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=discord.Colour.blue())
    em.set_author(name="Empero Help 4")
    em.add_field(name="**Help4*",value='Music commands', inline=False)
    em.add_field(name="**play**", value='Plays a song', inline=False)
    em.add_field(name="**stop**", value='Stops everything and leaves the voice channel', inline=False)
    em.add_field(name="**queue**", value='Following tracks', inline=False)
    em.add_field(name="**skip**", value='Plays the next song', inline=False)
    em.add_field(name="**pause**", value='Pause the song', inline=False)
    em.add_field(name="**resume**", value='Unpause the song', inline=False)
    em.add_field(name="**join**", value='Connects to a voice channel', inline=False)
    em.set_thumbnail(url=ctx.me.avatar_url)
    msg = await ctx.send(embed=em)
 

@bot.listen()
async def on_message(message : discord.Message):
    if bot.user.mentioned_in(message):
        await message.channel.send(':sleeping: | You woke me up :( . My prefix is `e?` , for a list of commands type `e?help`', delete_after=10)

@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        return await ctx.send(f':no_entry: | Hey, You are being ratelimited! Try again in** {int(error.retry_after)} **seconds!', delete_after=5)
    if isinstance(error, commands.CommandNotFound):
        return await ctx.message.add_reaction('\N{BLACK QUESTION MARK ORNAMENT}')
    error = error.__cause__ or error
    tb = traceback.format_exception(type(error), error, error.__traceback__, limit=2, chain=False)
    tb = ''.join(tb)
    fmt = 'Error in command {}\n\n{}:\n\n{}\n'.format(ctx.command, type(error).__name__, tb)
    print(fmt)




@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def search(ctx, *, query):
    search = query
    URL = "https://www.google.com/search?q="
    words = search.split(" ")

    num = 0
    for w in words:
        if num is 0:
            URL = URL + w
            num = 1
        else:
            URL = URL + "+"+ w

    await ctx.send(URL)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def say(ctx, *, message):
    """Make the BOT say what you want"""
    await ctx.send(message)

@commands.is_owner()
@bot.command()
async def mass(ctx, *, message):
    async def maybe_send(member):
        try:
            await member.send(message)
        finally:
            await ctx.message.delete()

    await asyncio.gather(*[maybe_send(m) for m in ctx.guild.members])





@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def ping(ctx):
    """Get your MS"""
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=discord.Colour.green())
    em.set_author(name="")
    em.add_field(name="Ping", value='Pong! :ping_pong:', inline=True)
    em.add_field(name="MS", value=f'Took : **{ctx.bot.latency * 1000:,.2f}ms**', inline=True)
    await ctx.send(embed=em)


@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def avatar(ctx, member: discord.Member=None):
    """Get your info"""
    if member is None:
        member = ctx.author
    em = discord.Embed(title="", color=discord.Colour.blue())
    em.set_author(name=f"{member}'s avatar")
    em.set_image(url=member.avatar_url)
    msg = await ctx.send(embed=em)








@bot.listen()
async def on_message(message):
    if message.content.lower() == 'e?support' and message.author != bot.user:
        await message.channel.send('The support server is: https://discord.gg/GF3RWsd')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def invite(ctx):
    """Gives you the BOT invite link."""
    await ctx.send("Invite the BOT here: https://discordapp.com/api/oauth2/authorize?client_id=459000712538357760&permissions=201603158&scope=bot")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def support(ctx):
    """Get the lenny face"""
    await ctx.send("")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def lenny(ctx):
    """Get the lenny face"""
    await ctx.send("( ͡° ͜ʖ ͡° )")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def sinfo(ctx, member: discord.Member=None):
    """Get the server info"""
    if member is None:
        member = ctx.author
    em = discord.Embed(title=f"{ctx.guild.name}'s info", color=discord.Colour.blue())
    em.set_author(name="Server Info")
    em.add_field(name="Name", value=ctx.guild.name)
    em.add_field(name="ID", value=ctx.guild.id)
    em.add_field(name="Owner", value=ctx.guild.owner)
    em.add_field(name="Owner ID", value=ctx.guild.owner.id)
    em.add_field(name="Roles", value=len(ctx.guild.roles))
    em.add_field(name="Members", value=ctx.guild.member_count)
    em.add_field(name="Created", value=ctx.guild.created_at)
    em.set_thumbnail(url=ctx.guild.icon_url)
    msg = await ctx.send(embed=em)



@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def serverinfo(ctx, member: discord.Member=None):
    """Get the server info"""
    if member is None:
        member = ctx.author
    em = discord.Embed(title=f"{ctx.guild.name}'s info", color=discord.Colour.blue())
    em.set_author(name="Server Info")
    em.add_field(name="Name", value=ctx.guild.name)
    em.add_field(name="ID", value=ctx.guild.id)
    em.add_field(name="Owner", value=ctx.guild.owner)
    em.add_field(name="Owner ID", value=ctx.guild.owner.id)
    em.add_field(name="Roles", value=len(ctx.guild.roles))
    em.add_field(name="Members", value=ctx.guild.member_count)
    em.add_field(name="Created", value=ctx.guild.created_at)
    em.set_thumbnail(url=ctx.guild.icon_url)
    msg = await ctx.send(embed=em)



@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def respect(ctx):
    """Pay respect"""
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=discord.Colour.green())
    em.set_author(name="")
    em.add_field(name=f"{ctx.author.name}", value='Press :regional_indicator_f: to pay respect', inline=True)
    msg = await ctx.send(embed=em)
    await msg.add_reaction('\N{regional indicator symbol letter f}')


@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def playerinfo(ctx, member: discord.Member=None):
    """Get your info"""
    if member is None:
        member = ctx.author
    em = discord.Embed(title=f"{member}'s info", color=discord.Colour.blue())
    em.set_author(name="Player info")
    em.add_field(name="Name", value=member.name)
    em.add_field(name="ID", value=member.id)
    em.add_field(name="BOT:", value=member.bot)
    em.add_field(name="Tag", value=member.discriminator)
    em.add_field(name="Top Role", value=member.top_role)
    em.add_field(name="Nick", value=member.nick)
    em.add_field(name="Joined", value=member.joined_at)
    em.set_thumbnail(url=member.avatar_url)
    msg = await ctx.send(embed=em)


@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def pinfo(ctx, member: discord.Member=None):
    """Get your info"""
    if member is None:
        member = ctx.author
    em = discord.Embed(title=f"{member}'s info", color=discord.Colour.blue())
    em.set_author(name="Player info")
    em.add_field(name="Name", value=member.name)
    em.add_field(name="ID", value=member.id)
    em.add_field(name="BOT:", value=member.bot)
    em.add_field(name="Tag", value=member.discriminator)
    em.add_field(name="Top Role", value=member.top_role)
    em.add_field(name="Nick", value=member.nick)
    em.add_field(name="Joined", value=member.joined_at)
    em.set_thumbnail(url=member.avatar_url)
    msg = await ctx.send(embed=em)





@commands.cooldown(1, 5, commands.BucketType.user)  
@bot.command()
async def botinfo(ctx):
    """Get the BOT info"""
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=discord.Colour.blue())
    em.set_author(name="BOT Info")
    em.add_field(name="Name", value=ctx.bot.user.name, inline=True)
    em.add_field(name="ID", value=ctx.bot.user.id, inline=True)
    em.add_field(name="Prefix", value=ctx.bot.command_prefix, inline=True)
    em.add_field(name="Made with", value='Python 3.6.5', inline=True)
    em.add_field(name="Tag:", value=ctx.me.discriminator, inline=True)
    em.add_field(name="Creator", value='<@404708655578218511>', inline=True)
    em.add_field(name="Created at", value=ctx.bot.user.created_at, inline=True)
    em.set_thumbnail(url=ctx.me.avatar_url)
    msg = await ctx.send(embed=em)
    




@commands.cooldown(1, 5, commands.BucketType.user)  
@bot.command()
async def binfo(ctx):
    """Get the BOT info"""
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=discord.Colour.blue())
    em.set_author(name="BOT Info")
    em.add_field(name="Name", value=ctx.bot.user.name, inline=True)
    em.add_field(name="ID", value=ctx.bot.user.id, inline=True)
    em.add_field(name="Prefix", value=ctx.bot.command_prefix, inline=True)
    em.add_field(name="Made with", value='Python 3.6.5', inline=True)
    em.add_field(name="Tag:", value=ctx.me.discriminator, inline=True)
    em.add_field(name="Creator", value='<@404708655578218511>', inline=True)
    em.add_field(name="Created at", value=ctx.bot.user.created_at, inline=True)
    em.set_thumbnail(url=ctx.me.avatar_url)
    msg = await ctx.send(embed=em)
        







bot.run(os.getenv("TOKEN"))
