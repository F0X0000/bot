import yaml
import discord
import socket
from dotenv import load_dotenv
import os
from other import *

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} jest online!")
    await bot.change_presence(status=discord.Status.idle, activity = discord.Activity(type=discord.ActivityType.listening, name="/help"))

@bot.command(description="Wyświetla informacje o bocie.")
async def help(ctx):
    embed = discord.Embed(description="Wszystkie moje komendy znajdują się pod `/`")
    await ctx.respond(embed = embed)

@bot.command(name="8ball", description=" 🔮 Magiczna kula")
async def magiczna_kula(ctx, pytanie: discord.Option(str)):
    odpowiedz = losuj("other/8ball.txt")
    embed = discord.Embed(title=f"{odpowiedz}", color=discord.Colour.blurple())
    embed.set_author(name=f"{pytanie}", icon_url="https://em-content.zobj.net/source/microsoft/379/crystal-ball_1f52e.png")
    await ctx.respond(embed = embed)

bot.run(os.getenv('TOKEN'))