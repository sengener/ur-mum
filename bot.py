import discord
from discord.ext import commands
import ffmpeg
import asyncio
import random

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def GetToken():
    filename = '/home/bot-files/token.txt'
    with open(filename, 'r') as file:
        token = file.read()
        return token
TOKEN = GetToken()

def TransEnable(val):
    if val == "1":
        return "enabled"
    elif val == "0":
        return "disabled"        
    else:
        return "val"

def properties(settings):
    filename = 'bot_settings.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if settings in line:
            value = line.split(':')[1].strip()
            return value
        
def ReadIDs(message, group, member):
    filename = "/home/bot-files/" + group + '.txt'
    with open(filename, 'r') as f:
        file_contents = f.read()
        if message is not None and str(message.author.id) in file_contents:
            return 1
        elif member is not None and str(member.id) in file_contents:
            return 1
def editProperties(settings, NewVal):
    filename = 'bot_settings.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if settings in line:
            value = line.split(':')[1].strip()
            new_value = NewVal
            lines[i] = f'{settings}:{new_value}\n'
    with open(filename, 'w') as f:
        f.writelines(lines)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if ReadIDs(message, group="mods", member=None) == 1 and message.content == "YM1" and properties("onVCjoinAudio") == "0":
        editProperties("onVCjoinAudio", 1)
        await message.channel.send("onVCjoinAudio set to " + TransEnable(properties("onVCjoinAudio")))
        print("onVCjoinAudio set to " + properties("onVCjoinAudio"))
        return
    elif ReadIDs(message, group="mods", member=None) == 1 and message.content == "YM1" and properties("onVCjoinAudio") == "1":
        await message.channel.send("onVCjoinAudio is currently set to " + TransEnable(properties("onVCjoinAudio")))
        print("onVCjoinAudio is currently set to " + properties("onVCjoinAudio"))
        return
    elif ReadIDs(message, group="mods", member=None) == 1 and message.content == "YM0" and properties("onVCjoinAudio") == "1":
        editProperties("onVCjoinAudio", 0)
        await message.channel.send("onVCjoinAudio set to " + TransEnable(properties("onVCjoinAudio")))
        print("onVCjoinAudio set to " + properties("onVCjoinAudio"))
        return
    elif ReadIDs(message, group="mods", member=None) == 1 and message.content == "YM0" and properties("onVCjoinAudio") == "0":
        await message.channel.send("onVCjoinAudio is currently set to " + TransEnable(properties("onVCjoinAudio")))
        print("onVCjoinAudio is currently set to " + properties("onVCjoinAudio"))
        return
    else:
        return

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None and properties("onVCjoinAudio") == "1":
        voice_channel = after.channel
        if ReadIDs(member=member, group="zalozeni", message=None) == 1: #based server members ------------------------------------------------------------------
            voice_client = await voice_channel.connect()
            audio_source = discord.FFmpegPCMAudio('/home/sounds/soundOne.mp3')
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(5)
            await voice_client.disconnect()
        elif ReadIDs(member=member, group="cats", message=None) == 1: #cat server members -------------------------------------------------------------------
            soundSelect = random.randint(0,1)
            if soundSelect == 0:
                voice_client = await voice_channel.connect()
                audio_source = discord.FFmpegPCMAudio('/home/sounds/soundTwo.mp3')
                voice_client.play(audio_source)
            elif soundSelect == 1:
                voice_client = await voice_channel.connect()
                audio_source = discord.FFmpegPCMAudio('/home/sounds/soundThree.mp3')
                voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(5)
            await voice_client.disconnect()
        elif ReadIDs(member=member, group="nezalozeni", message=None) == 1: #unbased server members -------------------------------------------------------------------
            voice_client = await voice_channel.connect()
            audio_source = discord.FFmpegPCMAudio('/home/sounds/soundThree.mp3')
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(5)
            await voice_client.disconnect()
        elif ReadIDs(member=member, group="jack", message=None) == 1: #wierd server member -------------------------------------------------------------------
            soundSelect = random.randint(0,1)
            if soundSelect == 0:
                voice_client = await voice_channel.connect()
                audio_source = discord.FFmpegPCMAudio('/home/sounds/soundFour.mp3')
                voice_client.play(audio_source)
            elif soundSelect == 1:
                voice_client = await voice_channel.connect()
                audio_source = discord.FFmpegPCMAudio('/home/sounds/soundSix.mp3')
                voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(5)
            await voice_client.disconnect()
        elif ReadIDs(member=member, group="neverheal", message=None) == 1: #retarded server member -------------------------------------------------------------------
            voice_client = await voice_channel.connect()
            audio_source = discord.FFmpegPCMAudio('/home/sounds/soundFive.mp3')
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(5)
            await voice_client.disconnect()
client.run(TOKEN)