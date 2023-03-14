import discord
from discord.ext import commands
import ffmpeg
import asyncio

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def GetToken():
    filename = '/home/token/token.txt'
    with open(filename, 'r') as file:
        token = file.read()
        return token

TOKEN = GetToken()

kaili = 780737111182934066
rover = 507535631119810565
greedy = 409415460333813771
cat = 593391713515470848
catgirl = 829445670091096064
Edward_David_Andrew = 639477130358423558
reco = 403541560349687820
homie = 527265429027160074
jack = 348818807026089985
neverheal = 675892132434673675

zalozeni = [kaili, rover, greedy, reco, homie]
nezalozeni = [Edward_David_Andrew]
cats = [cat, catgirl]
mods = [kaili, rover]

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

def isMod(message):
    if message.author.id in mods:
        return 1

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    
    if isMod(message) == 1 and message.content == "YM1" and properties("onVCjoinAudio") == "0":
        editProperties("onVCjoinAudio", 1)
        await message.channel.send("onVCjoinAudio set to " + TransEnable(properties("onVCjoinAudio")))
        print("onVCjoinAudio set to " + properties("onVCjoinAudio"))
        return
    elif isMod(message) == 1 and message.content == "YM1" and properties("onVCjoinAudio") == "1":
        await message.channel.send("onVCjoinAudio is currently set to " + TransEnable(properties("onVCjoinAudio")))
        print("onVCjoinAudio is currently set to " + properties("onVCjoinAudio"))
        return
    elif isMod(message) == 1 and message.content == "YM0" and properties("onVCjoinAudio") == "1":
        editProperties("onVCjoinAudio", 0)
        await message.channel.send("onVCjoinAudio set to " + TransEnable(properties("onVCjoinAudio")))
        print("onVCjoinAudio set to " + properties("onVCjoinAudio"))
        return
    elif isMod(message) == 1 and message.content == "YM0" and properties("onVCjoinAudio") == "0":
        await message.channel.send("onVCjoinAudio is currently set to " + TransEnable(properties("onVCjoinAudio")))
        print("onVCjoinAudio is currently set to " + properties("onVCjoinAudio"))
        return
    else:
        return


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None and properties("onVCjoinAudio") == "1":
        voice_channel = after.channel
        if member.id in zalozeni:
            voice_client = await voice_channel.connect()
            audio_source = discord.FFmpegPCMAudio('/home/sounds/soundOne.mp3')
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(5)
            await voice_client.disconnect()
        
        elif member.id in cats:
            voice_client = await voice_channel.connect()
            audio_source = discord.FFmpegPCMAudio('/home/sounds/soundTwo.mp3')
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(5)
            await voice_client.disconnect()
        
        elif member.id in nezalozeni:
            voice_client = await voice_channel.connect()
            audio_source = discord.FFmpegPCMAudio('/home/sounds/soundThree.mp3')
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(5)
            await voice_client.disconnect()
        elif member.id == jack:
            voice_client = await voice_channel.connect()
            audio_source = discord.FFmpegPCMAudio('/home/sounds/soundFour.mp3')
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(5)
            await voice_client.disconnect()
        elif member.id == neverheal:
            voice_client = await voice_channel.connect()
            audio_source = discord.FFmpegPCMAudio('/home/sounds/soundFive.mp3')
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(5)
            await voice_client.disconnect()
client.run(TOKEN)