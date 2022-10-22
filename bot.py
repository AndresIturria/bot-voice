import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return

    if before.channel is None and after.channel is not None:
        channel = after.channel
        voice = await channel.connect
        source = discord.FFmpegPCMAudioAudio('monkey.mp3')
        player = voice.play(source)


bot.run(TOKEN)