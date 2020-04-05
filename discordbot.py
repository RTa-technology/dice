import os
import re
import traceback
import random
import discord
from discord.ext import commands as rta


bot = rta.Bot(command_prefix='!')#, help_command=JapaneseHelpCommand()

token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command(name="d")
async def d(ctx, dice: str):
    """{n}d{n}の書式で入力"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('!d NdNの書式で入力')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    mappedData = map(int, result.split(","))
    output = list(mappedData)
    sumresult = sum(output)
    msg = f"{ctx.author.mention}\n" + result
    await ctx.send(msg)
    await ctx.send(sumresult)


    
@bot.command(name="dice")
async def dice(ctx, dice: str):
    """{n}d{n}の書式で入力"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('!dice NdNの書式で入力')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    mappedData = map(int, result.split(","))
    output = list(mappedData)
    sumresult = sum(output)
    embed = discord.Embed(title=sumresult ,description=f"{ctx.author.name}\n{ctx.message.content}",color=discord.Colour.from_rgb(255,0,0))
    embed.set_author(name=result)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

@bot.command(name="dp")
async def dp(ctx, dice: str):
    """{n}d{n}+kの書式で入力"""
    rolls, str1 = map(str, dice.split('d'))
    limit, plus =map(int, str1.split('+'))

    rolls = int(rolls)
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    mappedData = map(int, result.split(","))
    output = list(mappedData)
    sumresult = sum(output)
    firesult = sumresult + plus
    msg = f"{ctx.author.mention}\n" + result
    msg2 = f"{sumresult} + {plus}"
    embed = discord.Embed(title=firesult ,description=f"{ctx.author.name}\n{sumresult}\n{msg2}\n{ctx.message.content}",color=discord.Colour.from_rgb(255,0,0))
    embed.set_author(name=result)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

    
    
    
    
    
@bot.command(name="dj")
async def dj(ctx, dice: str):
    """{n}d{n}<kの書式で入力"""
    try:
        rolls, str1 = map(str, dice.split('d'))
        limit, judge =map(int, str1.split('<'))
    except Exception:
        await ctx.send('!d NdN<kの書式で入力')
        return
    rolls = int(rolls)
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    mappedData = map(int, result.split(","))
    output = list(mappedData)
    sumresult = sum(output)
    sumresult = int(sumresult)
    if sumresult < judge:
        msg1 = f"{sumresult} < {judge} => 成功"
    else:
        msg1 = f"{sumresult} < {judge} => 失敗"

    msg = f"{ctx.author.mention}\n" + result
    embed = discord.Embed(title=msg1 ,description=f"{ctx.author.name}\n{sumresult}\n{ctx.message.content}",color=discord.Colour.from_rgb(255,0,0))
    embed.set_author(name=result)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)



# @bot.command(name="di")
# async def di(ctx, dice: str):
#     """{n}d{n}の書式で入力"""
#     if dice in "+":
#         rolls, str1 = map(str, dice.split('d'))
#         limit, plus =map(int, str1.split('p'))
#         rolls = int(rolls)
#         result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#         mappedData = map(int, result.split(","))
#         output = list(mappedData)
#         sumresult = sum(output)
#         firesult = sumresult + plus
#         msg = f"{ctx.author.mention}\n" + result
#         msg2 = f"{sumresult} + {plus}"
#         await ctx.send(msg)
#         await ctx.send(sumresult)
#         await ctx.send(msg2)
#         await ctx.send(firesult)
#     else:
#         rolls, limit = map(int, dice.split('d'))
#         result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#         mappedData = map(int, result.split(","))
#         output = list(mappedData)
#         sumresult = sum(output)
#         embed = discord.Embed(title=sumresult ,description=f"{ctx.author.name}\n{ctx.message.content}",color=discord.Colour.from_rgb(255,0,0))
#         embed.set_author(name=result)
#         await ctx.send(f"{ctx.author.mention}")
#         await ctx.send(embed=embed)
#         return
    
bot.run(token)

