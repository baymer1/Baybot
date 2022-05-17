import discord
from discord.ext import commands
import youtube_dl
import os
import tokenFile2
from asyncio import sleep


client = commands.Bot(command_prefix="!")
#@client.command()

client.load_extension("cogs.musicCog")


@client.command()
async def fart(ctx, *, channel = None):
    
    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Voice')
    try:
        if not channel:
            voiceChannel = ctx.author.voice.channel
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    except AttributeError:
        await ctx.send("You're not in a VC :( Please join... please...")
        
    
    vc = await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("fart.mp3"))
    await sleep(1)
    await vc.disconnect()

@client.event
async def on_message(message):
    if message.content.find("test") != -1:
        await message.channel.send("HI!")

@client.command()
async def sneeze(ctx, *, channel = None):
    
    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Voice')
    try:
        if not channel:
            voiceChannel = ctx.author.voice.channel
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    except AttributeError:
        await ctx.send("You're not in a VC :( Please join... please...")
        
    
    vc = await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("sneeze.mp3"))
    await sleep(1)
    await vc.disconnect()

@client.command()
async def thanks(ctx, *, channel = None):
    
    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Voice')
    try:
        if not channel:
            voiceChannel = ctx.author.voice.channel
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    except AttributeError:
        await ctx.send("You're not in a VC :( Please join... please...")
        
    
    vc = await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("tyForComing.mp3"))
    await sleep(2)
    await vc.disconnect()

@client.command()
async def slurp(ctx, *, channel = None):
    
    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Voice')
    try:
        if not channel:
            voiceChannel = ctx.author.voice.channel
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    except AttributeError:
        await ctx.send("You're not in a VC :( Please join... please...")
        
    
    vc = await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("slurp.mp3"))
    await sleep(1)
    await vc.disconnect()

@client.command()
async def itgo(ctx, *, channel = None):
    
    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Voice')
    try:
        if not channel:
            voiceChannel = ctx.author.voice.channel
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    except AttributeError:
        await ctx.send("You're not in a VC :( Please join... please...")
        
    
    vc = await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("itGo.mp3"))
    await sleep(3)
    await vc.disconnect()



@client.command()
async def beastmode(ctx, *, channel = None):
    
    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Voice')
    try:
        if not channel:
            voiceChannel = ctx.author.voice.channel
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    except AttributeError:
        await ctx.send("You're not in a VC :( Please join... please...")
        
    
    vc = await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("beastMode.mp3"))
    await sleep(8)
    await vc.disconnect()
    
@client.command()
async def throwup(ctx, *, channel = None):
    
    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Voice')
    try:
        if not channel:
            voiceChannel = ctx.author.voice.channel
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    except AttributeError:
        await ctx.send("You're not in a VC :( Please join... please...")
        
    
    vc = await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("throwUp.mp3"))
    await sleep(1)
    await vc.disconnect()
    
@client.command()
async def sus(ctx, *, channel = None):
    
    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Voice')
    try:
        if not channel:
            voiceChannel = ctx.author.voice.channel
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    except AttributeError:
        await ctx.send("You're not in a VC :( Please join... please...")
        
    
    vc = await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("sus.mp3"))
    await sleep(3)
    await vc.disconnect()
    
@client.command()
async def totm(ctx, *, channel = None):
    
    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Voice')
    try:
        if not channel:
            voiceChannel = ctx.author.voice.channel
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    except AttributeError:
        await ctx.send("You're not in a VC :( Please join... please...")
        
    
    vc = await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("totm.mp3"))
    await sleep(6)
    await vc.disconnect()

@client.command()
async def lgts(ctx, *, channel = None):
    
    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Voice')
    try:
        if not channel:
            voiceChannel = ctx.author.voice.channel
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    except AttributeError:
        await ctx.send("You're not in a VC :( Please join... please...")
        
    
    vc = await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("lgts.mp3"))
    await sleep(3)
    await vc.disconnect()

@client.command()
async def dab(ctx):
    await ctx.send("ヽ(o⌣oヾ)")
    
@client.command()
async def rateme(ctx):
    await ctx.send(ctx.author.mention+" is really hot!")
    
    
@client.command()
async def letsgo(ctx):
    await ctx.send("☜(˚▽˚)☞")
    
@client.command()
async def ip(ctx):
    await ctx.send("christian-squad.mcnode.net")

client.run(tokenFile.token)
