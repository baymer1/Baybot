import discord
from discord.ext import commands
import youtube_dl
import os
import tokenFile
from asyncio import sleep

client = commands.Bot(command_prefix="!")
#@client.command()

client.load_extension("cogs.musicCog")

@client.command()
async def sneeze(ctx):

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Squad Voice')
    vc = await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("sneeze.mp3"))
    await sleep(1)
    await vc.disconnect()




client.run(tokenFile.token)
