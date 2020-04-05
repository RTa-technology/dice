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
    try:
        rolls, str1 = map(str, dice.split('d'))
        limit, plus =map(int, str1.split('+'))
    except Exception:
        await ctx.send('!d NdN+kの書式で入力')
        return
    rolls = int(rolls)
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    mappedData = map(int, result.split(","))
    output = list(mappedData)
    sumresult = sum(output)
    firesult = sumresult + plus
    msg = f"{ctx.author.mention}\n" + result
    msg2 = f"{sumresult} + {plus}"
    await ctx.send(msg)
    await ctx.send(sumresult)
    await ctx.send(msg2)
    await ctx.send(firesult)
    
    
    
    
    
    
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
        if sumresult < judge:
            msg1 = f"{sumresult} < {judge} => 成功"
        else:
            msg1 = f"{sumresult} < {judge} => 失敗"
    msg = f"{ctx.author.mention}\n" + result
    await ctx.send(msg)
    await ctx.send(msg1)
    await ctx.send(sumresult)
    
    
    
    
# @bot.command(name="dp")
# async def dp(ctx, dice: str):
#     l2 = '+'
#     l3 = '<'
#     """{n}d{n}の書式で入力"""

#     if dice in l2:
#         rolls, str1 = map(str, dice.split('d'))
#         limit, plus = map(str, str1.split('+'))
#         rolls = int(rolls)
#         limit = int(limit)
#         plus = int(plus)
#         result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#         mappedData = map(int, result.split(","))
#         output = list(mappedData)
#         sumresult = sum(output)
#         sumresult = sumresult + plus
        
#     elif dice in l3:
#         rolls, str2 = map(str, dice.split('d'))
#         plus, judge_limit = map(str, str2.split('<'))
#         rolls = int(rolls)
#         limit = int(limit)
#         judge_limit = int(judge_limit)
#             if sumresult < judge_limit:
#                 sumresult = f"{str(sumresult)} < {str(judge_limit)} => 成功"
#             elif sumresult >= judge_limit :
#                 sumresult = f"{str(sumresult)} >= {str(judge_limit)} => 失敗"
#             else:
#                 sumresult = sumresult
#                 return
        
#     else:
#         rolls, str1 = map(str, dice.split('d'))
#         limit, str2 = map(str, str1.split('+'))
#         plus, judge_limit = map(str, str2.split('<'))
#         rolls = int(rolls)
#         limit = int(limit)
#         plus = int(plus)
#         judge_limit = int(judge_limit)
        
#         result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#         mappedData = map(int, result.split(","))
#         output = list(mappedData)
#         sumresult = sum(output)
#         sumresult = sumresult + plus
#             if sumresult < judge_limit:
#                 sumresult = f"{str(sumresult)} < {str(judge_limit)} => 成功"
#             elif sumresult >= judge_limit :
#                 sumresult = f"{str(sumresult)} >= {str(judge_limit)} => 失敗"
#             else:
#                 sumresult = sumresult
#                 return
#         return
    

#     msg = f"{ctx.author.mention}\n" + sumresult
#     await ctx.send(msg)


# class JapaneseHelpCommand(commands.DefaultHelpCommand):
#   def __init__(self):
#        super().__init__()
#        self.commands_heading = "コマンド:"
#        self.no_category = "その他"
#        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

#    def get_ending_note(self):
#        return (f"各コマンドの説明: $help <コマンド名>\n"
#                f"各カテゴリの説明: $help <カテゴリ名>\n")



bot.run(token)

