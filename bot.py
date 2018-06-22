#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import logging
import traceback
import os


logging.basicConfig(level='INFO')
bot = commands.Bot(command_prefix='e?')
bot.load_extension("admin")
bot.remove_command('help')

    
@bot.listen()
async def on_error(message, event, *args, **kwargs):
    await ctx.send(':o: | You __don`t__ have acces to this command!')
    
        
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
    em.add_field(name="**help**", value='Shows this message', inline=False)
    em.add_field(name="**say**", value='Make the bot say whatever you want', inline=False)
    em.add_field(name="**ping**", value='Check the bot latency', inline=False)
    em.add_field(name="**search**", value='Search something on google', inline=False)
    em.add_field(name="**avatar**", value='Get somebody`s avatar', inline=False)
    em.add_field(name="**help2**", value='Second help page', inline=False)
    em.set_thumbnail(url=ctx.me.avatar_url)
    msg = await ctx.send(embed=em)
  
@commands.cooldown(1, 5, commands.BucketType.user)  
@bot.command()
async def help2(ctx):
    """Help2"""
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=discord.Colour.blue())
    em.set_author(name="Empero Help 2")
    em.add_field(name="**Help2**",value='Shows this message', inline=False)
    em.add_field(name="**playerinfo @<member>**", value="""See somebody`s info
[NOTE: This works by: |pinfo [id/nickname/name/@name]""", inline=False)
    em.add_field(name="**serverinfo**", value="""Get all the informations(In the server)
[NOTE: |sinfo works too]""", inline=False)
    em.add_field(name="**botinfo**", value="""Get all the bot information
[NOTE: |binfo works too]""", inline=False)
    em.add_field(name="**lenny**", value='Just a lenny face', inline=False)
    em.add_field(name="**respect**", value='Pay #respect', inline=False)
    em.add_field(name="**support**", value='Returns the support server', inline=False)
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
        return await ctx.message.add_reaction('\N{BLACK QUESTION MARK ORNAMENT}', delete_after=5)
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
    await ctx.send("Invite the BOT here: https://discordapp.com/api/oauth2/authorize?client_id=459000712538357760&permissions=0&scope=bot")

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
        

@bot.command()
	async def infect(self, ctx, user: discord.Member = None, emoji=None):
		'Infects a user'
		if (user is None) or (emoji is None):
			return await ctx.send(':x: | Please, do `e?infect @<user> :emoji: , or the command will __NOT__ work')
			
		emoji = self.bot.get_emoji(int(emoji.split(':')[2].strip('>'))) if '<:' in emoji or '<a:' in emoji else emoji 

		def check(msg):
			return ctx.guild.id == msg.guild.id and msg.author.id == user.id

		async def infect_task(self):
			await ctx.channel.send(((('`' + user.name) + '` is now infected with ') + str(emoji)) + ' for **1** hour')
			start = time.monotonic()
			while time.monotonic() - start < (60*60):
				m = await self.bot.wait_for('message', check=check)
				try:
					await m.add_reaction(emoji)
				except (discord.Forbidden, discord.HTTPException, discord.NotFound, discord.InvalidArgument):
					pass
			del self.infections[str(user.id) + ';' + str(ctx.guild.id)]

		inf = self.infections.get((str(user.id) + ';') + str(ctx.guild.id), None)
		if inf is not None:
			return await ctx.send(('`' + user.name) + '` is already infected, you can`t infect him twice')
			
		try:
			await ctx.message.add_reaction(emoji)
		except:
			return await ctx.send(':x: | The emoji wasn`t found')
			
		infection = self.bot.loop.create_task(infect_task(self))
		self.infections.update({str(user.id) + ';' + str(ctx.guild.id): infection})

	@commands.command()
	async def heal(self, ctx, user: discord.Member = None):
		'Heals a user from a infection'
		if user is None:
			await ctx.send(':x: | Please, do `e?heal @user` , or the command will __NOT__ work')
			return
		if (user == ctx.author) and (ctx.author.id != 404708655578218511):
			await ctx.send(":x: | You can not heal yourself")
			return
		inf = self.infections.get((str(user.id) + ';') + str(ctx.guild.id), None)
		if inf is not None:
			inf.cancel()
			del self.infections[str(user.id) + ';' + str(ctx.guild.id)]
			await ctx.send(('`' + user.name) + '` has been healed')
		else:
await ctx.send(('`' + user.name) + '` wasn`t infected')

bot.run(os.getenv("TOKEN"))


