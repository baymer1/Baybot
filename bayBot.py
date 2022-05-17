import discord
from discord.ext import commands
import youtube_dl
import os
import tokenFile
from asyncio import sleep


client = commands.Bot(command_prefix="!")
#@client.command()

client.load_extension("cogs.musicCog")

async def playsound(ctx, *, channel = None, soundName, soundTime):
    try:
        if not channel:
            voiceChannel = ctx.author.voice.channel
        else:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
        except AttributeError:
            await ctx.send("You're not in a VC :( Please join... please...")
            
        vc await voiceChannel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(soundName))
        await sleep(soundTime)
        await vc.disconnect
        
@client.command()
async def fart(ctx, *, channel = None):
    
    playsound(ctx, *, channel = None, "fart.mp3", 1)

@client.command()
async def sneeze(ctx, *, channel = None):
    
    playsound(ctx, *, channel = None, "sneeze.mp3", 1)

@client.command()
async def thanks(ctx, *, channel = None):
    
    playsound(ctx, *, channel = None, "tyForComing.mp3", 2)

@client.command()
async def slurp(ctx, *, channel = None):
    
    playsound(ctx, *, channel = None, "slurp.mp3", 1)

@client.command()
async def itgo(ctx, *, channel = None):
    
    playsound(ctx, *, channel = None, "itGo.mp3", 3)



@client.command()
async def beastmode(ctx, *, channel = None):
    
    playsound(ctx, *, channel = None, "beastMode.mp3", 8)
    
@client.command()
async def throwup(ctx, *, channel = None):
    
    playsound(ctx, *, channel = None, "throwUp.mp3", 1)
    
@client.command()
async def sus(ctx, *, channel = None):
    
    playsound(ctx, *, channel = None, "sus.mp3", 3)
    
@client.command()
async def totm(ctx, *, channel = None):
    
    playsound(ctx, *, channel = None, "totm.mp3", 6)

@client.command()
async def lgts(ctx, *, channel = None):
    
    playsound(ctx, *, channel = None, "lgts.mp3", 3)

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
