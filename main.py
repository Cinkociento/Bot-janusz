import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(f"Login by : {bot.user.name}")

# ================================================
@bot.command()
async def autor(ctx):
  embed = discord.Embed(title="Bot info",
                      description="My autor is **\"Cinkociento\"** he is a __young python programer!__\n__He's coding for 2 months__ and **__he love's coding__**.\nBut he doesn't like any things of git and github.",
                      colour=0xffbe4d)

  embed.set_author(name="BOT Stupid",
                 icon_url="https://img.freepik.com/premium-vector/ebon-mini-mech-stylish-robot-logo-vector-dark-cyber-pal-futuristic-mascot-icon_706143-32434.jpg")

  embed.set_thumbnail(url="https://miro.medium.com/v2/resize:fit:1400/1*mtsk3fQ_BRemFidhkel3dA.png")

  embed.set_footer(text="BOT Stupid")

  await ctx.send(embed=embed)

@bot.command()
async def botinfo(ctx):
  embed = discord.Embed(title="Bot info",
                      description="I'm created by **Cinkociento** when you need more information type **__!autor__**\nI'm created in __python with discord library.__",
                      colour=0xffbe4d)

  embed.set_author(name="BOT Stupid",
                 icon_url="https://img.freepik.com/premium-vector/ebon-mini-mech-stylish-robot-logo-vector-dark-cyber-pal-futuristic-mascot-icon_706143-32434.jpg")

  embed.set_footer(text="BOT Stupid")

  await ctx.send(embed=embed)

#powyżej umieść więcej komend 
#poniżej umieść komendy do zmiany statusu

# @bot.command()
# async def play(ctx):
  # tutaj umieść embeda z informacją o zmianie statusu




# ================================================
bot.run(config.token)