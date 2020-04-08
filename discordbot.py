import os
import re
import traceback
import random
import discord

from discord.ext import commands as rta


bot = rta.Bot(command_prefix='!')#, help_command=JapaneseHelpCommand()

token = os.environ['DISCORD_BOT_TOKEN']

# def has_any_role():
#     async def predicate(ctx):
#         if len(ctx.author.roles) > 1:
#             return True
#     return commands.check(predicate)

#Lenz
STR_4176 = 14
DEX_4176 = 14
INT_4176 = 13
CON_4176 = 14
APP_4176 = 10
POW_4176 = 11
SIZ_4176 = 10
SAN_4176 = 55
EDU_4176 = 15
HP_4176 = 12
#rta
STR_4091 = 12
DEX_4091 = 12
INT_4091 = 11
CON_4091 = 7
APP_4091 = 7
POW_4091 = 11
SIZ_4091 = 12
SAN_4091 = 55
EDU_4091 = 9
HP_4091 = 9
#extra
STR_4560 = 18
DEX_4560 = 13
INT_4560 = 14
CON_4560 = 11
APP_4560 = 10
POW_4560 = 6
SIZ_4560 = 13
SAN_4560 = 30
EDU_4560 = 18
HP_4560 = 12
#konuma
STR_864 = 18
DEX_864 = 13
INT_864 = 14
CON_864 = 11
APP_864 = 10
POW_864 = 6
SIZ_864 = 13
SAN_864 = 30
EDU_864 = 18
HP_864 = 12

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    


@bot.command(name="d")
async def d(ctx, dice: str):
    """!d {n}d{n}の書式で入力(合計表示のみ)"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('!d NdNの書式で入力')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    mappedData = map(int, result.split(","))
    output = list(mappedData)
    sumresult = sum(output)
    msg = f"{ctx.author.mention}\n{sumresult}"
    await ctx.send(msg)


    
@bot.command(name="dice")
async def dice(ctx, dice: str):
    """!dice {n}d{n}の書式で入力"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('!dice NdNの書式で入力')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    mappedData = map(int, result.split(","))
    output = list(mappedData)
    sumresult = sum(output)
    mention= f"<@{ctx.author.id}>"
    embed = discord.Embed(title=sumresult ,description=f"{ctx.author.mention}\n{ctx.message.content}",color=discord.Colour.from_rgb(255,0,0))
    embed.set_author(name=result)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

@bot.command(name="dp")
async def dp(ctx, dice: str):
    """!dp {n}d{n}+kの書式で入力"""
    rolls, str1 = map(str, dice.split('d'))
    limit, plus =map(int, str1.split('+'))

    rolls = int(rolls)
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    mappedData = map(int, result.split(","))
    output = list(mappedData)
    sumresult = sum(output)
    firesult = sumresult + plus
    mention= f"<@{ctx.author.id}>"
    msg = f"{ctx.author.mention}\n" + result
    msg2 = f"{firesult} = {sumresult} + {plus}"
    embed = discord.Embed(title=firesult ,description=f"{mention}\n{result}\n{sumresult}\n{msg2}\n{ctx.message.content}",color=discord.Colour.from_rgb(255,0,0))
#     embed.set_author(name=firesult)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

    
@bot.command(name="dj")
async def dj(ctx, dice: str):
    """!dj {n}d{n}<kの書式で入力"""
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
    mention= f"<@{ctx.author.id}>"
    if sumresult < judge:
        msg1 = f"{sumresult} < {judge} => 成功"
    else:
        msg1 = f"{sumresult} < {judge} => 失敗"

    msg = f"{ctx.author.mention}\n" + result
    embed = discord.Embed(title=msg1 ,description=f"{mention}\n{result}\n{sumresult}\n{ctx.message.content}",color=discord.Colour.from_rgb(255,0,0))
#     embed.set_author(name=msg1)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

    
@bot.command(name="s")
async def s(ctx: str):
#     nonlocal STR_4176
#     nonlocal DEX_4176
#     nonlocal INT_4176
#     nonlocal CON_4176
#     nonlocal APP_4176
#     nonlocal POW_4176
#     nonlocal SIZ_4176
#     nonlocal SAN_4176
#     nonlocal EDU_4176
#     nonlocal HP_4176
#     nonlocal STR_4091
#     nonlocal DEX_4091
#     nonlocal INT_4091
#     nonlocal CON_4091
#     nonlocal APP_4091
#     nonlocal POW_4091
#     nonlocal SIZ_4091
#     nonlocal SAN_4091
#     nonlocal EDU_4091
#     nonlocal HP_4091
#     nonlocal STR_4091
#     nonlocal DEX_4091
#     nonlocal INT_4091
#     nonlocal CON_4091
#     nonlocal APP_4091
#     nonlocal POW_4091
#     nonlocal SIZ_4091
#     nonlocal SAN_4091
#     nonlocal EDU_4091
#     nonlocal HP_4091
#     nonlocal STR_4176
#     nonlocal DEX_4176
#     nonlocal INT_4176
#     nonlocal CON_4176
#     nonlocal APP_4176
#     nonlocal POW_4176
#     nonlocal SIZ_4176
#     nonlocal SAN_4176
#     nonlocal EDU_4176
#     nonlocal HP_4176  
#     nonlocal STR_864
#     nonlocal DEX_864
#     nonlocal INT_864
#     nonlocal CON_864
#     nonlocal APP_864
#     nonlocal POW_864
#     nonlocal SIZ_864
#     nonlocal SAN_864
#     nonlocal EDU_864
#     nonlocal HP_864
    if (ctx.author.id == 4176):  
	msg0 = f"STR:{STR_4176}\nDEX:{DEX_4176}\nINT:{INT_4176}\nCON:{CON_4176}\nAPP:{APP_4176}\nPOW:{POW_4176}\nSIZ:{SIZ_4176}\nSAN:{SAN_4176}\nEDU:{EDU_4176}\nHP:{HP_4176}"
        await ctx.send(msg0)
    elif (ctx.author.id == 4091):
        msg1 = f"STR:{STR_4091}\nDEX:{DEX_4091}\nINT:{INT_4091}\nCON:{CON_4091}\nAPP:{APP_4091}\nPOW:{POW_4091}\nSIZ:{SIZ_4091}\nSAN:{SAN_4091}\nEDU:{EDU_4091}\nHP:{HP_4091}"
        await ctx.send(msg1)
    elif (ctx.author.id == 4560):      
        msg2 = f"STR:{STR_4560}\nDEX:{DEX_4560}\nINT:{INT_4560}\nCON:{CON_4560}\nAPP:{APP_4560}\nPOW:{POW_4560}\nSIZ:{SIZ_4560}\nSAN:{SAN_4560}\nEDU:{EDU_4560}\nHP:{HP_4560}"
        await ctx.send(msg2)
    elif (ctx.author.id == 864):
        msg3 = f"STR:{STR_864}\nDEX:{DEX_864}\nINT:{INT_864}\nCON:{CON_864}\nAPP:{APP_864}\nPOW:{POW_864}\nSIZ:{SIZ_864}\nSAN:{SAN_864}\nEDU:{EDU_864}\nHP:{HP_864}"
        await ctx.send(msg3)
    else:
	return

# @bot.command(aliases=['cnt'])
# @has_any_role()
# async def count(self, ctx, num: typing.Optional[int] = 0):
#     if num == 0:
#         await ctx.send("引数を正しく入力してください")
#         return

#     msg = await ctx.send(f"{ctx.author.mention}\nリアクション集計を行います: 目標リアクション数 ** {num} **\n本メッセージにリアクションをつけてください")
#     today = datetime.today()
#     now = (today + timedelta(minutes=num)
#            ).strftime('%Y-%m-%d %H:%M:%S')
#     self.reaction_dict[str(msg.id)] = {
#         "cnt": num,
#         "author": ctx.author.mention,
#         "reaction_sum": 0,
#         "channel": ctx.channel.id,
#         "matte": 0,
#         "time": now,
#         "url": ctx.message.jump_url}
#     self.dump_json(self.reaction_dict)

# @bot.command(aliases=['ls'])
# @has_any_role()
# async def list_data(self, ctx):
#     if len(self.reaction_dict) == 0:
#         await ctx.send("集計中のリアクションはありません")
#     else:
#         embed = discord.Embed(
#             title="集計中のリアクションは以下の通りです",
#             description=f"{len(self.reaction_dict)}件集計中",
#             color=0xffffff)

#         for num, i in enumerate(self.reaction_dict):
#             auth = self.reaction_dict[i]["author"]
#             time = self.reaction_dict[i]["time"]
#             url = self.reaction_dict[i]["url"]
#             reaction_sum = self.reaction_dict[i]["reaction_sum"]
#             reaction_cnt = self.reaction_dict[i]["cnt"]

#             if self.reaction_dict[i]["matte"] > 0:
#                 matte = " **待って！**"
#             else:
#                 matte = ""

#             embed.add_field(
#                 name=f"{num+1}番目",
#                 value=f"ID : {i} by : {auth} time : {time} prog : {reaction_sum}/{reaction_cnt}{matte}\n{url}",
#                 inline=False)
#         embed.set_footer(text="あんまり貯めないでね")
#         await ctx.send(embed=embed)

# @bot.Cog.listener()
# async def on_raw_reaction_add(self, reaction):
#     for msg_id in list(self.reaction_dict):
#         if int(msg_id) == reaction.message_id:
#             if "matte" in reaction.emoji.name:
#                 self.reaction_dict[msg_id]["matte"] += 1
#                 channel = self.bot.get_channel(reaction.channel_id)
#                 msg = await channel.fetch_message(reaction.message_id)
#                 await msg.edit(content=msg.content + "\n待ちます")
#             else:
#                 self.reaction_dict[msg_id]["reaction_sum"] += 1

#             await self.judge_and_notice(msg_id)

# @bot.Cog.listener()
# async def on_raw_reaction_remove(self, reaction):
#     for msg_id in list(self.reaction_dict):
#         if int(msg_id) == reaction.message_id:
#             if "matte" in reaction.emoji.name:
#                 self.reaction_dict[msg_id]["matte"] -= 1
#                 channel = self.bot.get_channel(reaction.channel_id)
#                 msg = await channel.fetch_message(reaction.message_id)
#                 await msg.edit(content=msg.content.replace("\n待ちます", "", 1))
#             else:
#                 self.reaction_dict[msg_id]["reaction_sum"] -= 1

#             await self.judge_and_notice(msg_id)

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

