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
async def github(ctx):
  embed = discord.Embed(title="Github",
                      description="Hello I'm **\"Cinkociento\"** and **__I'm created Bot Mark__**\nI'm young programist. __I coding in python.__\nI became interested in programming 3 months ago.\nMy current teacher kurczakooo,\non github encouraged me to start programming",
                      colour=0x00b0f4)
  embed.set_author(name="BOT Mark",
                 url="https://github.com/Cinkociento",
                 icon_url="https://img.freepik.com/premium-vector/ebon-mini-mech-stylish-robot-logo-vector-dark-cyber-pal-futuristic-mascot-icon_706143-32434.jpg")
  embed.set_thumbnail(url="https://p.kindpng.com/picc/s/779-7793481_github-logo-github-transparent-background-png-png-download.png")
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

@bot.command()
async def commands(ctx):
  embed = discord.Embed(title="Commands",
                      description="All comends is:\nChapter 1 - basic commands\n1. **__!autor__** - information about the autor\n2. **__!github__** - information and link to the author's github\n3. **__!botinfo__** - information about the bot\n\nChapter 2 - status commands\n1. **__!statusreset__** - resets the bot status\n2. **__!statusplay__** - sets the bot status to game\n3. **__!statuslisten__** - sets the bot status to listen\n4. **__!statuswatch__** - sets the bot status to watch\n5. **__!statuswalk__** - sets the bot status to walk\n6. **__!mystatus__** - sets the bot status to your select status",
                      colour=0x00b0f4)
  embed.set_author(name="BOT Mark",
                 url="https://github.com/Cinkociento",
                 icon_url="https://img.freepik.com/premium-vector/ebon-mini-mech-stylish-robot-logo-vector-dark-cyber-pal-futuristic-mascot-icon_706143-32434.jpg")
  embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz9JN8LXum_lUbIYFGk79pmN6Cwk3YGCY0zw&s")
  embed.set_footer(text="BOT Stupid")
  await ctx.send(embed=embed)



###################################################################### poniżej są komendy do statusu bota

@bot.command()
async def statusreset(ctx):
  embed = discord.Embed(title="Status",
                      description="Status is changed!\nNew status is __\"None status\".__",
                      colour=0x00b0f4)
  embed.set_author(name="BOT Mark",
                 icon_url="https://img.freepik.com/premium-vector/ebon-mini-mech-stylish-robot-logo-vector-dark-cyber-pal-futuristic-mascot-icon_706143-32434.jpg")
  embed.set_thumbnail(url="https://support.discord.com/hc/user_images/fBEuvpvxwAX3_rh2KTUj1Q.png")
  embed.set_footer(text="BOT Stupid")
  await ctx.send(embed=embed)
  await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def statusplay(ctx):
  embed = discord.Embed(title="Status",
                      description="Status is changed!\nNew status is  __\"In game Visual Studio Code\".__",
                      colour=0x00b0f4)
  embed.set_author(name="BOT Mark",
                 icon_url="https://img.freepik.com/premium-vector/ebon-mini-mech-stylish-robot-logo-vector-dark-cyber-pal-futuristic-mascot-icon_706143-32434.jpg")

  embed.set_thumbnail(url="https://support.discord.com/hc/user_images/fBEuvpvxwAX3_rh2KTUj1Q.png")
  embed.set_footer(text="BOT Stupid")
  await ctx.send(embed=embed)
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name='Visual Studio Code'))

@bot.command()
async def statuslisten(ctx):
  embed = discord.Embed(title="Status",
                      description="Status is changed!\nNew status is  __\"Listen Rap God\".__",
                      colour=0x00b0f4)
  embed.set_author(name="BOT Mark",
                 icon_url="https://img.freepik.com/premium-vector/ebon-mini-mech-stylish-robot-logo-vector-dark-cyber-pal-futuristic-mascot-icon_706143-32434.jpg")
  embed.set_thumbnail(url="https://support.discord.com/hc/user_images/fBEuvpvxwAX3_rh2KTUj1Q.png")
  embed.set_footer(text="BOT Stupid")
  await ctx.send(embed=embed)
  await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name='Rap God'))

@bot.command()
async def statuswatch(ctx):
  embed = discord.Embed(title="Status",
                      description="Status is changed!\nNew status is  __\"Watch youtube\".__",
                      colour=0x00b0f4)
  embed.set_author(name="BOT Mark",
                 icon_url="https://img.freepik.com/premium-vector/ebon-mini-mech-stylish-robot-logo-vector-dark-cyber-pal-futuristic-mascot-icon_706143-32434.jpg")
  embed.set_thumbnail(url="https://support.discord.com/hc/user_images/fBEuvpvxwAX3_rh2KTUj1Q.png")
  embed.set_footer(text="BOT Stupid")
  await ctx.send(embed=embed)
  await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='Youtube'))

@bot.command()
async def statuswalk(ctx):
  embed = discord.Embed(title="Status",
                      description="Status is changed!\nNew status is  __\"BOT Mark walk the dog\".__",
                      colour=0x00b0f4)
  embed.set_author(name="BOT Mark",
                 icon_url="https://img.freepik.com/premium-vector/ebon-mini-mech-stylish-robot-logo-vector-dark-cyber-pal-futuristic-mascot-icon_706143-32434.jpg")
  embed.set_thumbnail(url="https://support.discord.com/hc/user_images/fBEuvpvxwAX3_rh2KTUj1Q.png")
  embed.set_footer(text="BOT Stupid")
  await ctx.send(embed=embed)
  await bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='BOT Mark walk the dog')) 

@bot.command()
async def mystatus(ctx, nazwa):
  embed = discord.Embed(title="Status",
                      description="Status is changed!\nNew status is  __\"Your own status\".__",
                      colour=0x00b0f4)
  embed.set_author(name="BOT Mark",
                 icon_url="https://img.freepik.com/premium-vector/ebon-mini-mech-stylish-robot-logo-vector-dark-cyber-pal-futuristic-mascot-icon_706143-32434.jpg")
  embed.set_thumbnail(url="https://support.discord.com/hc/user_images/fBEuvpvxwAX3_rh2KTUj1Q.png")
  embed.set_footer(text="BOT Stupid")
  await ctx.send(embed=embed)
  await bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name=f'{nazwa}'))

################################################################################### 


# ================================================
bot.run(config.token)