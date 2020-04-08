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
4176_STR = 14
4176_DEX = 14
4176_INT = 13
4176_CON = 14
4176_APP = 10
4176_POW = 11
4176_SIZ = 10
4176_SAN = 55
4176_EDU = 15
4176_HP = 12
# #rta
# 4091_STR = 12
# 4091_DEX = 12
# 4091_INT = 11
# 4091_CON = 7
# 4091_APP = 7
# 4091_POW = 11
# 4091_SIZ = 12
# 4091_SAN = 55
# 4091_EDU = 9
# 4091_HP = 9
# #extra
# 4560_STR = 18
# 4560_DEX = 13
# 4560_INT = 14
# 4560_CON = 11
# 4560_APP = 10
# 4560_POW = 6
# 4560_SIZ = 13
# 4560_SAN = 30
# 4560_EDU = 18
# 4560_HP = 12
# #konuma
# 864_STR = 18
# 864_DEX = 13
# 864_INT = 14
# 864_CON = 11
# 864_APP = 10
# 864_POW = 6
# 864_SIZ = 13
# 864_SAN = 30
# 864_EDU = 18
# 864_HP = 12

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
async def s(ctx, sta: str):
#     if message.author.id == 4176:
#         msg = f"STR:{4176_STR}\nDEX:{4176_DEX}\nINT:{4176_INT}\nCON:{4176_CON}\nAPP:{4176_APP}\nPOW:{4176_POW}\nSIZ:{4176_SIZ}\nSAN:{4176_SAN}\nEDU:{4176_EDU}\nHP:{4176_HP}"
#     elif message.author.id == 4091:
#         msg = f"STR:{4091_STR}\nDEX:{4091_DEX}\nINT:{4091_INT}\nCON:{4091_CON}\nAPP:{4091_APP}\nPOW:{4091_POW}\nSIZ:{4091_SIZ}\nSAN:{4091_SAN}\nEDU:{4091_EDU}\nHP:{4091_HP}"
#     elif message.author.id == 4560:
#         msg = f"STR:{4560_STR}\nDEX:{4560_DEX}\nINT:{4560_INT}\nCON:{4560_CON}\nAPP:{4560_APP}\nPOW:{4560_POW}\nSIZ:{4560_SIZ}\nSAN:{4560_SAN}\nEDU:{4560_EDU}\nHP:{4560_HP}"
#     elif message.author.id == 864:
#         msg = f"STR:{864_STR}\nDEX:{864_DEX}\nINT:{864_INT}\nCON:{864_CON}\nAPP:{864_APP}\nPOW:{864_POW}\nSIZ:{864_SIZ}\nSAN:{864_SAN}\nEDU:{864_EDU}\nHP:{864_HP}"
    msg = f"STR:{4176_STR}\nDEX:{4176_DEX}\nINT:{4176_INT}\nCON:{4176_CON}\nAPP:{4176_APP}\nPOW:{4176_POW}\nSIZ:{4176_SIZ}\nSAN:{4176_SAN}\nEDU:{4176_EDU}\nHP:{4176_HP}"
    await ctx.send(msg)


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

