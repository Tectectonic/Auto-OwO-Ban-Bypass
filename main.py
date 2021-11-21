import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

#-----SETUP-----#
#SERECTS - TOKEN VALUE YOUR TOKEN#

prefix = "?"

#use the .env feature to hide your token

keep_alive()
token = os.getenv("TOKEN")
#dont put  token here
#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)






@bot.event
async def on_ready():
    
    print(f'''{Fore.RED}
{Fore.GREEN}

Killing Discord


    ....
        Ready for OwO?
Go!  Made By ITZ GLITCHY
''')


















@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="💰 Help AutoOwO ",
        color=420699,
        description=
        f" ❄ **{prefix}autoOwO**\nowoh, owo sell all, owo flip 500 and owo cash 50 seconds.\n\n**{prefix}stopautoOwO**\nstops autoOwO.\n\n** ❄ {prefix}Owobanbypass**\nIts prevent you from banning Owo by taking appropriate time\n Example:-`the bot takes breaak 5 min of runnning 1st break= 5min,2nd break=10min 3rd break=15min` \n\n made by Aditya Codez"
    )
    embed.set_image(
        url=
        "https://images-ext-2.discordapp.net/external/j2-o1dYE9fxqfH2dOHak23cxJOP-Ps6wZBC-r6ld_6E/%3Fwidth%3D432%26height%3D265/https/images-ext-1.discordapp.net/external/__GnKIVffGi3PbAL_Q5p9Dt8AuL9upjYyy3q2fW_fv0/https/media.discordapp.net/attachments/760116404107870228/778236393863381002/20201116_215614.gif"
    )
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('Engine **on**!🚗🏃 ')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(5)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)


@bot.command()
async def stopautoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('Engine **off**! 🚗 ')
    global dmcs
    dmcs = False


@bot.command(pass_context=True)
async def Owobanbypass(ctx):
    await ctx.message.delete()
    await ctx.send('Special Engine **on**! 🚗 ☁ ')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(5)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(17)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(15)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owo hunt') 
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(14)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(300) 

            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(4)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(12)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(16)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(4)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(900)

            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(4)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(12)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(16)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(14)
            await ctx.send('owoh')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(4)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(11)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(900)

            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(8)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await asyncio.sleep(5)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(11)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(18)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(12)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(10)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(5)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(17)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(12)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(15)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(9)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(13)
            await ctx.send('owo hunt')
            print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(14)
            await ctx.send('owo sell all')
            print(f"{Fore.GREEN}succefully sell")
            await ctx.send('owo flip 500')
            print(f"{Fore.GREEN}succefully owo flip 500")
            await asyncio.sleep(14)
            await ctx.send('owo cash')
            print(f"{Fore.GREEN}succefully cash")
            await asyncio.sleep(1200)        
            
# @bot.command()
# async def stopautoOwO(ctx):
#     await ctx.message.delete()
#     await ctx.send('Engine **off good night**!')
#     global dmcs
#     dmcs = False
























keep_alive()
bot.run(token, bot=False)


#made by aditya Codez
