import discord
from discord.ext import commands
import config
from discord.utils import get
from voice_module.voice import *

intents =discord.Intents.default()
intents.message_content = True
Bot = commands.Bot(command_prefix='+', intents=intents)


@Bot.event
async def on_ready():
    print('Hello')

@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
    global voice
    channel = message.author.voice.channel
    voice = get(Bot.voice_clients, guild=message.guild)
    if voice and voice.is_connected():
        text = message.content
        if(text[0]=='+'):
            return
        voice_file = get_speech(text)
        message.guild.voice_client.play(discord.FFmpegPCMAudio(voice_file))





@Bot.command()
async def con(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(Bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@Bot.command()
async def dis(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(Bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()



Bot.run(config.TOKEN)