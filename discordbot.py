import os
import re
import traceback
import random
import discord

from discord.ext import commands as rta


bot = rta.Bot(command_prefix='!')#, help_command=JapaneseHelpCommand()

token = os.environ['DISCORD_BOT_TOKEN']

# #Lenz
# STR_4176 = 14
# DEX_4176 = 14
# INT_4176 = 13
# CON_4176 = 14
# APP_4176 = 10
# POW_4176 = 11
# SIZ_4176 = 10
# SAN_4176 = 55
# EDU_4176 = 15
# HP_4176 = 12
# #rta
# STR_4091 = 12
# DEX_4091 = 12
# INT_4091 = 11
# CON_4091 = 7
# APP_4091 = 7
# POW_4091 = 11
# SIZ_4091 = 12
# SAN_4091 = 55
# EDU_4091 = 9
# HP_4091 = 9
# #extra
# STR_4560 = 18
# DEX_4560 = 13
# INT_4560 = 14
# CON_4560 = 11
# APP_4560 = 10
# POW_4560 = 6
# SIZ_4560 = 13
# SAN_4560 = 30
# EDU_4560 = 18
# HP_4560 = 12
# #konuma
# STR_864 = 18
# DEX_864 = 13
# INT_864 = 14
# CON_864 = 11
# APP_864 = 10
# POW_864 = 6
# SIZ_864 = 13
# SAN_864 = 30
# EDU_864 = 18
# HP_864 = 12

    
HP_4176 = 12
HP_4091 = 11
HP_4560 = 55
MP_4176 = 16
MP_4091 = 6
MP_4560 = 30
SA_4176 = 12
SA_4091 = 11
SA_4560 = 55







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


    


    
@bot.command(name="l")
async def l(ctx: str):
    """!l(エル)の書式で入力:Lens"""
    global HP_4176
    global MP_4176
    global SA_4176

    msg = f"トイ=ウォーターズ(パイロット)\n耐久力 {HP_4176}/12. MP {MP_4176}/11.  正気度 {SA_4176}/99."
    await ctx.send(msg)
    
@bot.command(name="e")
async def e(ctx: str):
    """!eの書式で入力:extra"""
    global HP_4560
    global MP_4560
    global SA_4560

    msg = f"ケビン=アンダーソン(スポーツ選手)\n耐久力 {HP_4560}/12. MP {MP_4560}/11.  正気度 {SA_4560}/99."
    await ctx.send(msg)

@bot.command(name="r")
async def r(ctx: str):
    """!rの書式で入力:rta"""
    global HP_4091
    global MP_4091
    global SA_4091

    msg = f"ルイ＝ビール(警官)\n耐久力 {HP_4091}/12. MP {MP_4091}/11.  正気度 {SA_4091}/99."
    await ctx.send(msg)
    
@bot.command(name="k")
async def k(ctx,stu: str):
    """!kの書式で入力:konuma"""
    global HP_4176
    global MP_4176
    global SA_4176
    global HP_4091
    global MP_4091
    global SA_4091
    global HP_4560
    global MP_4560
    global SA_4560


    msg = f"トイ=ウォーターズ(パイロット)\n耐久力 {HP_4176}/12. MP {MP_4176}/11.  正気度 {SA_4176}/99.\n\nケビン=アンダーソン(スポーツ選手)\n耐久力 {HP_4560}/16. MP {MP_4560}/6. 正気度 {SA_4560}/99.\n\nルイ＝ビール(警官)\n耐久値 {HP_4091}/12. MP {MP_4091}/11. 正気度 {SA_4091}/99."

    await ctx.send(msg)
    
    
@bot.command(name="rp")
async def rp(ctx, stu: str):
    """!rp {states}+{N}の書式で入力"""
    global HP_4091
    global MP_4091
    global SA_4091
    
    states, plus = map(str, stu.split('+'))
    plus = int(plus)
    if states == "hp":
        hp = HP_4091 + plus
        HP_4091 = hp
        msg1 = f"HPを+{plus}しました。"
    elif states == "mp":
        mp = MP_4091 + plus
        MP_4091 = mp
        msg1 = f"MPを+{plus}しました。"
    elif states == "san":
        san = SA_4091 + plus
        SA_4091 == san
        msg1 = f"SANを+{plus}しました。"
    an = f"現在のルイ＝ビールのステータスを表示します。"
    msg = f"ルイ＝ビール(警官)\n耐久値 {HP_4091}/12. MP {MP_4091}/11. 正気度 {SA_4091}/99."
    mention= f"<@{ctx.author.id}>"
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#     embed.set_author(name=firesult)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

@bot.command(name="rm")
async def rm(ctx, stu: str):
    """!rm {states}-{N}の書式で入力"""
    global HP_4091
    global MP_4091
    global SA_4091
    
    states, minus = map(str, stu.split('-'))
    minus = int(minus)
    if states == "hp":
        hp = HP_4091 - minus
        HP_4091 = hp
        msg1 = f"HPを-{minus}しました。"
    elif states == "mp":
        mp = MP_4091 - minus
        MP_4091 = mp
        msg1 = f"MPを-{minus}しました。"
    elif states == "san":
        san = SA_4091 - minus
        SA_4091 == san
        msg1 = f"SANを-{minus}しました。"
    an = f"現在のルイ＝ビールのステータスを表示します。"
    msg = f"ルイ＝ビール(警官)\n耐久値 {HP_4091}/12. MP {MP_4091}/11. 正気度 {SA_4091}/99."
    mention= f"<@{ctx.author.id}>"
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#     embed.set_author(name=firesult)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

@bot.command(name="ep")
async def ep(ctx, stu: str):
    """!ep {states}+{N}の書式で入力"""
    global HP_4560
    global MP_4560
    global SA_4560
    
    states, plus = map(str, stu.split('+'))
    plus = int(plus)
    if states == "hp":
        hp = HP_4560 + plus
        HP_4560 = hp
        msg1 = f"HPを+{plus}しました。"
    elif states == "mp":
        mp = MP_4560 + plus
        MP_4560 = mp
        msg1 = f"MPを+{plus}しました。"
    elif states == "san":
        san = SA_4560 + plus
        SA_4560 == san
        msg1 = f"SANを+{plus}しました。"
    an = f"現在のケビン=アンダーソンのステータスを表示します。"
    msg = f"ケビン=アンダーソン(スポーツ選手)\n耐久値 {HP_4560}/16. MP {MP_4560}/6. 正気度 {SA_4560}/99."
    mention= f"<@{ctx.author.id}>"
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#     embed.set_author(name=firesult)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

@bot.command(name="em")
async def em(ctx, stu: str):
    """!em {states}-{N}の書式で入力"""
    global HP_4560
    global MP_4560
    global SA_4560
    
    states, minus = map(str, stu.split('-'))
    minus = int(minus)
    if states == "hp":
        hp = HP_4560 - minus
        HP_4560 = hp
        msg1 = f"HPを-{minus}しました。"
    elif states == "mp":
        mp = MP_4560 - minus
        MP_4560 = mp
        msg1 = f"MPを-{minus}しました。"
    elif states == "san":
        san = SA_4560 - minus
        SA_4560 == san
        msg1 = f"SANを-{minus}しました。"
    an = f"現在のケビン=アンダーソンのステータスを表示します。"
    msg = f"ケビン=アンダーソン(スポーツ選手)\n耐久値 {HP_4560}/16. MP {MP_4560}/6. 正気度 {SA_4560}/99." mention= f"<@{ctx.author.id}>"
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#     embed.set_author(name=firesult)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)


@bot.command(name="lp")
async def lp(ctx, stu: str):
    """!lp {states}+{N}の書式で入力"""
    global HP_4176
    global MP_4176
    global SA_4176
    
    states, plus = map(str, stu.split('+'))
    plus = int(plus)
    if states == "hp":
        hp = HP_4176 + plus
        HP_4176 = hp
        msg1 = f"HPを+{plus}しました。"
    elif states == "mp":
        mp = MP_4176 + plus
        MP_4176 = mp
        msg1 = f"MPを+{plus}しました。"
    elif states == "san":
        san = SA_4176 + plus
        SA_4176 == san
        msg1 = f"SANを+{plus}しました。"
    an = f"現在のトイ=ウォーターズのステータスを表示します。"
    msg = f"トイ=ウォーターズ(パイロット)\n耐久値 {HP_4176}/12. MP {MP_4176}/11. 正気度 {SA_4176}/99."
    mention= f"<@{ctx.author.id}>"
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#     embed.set_author(name=firesult)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

@bot.command(name="lm")
async def lm(ctx, stu: str):
    """!lm {states}-{N}の書式で入力"""
    global HP_4176
    global MP_4176
    global SA_4176
    
    states, minus = map(str, stu.split('-'))
    minus = int(minus)
    if states == "hp":
        hp = HP_4176 - minus
        HP_4176 = hp
        msg1 = f"HPを-{minus}しました。"
    elif states == "mp":
        mp = MP_4176 - minus
        MP_4176 = mp
        msg1 = f"MPを-{minus}しました。"
    elif states == "san":
        san = SA_4176 - minus
        SA_4176 == san
        msg1 = f"SANを-{minus}しました。"
    an = f"現在のトイ=ウォーターズのステータスを表示します。"
    msg = f"トイ=ウォーターズ(パイロット)\n耐久値 {HP_4176}/12. MP {MP_4176}/11. 正気度 {SA_4176}/99."    mention= f"<@{ctx.author.id}>"
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#     embed.set_author(name=firesult)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

# @bot.command(name="s4176")
# async def s4176(ctx: str):
#     global STR_4176
#     global DEX_4176
#     global INT_4176
#     global CON_4176
#     global APP_4176
#     global POW_4176
#     global SIZ_4176
#     global SAN_4176
#     global EDU_4176
#     global HP_4176
#     msg0 = f"STR:{STR_4176}\nDEX:{DEX_4176}\nINT:{INT_4176}\nCON:{CON_4176}\nAPP:{APP_4176}\nPOW:{POW_4176}\nSIZ:{SIZ_4176}\nSAN:{SAN_4176}\nEDU:{EDU_4176}\nHP:{HP_4176}"
#     await ctx.send(msg0)
    
# @bot.command(name="shp")
# async def s4176(ctx,stu: str):
#     global STR_4176
#     global DEX_4176
#     global INT_4176
#     global CON_4176
#     global APP_4176
#     global POW_4176
#     global SIZ_4176
#     global SAN_4176
#     global EDU_4176
#     global HP_4176
#     global HP_4091
#     global HP_4560  
#     status, plus = map(str, stu.split('+'))
#     plus = int(plus)
#     a_id = ctx.author.id
#     if a_id == 4176:
#         hp = HP_4176
#         HP_4176 = hp + plus
#         msg0 = f"STR:{STR_4176}\nDEX:{DEX_4176}\nINT:{INT_4176}\nCON:{CON_4176}\nAPP:{APP_4176}\nPOW:{POW_4176}\nSIZ:{SIZ_4176}\nSAN:{SAN_4176}\nEDU:{EDU_4176}\nHP:{HP_4176}"
#     elif a_id == 4091:
#         hp = HP_4091
#         HP_4091 = hp + plus
#         msg0 = f"STR:{STR_4091}\nDEX:{DEX_4091}\nINT:{INT_4091}\nCON:{CON_4091}\nAPP:{APP_4091}\nPOW:{POW_4091}\nSIZ:{SIZ_4091}\nSAN:{SAN_4091}\nEDU:{EDU_4091}\nHP:{HP_4091}"
#     elif a_id == 4560:
#         hp = HP_4560
#         HP_4560 = hp + plus
#         msg0 = f"STR:{STR_4560}\nDEX:{DEX_4560}\nINT:{INT_4560}\nCON:{CON_4560}\nAPP:{APP_4560}\nPOW:{POW_4560}\nSIZ:{SIZ_4560}\nSAN:{SAN_4560}\nEDU:{EDU_4560}\nHP:{HP_4560}"
#     await ctx.send(msg0)
    
    
# # @bot.command(name="sp4176")
# # async def sp4176(ctx, stu: str):
# #     global STR_4176
# #     global DEX_4176
# #     global INT_4176
# #     global CON_4176
# #     global APP_4176
# #     global POW_4176
# #     global SIZ_4176
# #     global SAN_4176
# #     global EDU_4176
# #     global HP_4176
# #     st = STR_4176
# #     dex = DEX_4176
# #     in =  INT_4176
# #     con = CON_4176
# #     app = APP_4176
# #     pw = POW_4176
# #     siz = SIZ_4176
# #     san = SAN_4176
# #     edu = EDU_4176
# #     hp = HP_4176
# #     status, plus = map(int, stu.split('+'))
# #     if status == 1:
# #         hp = hp + plus
# #         HP_4176 = hp
# #     else:
# #         HP_4176 = HP_4176
# #     msg0 = f"STR:{STR_4176}\nDEX:{DEX_4176}\nINT:{INT_4176}\nCON:{CON_4176}\nAPP:{APP_4176}\nPOW:{POW_4176}\nSIZ:{SIZ_4176}\nSAN:{SAN_4176}\nEDU:{EDU_4176}\nHP:{HP_4176}"
# #     await ctx.send(msg0)
    
# @bot.command(name="s4091")
# async def s4091(ctx: str):
#     global STR_4091
#     global DEX_4091
#     global INT_4091
#     global CON_4091
#     global APP_4091
#     global POW_4091
#     global SIZ_4091
#     global SAN_4091
#     global EDU_4091
#     global HP_4091
#     msg1 = f"STR:{STR_4091}\nDEX:{DEX_4091}\nINT:{INT_4091}\nCON:{CON_4091}\nAPP:{APP_4091}\nPOW:{POW_4091}\nSIZ:{SIZ_4091}\nSAN:{SAN_4091}\nEDU:{EDU_4091}\nHP:{HP_4091}"
#     await ctx.send(msg1)
 

# @bot.command(name="s4560")
# async def s4560(ctx: str):
#     global STR_4560
#     global DEX_4560
#     global INT_4560
#     global CON_4560
#     global APP_4560
#     global POW_4560
#     global SIZ_4560
#     global SAN_4560
#     global EDU_4560
#     global HP_4560
#     msg2 = f"STR:{STR_4560}\nDEX:{DEX_4560}\nINT:{INT_4560}\nCON:{CON_4560}\nAPP:{APP_4560}\nPOW:{POW_4560}\nSIZ:{SIZ_4560}\nSAN:{SAN_4560}\nEDU:{EDU_4560}\nHP:{HP_4560}"
#     await ctx.send(msg2)
 

#     global STR_4176
#     global DEX_4176
#     global INT_4176
#     global CON_4176
#     global APP_4176
#     global POW_4176
#     global SIZ_4176
#     global SAN_4176
#     global EDU_4176
#     global HP_4176

#     global STR_4091
#     global DEX_4091
#     global INT_4091
#     global CON_4091
#     global APP_4091
#     global POW_4091
#     global SIZ_4091
#     global SAN_4091
#     global EDU_4091
#     global HP_4091

#     global STR_4560
#     global DEX_4560
#     global INT_4560
#     global CON_4560
#     global APP_4560
#     global POW_4560
#     global SIZ_4560
#     global SAN_4560
#     global EDU_4560
#     global HP_4560
 
#     global STR_864
#     global DEX_864
#     global INT_864
#     global CON_864
#     global APP_864
#     global POW_864
#     global SIZ_864
#     global SAN_864
#     global EDU_864
#     global HP_864
#     if (ctx.author.id == 4176):  
# 	msg0 = f"STR:{STR_4176}\nDEX:{DEX_4176}\nINT:{INT_4176}\nCON:{CON_4176}\nAPP:{APP_4176}\nPOW:{POW_4176}\nSIZ:{SIZ_4176}\nSAN:{SAN_4176}\nEDU:{EDU_4176}\nHP:{HP_4176}"
#         await ctx.send(msg0)
#     elif (ctx.author.id == 4091):
#         msg1 = f"STR:{STR_4091}\nDEX:{DEX_4091}\nINT:{INT_4091}\nCON:{CON_4091}\nAPP:{APP_4091}\nPOW:{POW_4091}\nSIZ:{SIZ_4091}\nSAN:{SAN_4091}\nEDU:{EDU_4091}\nHP:{HP_4091}"
#         await ctx.send(msg1)
#     elif (ctx.author.id == 4560):      
#         msg2 = f"STR:{STR_4560}\nDEX:{DEX_4560}\nINT:{INT_4560}\nCON:{CON_4560}\nAPP:{APP_4560}\nPOW:{POW_4560}\nSIZ:{SIZ_4560}\nSAN:{SAN_4560}\nEDU:{EDU_4560}\nHP:{HP_4560}"
#         await ctx.send(msg2)
#     elif (ctx.author.id == 0864):
#         msg3 = f"STR:{STR_864}\nDEX:{DEX_864}\nINT:{INT_864}\nCON:{CON_864}\nAPP:{APP_864}\nPOW:{POW_864}\nSIZ:{SIZ_864}\nSAN:{SAN_864}\nEDU:{EDU_864}\nHP:{HP_864}"
#         await ctx.send(msg3)
#     else:
# 	return

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

