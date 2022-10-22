import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
filename = 'monkey.mp3'
bot = commands.Bot(command_prefix="$", intents=discord.Intents.default())

@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return

    if before.channel is None and after.channel is not None:
        channel = after.channel
        voice_channel = await channel.connect()
        voice_channel.play(discord.FFmpegPCMAudio(source=filename))



bot.run(TOKEN)