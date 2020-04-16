import os
import re
import traceback
import random
import discord

from discord.ext import commands as rta


bot = rta.Bot(command_prefix='!')#, help_command=JapaneseHelpCommand()

token = os.environ['DISCORD_BOT_TOKEN']

# #Lenz
# STR_0864 = 14
# DEX_0864 = 14
# INT_0864 = 13
# CON_0864 = 14
# APP_0864 = 10
# POW_0864 = 11
# SIZ_0864 = 10
# SAN_0864 = 55
# EDU_0864 = 15
# HP_0864 = 12
# #rta
# STR_0191 = 12
# DEX_0191 = 12
# INT_0191 = 11
# CON_0191 = 7
# APP_0191 = 7
# POW_0191 = 11
# SIZ_0191 = 12
# SAN_0191 = 55
# EDU_0191 = 9
# HP_0191 = 9
# #extra
# STR_8199 = 18
# DEX_8199 = 13
# INT_8199 = 14
# CON_8199 = 11
# APP_8199 = 10
# POW_8199 = 6
# SIZ_8199 = 13
# SAN_8199 = 30
# EDU_8199 = 18
# HP_8199 = 12
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

    
HP_0864 = 10
HP_0191 = 12
HP_8199 = 11
MP_0864 = 12
MP_0191 = 15
MP_8199 = 14
SA_0864 = 59
SA_0191 = 75
SA_8199 = 70







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

    
@bot.command(name="h")
async def dice(ctx: str):
    """!h 短縮help"""
    embed = discord.Embed(title="Help",description="各種コマンドの説明を行います。",color=discord.Colour.from_rgb(0,0,100))
    embed.add_field(name="!d",value="!d {n}d{n}の書式で入力\n合計値のみ表示",inline=False)
    embed.add_field(name="!dice",value="!dice {n}d{n}の書式で入力\n配列表示あり",inline=False)
    embed.add_field(name="!dj",value="!dj {n}d{n}<kの書式で入力",inline=False)
    embed.add_field(name="!dp",value="!dj {n}d{n}+kの書式で入力",inline=False)
    embed.add_field(name="!p",value="!p {states}+{N}の書式で入力\nkeeperは!p {id}&{states}+{N}の書式で入力\n{id}は各playerの#以降\nステータスの表示は!p s",inline=False)
    embed.add_field(name="!m",value="!m {states}-{N}の書式で入力\nkeeperは!m {id}&{states}-{N}の書式で入力\n{id}は各playerの#以降\nステータスの表示は!m s",inline=False)
    embed.add_field(name="!h",value="これを表示",inline=False)
    embed.add_field(name="id",value="小沼さん\n0864\n\n六谷さん\n0191\n\n羅闇さん\n8199",inline=False)

    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 

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


    

@bot.command(name="p")
async def s0864(ctx,stu: str):
    """!p {states}+{N}の書式で入力    ステータスの加算を行います。    ただし、keeperは{id}&{states}+{N}と入力してください。    {id}は    小沼さん:0864    六谷さん:0191    羅闇さん:8199"""
    global HP_0864
    global MP_0864
    global SA_0864
    global HP_0191
    global MP_0191
    global SA_0191
    global HP_8199
    global MP_8199
    global SA_8199
    
    a_id = ctx.author.id
    if a_id == 294106055397474314:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の滝口 明夫のステータスを表示します。"
            msg = f"滝口 明夫\n耐久値 {HP_0864}/10. MP {MP_0864}/12. 正気度 {SA_0864}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        plus = int(plus)
        if states == "hp":
            hp = HP_0864 + plus
            HP_0864 = hp
            msg1 = f"HPを+{plus}しました。"
        elif states == "mp":
            mp = MP_0864 + plus
            MP_0864 = mp
            msg1 = f"MPを+{plus}しました。"
        elif states == "san":
            san = SA_0864 + plus
            SA_0864 = san
            msg1 = f"SANを+{plus}しました。"
        an = f"現在の滝口 明夫のステータスを表示します。"
        msg = f"滝口 明夫\n耐久値 {HP_0864}/10. MP {MP_0864}/12. 正気度 {SA_0864}/99."
    elif a_id == 649984563292012545:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の苑田 晋助のステータスを表示します。"
            msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        plus = int(plus)
        if states == "hp":
            hp = HP_0191 + plus
            HP_0191 = hp
            msg1 = f"HPを+{plus}しました。"
        elif states == "mp":
            mp = MP_0191 + plus
            MP_0191 = mp
            msg1 = f"MPを+{plus}しました。"
        elif states == "san":
            san = SA_0191 + plus
            SA_0191 = san
            msg1 = f"SANを+{plus}しました。"
        an = f"現在の苑田 晋助のステータスを表示します。"
        msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
    elif a_id == 452095387990229002:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の鈴木 耕一のステータスを表示します。"
            msg = f"鈴木 耕一\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        plus = int(plus)
        if states == "hp":
            hp = HP_8199 + plus
            HP_8199 = hp
            msg1 = f"HPを+{plus}しました。"
        elif states == "mp":
            mp = MP_8199 + plus
            MP_8199 = mp
            msg1 = f"MPを+{plus}しました。"
        elif states == "san":
            san = SA_8199 + plus
            SA_8199 = san
            msg1 = f"SANを+{plus}しました。"
        an = f"現在の鈴木 耕一のステータスを表示します。"
        msg = f"鈴木 耕一\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."

    elif a_id == 556772231011631104:
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, plus = map(str, str1.split('+'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"滝口 明夫\n耐久力 {HP_0864}/10. MP {MP_0864}/12.  正気度 {SA_0864}/99.\n\n鈴木 耕一\n耐久力 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99.\n\n苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        plus = int(plus)
        if pl_di == "0864":
            if states == "hp":
                hp = HP_0864 + plus
                HP_0864 = hp
                msg1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_0864 + plus
                MP_0864 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_0864 + plus
                SA_0864 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の滝口 明夫のステータスを表示します。"
            msg = f"滝口 明夫\n耐久値 {HP_0864}/10. MP {MP_0864}/12. 正気度 {SA_0864}/99."
        elif pl_di == "0191":
            if states == "hp":
                hp = HP_0191 + plus
                HP_0191 = hp
                ms2g1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_0191 + plus
                MP_0191 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_0191 + plus
                SA_0191 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の苑田 晋助のステータスを表示します。"
            msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
        elif pl_di == "8199":
            if states == "hp":
                hp = HP_8199 + plus
                HP_8199 = hp
                msg1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_8199 + plus
                MP_8199 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_8199 + plus
                SA_8199 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の鈴木 耕一のステータスを表示します。"
            msg = f"鈴木 耕一\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."

    elif a_id == 406447479622729728:
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, plus = map(str, str1.split('+'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"滝口 明夫\n耐久力 {HP_0864}/10. MP {MP_0864}/12.  正気度 {SA_0864}/99.\n\n鈴木 耕一\n耐久力 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99.\n\n苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        plus = int(plus)
        if pl_di == "0864":
            if states == "hp":
                hp = HP_0864 + plus
                HP_0864 = hp
                msg1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_0864 + plus
                MP_0864 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_0864 + plus
                SA_0864 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の滝口 明夫のステータスを表示します。"
            msg = f"滝口 明夫\n耐久値 {HP_0864}/10. MP {MP_0864}/12. 正気度 {SA_0864}/99."
        elif pl_di == "0191":
            if states == "hp":
                hp = HP_0191 + plus
                HP_0191 = hp
                msg1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_0191 + plus
                MP_0191 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_0191 + plus
                SA_0191 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の苑田 晋助のステータスを表示します。"
            msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
        elif pl_di == "8199":
            if states == "hp":
                hp = HP_8199 + plus
                HP_8199 = hp
                msg1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_8199 + plus
                MP_8199 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_8199 + plus
                SA_8199 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の鈴木 耕一のステータスを表示します。"
            msg = f"鈴木 耕一\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."
            
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 

    

@bot.command(name="m")
async def s0864(ctx,stu: str):
    """!p {states}-{N}の書式で入力    ステータスの加算を行います。    ただし、keeperは{id}&{states}-{N}と入力してください。    {id}は    小沼さん:0864    六谷さん:0191    羅闇さん:8199"""
    global HP_0864
    global MP_0864
    global SA_0864
    global HP_0191
    global MP_0191
    global SA_0191
    global HP_8199
    global MP_8199
    global SA_8199
    
    a_id = ctx.author.id
    if a_id == 294106055397474314:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の滝口 明夫のステータスを表示します。"
            msg = f"滝口 明夫\n耐久値 {HP_0864}/10. MP {MP_0864}/12. 正気度 {SA_0864}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        minus = int(minus)
        if states == "hp":
            hp = HP_0864 - minus
            HP_0864 = hp
            msg1 = f"HPを-{minus}しました。"
        elif states == "mp":
            mp = MP_0864 - minus
            MP_0864 = mp
            msg1 = f"MPを-{minus}しました。"
        elif states == "san":
            san = SA_0864 - minus
            SA_0864 = san
            msg1 = f"SANを-{minus}しました。"
        an = f"現在の滝口 明夫のステータスを表示します。"
        msg = f"滝口 明夫\n耐久値 {HP_0864}/10. MP {MP_0864}/12. 正気度 {SA_0864}/99."
    elif a_id == 649984563292012545:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の苑田 晋助のステータスを表示します。"
            msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        minus = int(minus)
        if states == "hp":
            hp = HP_0191 - minus
            HP_0191 = hp
            msg1 = f"HPを-{minus}しました。"
        elif states == "mp":
            mp = MP_0191 - minus
            MP_0191 = mp
            msg1 = f"MPを-{minus}しました。"
        elif states == "san":
            san = SA_0191 - minus
            SA_0191 = san
            msg1 = f"SANを-{minus}しました。"
        an = f"現在の苑田 晋助のステータスを表示します。"
        msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
    elif a_id == 452095387990229002:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の鈴木 耕一のステータスを表示します。"
            msg = f"鈴木 耕一\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        minus = int(minus)
        if states == "hp":
            hp = HP_8199 - minus
            HP_8199 = hp
            msg1 = f"HPを-{minus}しました。"
        elif states == "mp":
            mp = MP_8199 - minus
            MP_8199 = mp
            msg1 = f"MPを-{minus}しました。"
        elif states == "san":
            san = SA_8199 - minus
            SA_8199 = san
            msg1 = f"SANを-{minus}しました。"
        an = f"現在の鈴木 耕一のステータスを表示します。"
        msg = f"鈴木 耕一\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."

    elif a_id == 556772231011631104:
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, minus = map(str, str1.split('-'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"滝口 明夫\n耐久力 {HP_0864}/10. MP {MP_0864}/12.  正気度 {SA_0864}/99.\n\n鈴木 耕一\n耐久力 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99.\n\n苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        minus = int(minus)
        if pl_di == "0864":
            if states == "hp":
                hp = HP_0864 - minus
                HP_0864 = hp
                msg1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_0864 - minus
                MP_0864 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_0864 - minus
                SA_0864 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の滝口 明夫のステータスを表示します。"
            msg = f"滝口 明夫\n耐久値 {HP_0864}/10. MP {MP_0864}/12. 正気度 {SA_0864}/99."
        elif pl_di == "0191":
            if states == "hp":
                hp = HP_0191 - minus
                HP_0191 = hp
                ms2g1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_0191 - minus
                MP_0191 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_0191 - minus
                SA_0191 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の苑田 晋助のステータスを表示します。"
            msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
        elif pl_di == "8199":
            if states == "hp":
                hp = HP_8199 - minus
                HP_8199 = hp
                msg1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_8199 - minus
                MP_8199 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_8199 - minus
                SA_8199 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の鈴木 耕一のステータスを表示します。"
            msg = f"鈴木 耕一\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."

    elif a_id == 406447479622729728:
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, minus = map(str, str1.split('-'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"滝口 明夫\n耐久力 {HP_0864}/10. MP {MP_0864}/12.  正気度 {SA_0864}/99.\n\n鈴木 耕一\n耐久力 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99.\n\n苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        minus = int(minus)
        if pl_di == "0864":
            if states == "hp":
                hp = HP_0864 - minus
                HP_0864 = hp
                msg1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_0864 - minus
                MP_0864 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_0864 - minus
                SA_0864 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の滝口 明夫のステータスを表示します。"
            msg = f"滝口 明夫\n耐久値 {HP_0864}/10. MP {MP_0864}/12. 正気度 {SA_0864}/99."
        elif pl_di == "0191":
            if states == "hp":
                hp = HP_0191 - minus
                HP_0191 = hp
                msg1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_0191 - minus
                MP_0191 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_0191 - minus
                SA_0191 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の苑田 晋助のステータスを表示します。"
            msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
        elif pl_di == "8199":
            if states == "hp":
                hp = HP_8199 - minus
                HP_8199 = hp
                msg1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_8199 - minus
                MP_8199 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_8199 - minus
                SA_8199 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の鈴木 耕一のステータスを表示します。"
            msg = f"鈴木 耕一\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."
            
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 
    
# @bot.command(name="l")
# async def l(ctx: str):
#     """!l(エル)の書式で入力 小沼さん"""
#     global HP_0864
#     global MP_0864
#     global SA_0864

#     msg = f"滝口 明夫\n耐久力 {HP_0864}/12. MP {MP_0864}/11.  正気度 {SA_0864}/99."
#     await ctx.send(msg)
    
# @bot.command(name="e")
# async def e(ctx: str):
#     """!eの書式で入力 羅闇さん"""
#     global HP_8199
#     global MP_8199
#     global SA_8199

#     msg = f"鈴木 耕一\n耐久力 {HP_8199}/12. MP {MP_8199}/11.  正気度 {SA_8199}/99."
#     await ctx.send(msg)

# @bot.command(name="r")
# async def r(ctx: str):
#     """!rの書式で入力 六谷さん"""
#     global HP_0191
#     global MP_0191
#     global SA_0191

#     msg = f"苑田 晋助\n耐久力 {HP_0191}/12. MP {MP_0191}/11.  正気度 {SA_0191}/99."
#     await ctx.send(msg)
    
# @bot.command(name="kp")
# async def k(ctx: str):
#     """!kの書式で入力 keeper用"""
#     global HP_0864
#     global MP_0864
#     global SA_0864
#     global HP_0191
#     global MP_0191
#     global SA_0191
#     global HP_8199
#     global MP_8199
#     global SA_8199


#     msg = f"滝口 明夫\n耐久力 {HP_0864}/12. MP {MP_0864}/11.  正気度 {SA_0864}/99.\n\n鈴木 耕一\n耐久力 {HP_8199}/16. MP {MP_8199}/6. 正気度 {SA_8199}/99.\n\n苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/11. 正気度 {SA_0191}/99."

#     await ctx.send(msg)
    
    
# @bot.command(name="rp")
# async def rp(ctx, stu: str):
#     """!rp {states}+{N}の書式で入力"""
#     global HP_0191
#     global MP_0191
#     global SA_0191
    
#     states, plus = map(str, stu.split('+'))
#     plus = int(plus)
#     if states == "hp":
#         hp = HP_0191 + plus
#         HP_0191 = hp
#         msg1 = f"HPを+{plus}しました。"
#     elif states == "mp":
#         mp = MP_0191 + plus
#         MP_0191 = mp
#         msg1 = f"MPを+{plus}しました。"
#     elif states == "san":
#         san = SA_0191 + plus
#         SA_0191 = san
#         msg1 = f"SANを+{plus}しました。"
#     an = f"現在の苑田 晋助を表示します。"
#     msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/11. 正気度 {SA_0191}/99."
#     mention= f"<@{ctx.author.id}>"
#     embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
# #     embed.set_author(name=firesult)
#     await ctx.send(f"{ctx.author.mention}")
#     await ctx.send(embed=embed)

# @bot.command(name="rm")
# async def rm(ctx, stu: str):
#     """!rm {states}-{N}の書式で入力"""
#     global HP_0191
#     global MP_0191
#     global SA_0191
    
#     states, minus = map(str, stu.split('-'))
#     minus = int(minus)
#     if states == "hp":
#         hp = HP_0191 - minus
#         HP_0191 = hp
#         msg1 = f"HPを-{minus}しました。"
#     elif states == "mp":
#         mp = MP_0191 - minus
#         MP_0191 = mp
#         msg1 = f"MPを-{minus}しました。"
#     elif states == "san":
#         san = SA_0191 - minus
#         SA_0191 = san
#         msg1 = f"SANを-{minus}しました。"
#     an = f"現在の苑田 晋助のステータスを表示します。"
#     msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/11. 正気度 {SA_0191}/99."
#     mention= f"<@{ctx.author.id}>"
#     embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
# #     embed.set_author(name=firesult)
#     await ctx.send(f"{ctx.author.mention}")
#     await ctx.send(embed=embed)

# @bot.command(name="ep")
# async def ep(ctx, stu: str):
#     """!ep {states}+{N}の書式で入力"""
#     global HP_8199
#     global MP_8199
#     global SA_8199
    
#     states, plus = map(str, stu.split('+'))
#     plus = int(plus)
#     if states == "hp":
#         hp = HP_8199 + plus
#         HP_8199 = hp
#         msg1 = f"HPを+{plus}しました。"
#     elif states == "mp":
#         mp = MP_8199 + plus
#         MP_8199 = mp
#         msg1 = f"MPを+{plus}しました。"
#     elif states == "san":
#         san = SA_8199 + plus
#         SA_8199 = san
#         msg1 = f"SANを+{plus}しました。"
#     an = f"現在の鈴木 耕一のステータスを表示します。"
#     msg = f"鈴木 耕一\n耐久値 {HP_8199}/16. MP {MP_8199}/6. 正気度 {SA_8199}/99."
#     mention= f"<@{ctx.author.id}>"
#     embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
# #     embed.set_author(name=firesult)
#     await ctx.send(f"{ctx.author.mention}")
#     await ctx.send(embed=embed)

# @bot.command(name="em")
# async def em(ctx, stu: str):
#     """!em {states}-{N}の書式で入力"""
#     global HP_8199
#     global MP_8199
#     global SA_8199
    
#     states, minus = map(str, stu.split('-'))
#     minus = int(minus)
#     if states == "hp":
#         hp = HP_8199 - minus
#         HP_8199 = hp
#         msg1 = f"HPを-{minus}しました。"
#     elif states == "mp":
#         mp = MP_8199 - minus
#         MP_8199 = mp
#         msg1 = f"MPを-{minus}しました。"
#     elif states == "san":
#         san = SA_8199 - minus
#         SA_8199 = san
#         msg1 = f"SANを-{minus}しました。"
#     an = f"現在の鈴木 耕一のステータスを表示します。"
#     msg = f"鈴木 耕一\n耐久値 {HP_8199}/16. MP {MP_8199}/6. 正気度 {SA_8199}/99."
#     mention= f"<@{ctx.author.id}>"
#     embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
# #     embed.set_author(name=firesult)
#     await ctx.send(f"{ctx.author.mention}")
#     await ctx.send(embed=embed)


# @bot.command(name="lp")
# async def lp(ctx, stu: str):
#     """!lp {states}+{N}の書式で入力"""
#     global HP_0864
#     global MP_0864
#     global SA_0864
    
#     states, plus = map(str, stu.split('+'))
#     plus = int(plus)
#     if states == "hp":
#         hp = HP_0864 + plus
#         HP_0864 = hp
#         msg1 = f"HPを+{plus}しました。"
#     elif states == "mp":
#         mp = MP_0864 + plus
#         MP_0864 = mp
#         msg1 = f"MPを+{plus}しました。"
#     elif states == "san":
#         san = SA_0864 + plus
#         SA_0864 = san
#         msg1 = f"SANを+{plus}しました。"
#     an = f"現在の滝口 明夫のステータスを表示します。"
#     msg = f"滝口 明夫\n耐久値 {HP_0864}/12. MP {MP_0864}/11. 正気度 {SA_0864}/99."
#     mention= f"<@{ctx.author.id}>"
#     embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
# #     embed.set_author(name=firesult)
#     await ctx.send(f"{ctx.author.mention}")
#     await ctx.send(embed=embed)

# @bot.command(name="lm")
# async def lm(ctx, stu: str):
#     """!lm {states}-{N}の書式で入力"""
#     global HP_0864
#     global MP_0864
#     global SA_0864
    
#     states, minus = map(str, stu.split('-'))
#     minus = int(minus)
#     if states == "hp":
#         hp = HP_0864 - minus
#         HP_0864 = hp
#         msg1 = f"HPを-{minus}しました。"
#     elif states == "mp":
#         mp = MP_0864 - minus
#         MP_0864 = mp
#         msg1 = f"MPを-{minus}しました。"
#     elif states == "san":
#         san = SA_0864 - minus
#         SA_0864 = san
#         msg1 = f"SANを-{minus}しました。"
#     an = f"現在の滝口 明夫のステータスを表示します。"
#     msg = f"滝口 明夫\n耐久値 {HP_0864}/12. MP {MP_0864}/11. 正気度 {SA_0864}/99."
#     mention= f"<@{ctx.author.id}>"
#     embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
# #     embed.set_author(name=firesult)
#     await ctx.send(f"{ctx.author.mention}")
#     await ctx.send(embed=embed)

    
    

# @bot.command(name="s")
# async def s0864(ctx,stu: str):

#     global HP_0864
#     global MP_0864
#     global SA_0864
#     global HP_0191
#     global MP_0191
#     global SA_0191
#     global HP_8199
#     global MP_8199
#     global SA_8199
    
    
#     if stu in "+":
#         status, plus = map(str, stu.split('+'))
#         plus = int(plus)
#         a_id = ctx.author.id
#         if a_id == 294106055397474314:
#             states, plus = map(str, stu.split('+'))
#             plus = int(plus)
#             if states == "hp":
#                 hp = HP_0864 + plus
#                 HP_0864 = hp
#                 msg1 = f"HPを+{plus}しました。"
#             elif states == "mp":
#                 mp = MP_0864 + plus
#                 MP_0864 = mp
#                 msg1 = f"MPを+{plus}しました。"
#             elif states == "san":
#                 san = SA_0864 + plus
#                 SA_0864 = san
#                 msg1 = f"SANを+{plus}しました。"
#             an = f"現在の滝口 明夫のステータスを表示します。"
#             msg = f"滝口 明夫\n耐久値 {HP_0864}/12. MP {MP_0864}/11. 正気度 {SA_0864}/99."
#             embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#             await ctx.send(f"{ctx.author.mention}")
#             await ctx.send(embed=embed) 
#         elif a_id == 649984563292012545:
#             states, plus = map(str, stu.split('+'))
#             plus = int(plus)
#             if states == "hp":
#                 hp = HP_0191 + plus
#                 HP_0191 = hp
#                 msg1 = f"HPを+{plus}しました。"
#             elif states == "mp":
#                 mp = MP_0191 + plus
#                 MP_0191 = mp
#                 msg1 = f"MPを+{plus}しました。"
#             elif states == "san":
#                 san = SA_0191 + plus
#                 SA_0191 = san
#                 msg1 = f"SANを+{plus}しました。"
#             an = f"現在の苑田 晋助を表示します。"
#             msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/11. 正気度 {SA_0191}/99."
#             embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#             await ctx.send(f"{ctx.author.mention}")
#             await ctx.send(embed=embed) 
#         elif a_id == 452095387990229002:
#             states, plus = map(str, stu.split('+'))
#             plus = int(plus)
#             if states == "hp":
#                 hp = HP_8199 + plus
#                 HP_8199 = hp
#                 msg1 = f"HPを+{plus}しました。"
#             elif states == "mp":
#                 mp = MP_8199 + plus
#                 MP_8199 = mp
#                 msg1 = f"MPを+{plus}しました。"
#             elif states == "san":
#                 san = SA_8199 + plus
#                 SA_8199 = san
#                 msg1 = f"SANを+{plus}しました。"
#             an = f"現在の鈴木 耕一のステータスを表示します。"
#             msg = f"鈴木 耕一\n耐久値 {HP_8199}/16. MP {MP_8199}/6. 正気度 {SA_8199}/99."
#             embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#             await ctx.send(f"{ctx.author.mention}")
#             await ctx.send(embed=embed)    
#         elif a_id == 556772231011631104:
#             pl_di, str1 = map(str, stu.split('&'))
#             states, plus = map(str, str1.split('+'))
#             plus = int(plus)
#             if pl_di == "0864":
#                 if states == "hp":
#                     hp = HP_0864 + plus
#                     HP_0864 = hp
#                     msg1 = f"HPを+{plus}しました。"
#                 elif states == "mp":
#                     mp = MP_0864 + plus
#                     MP_0864 = mp
#                     msg1 = f"MPを+{plus}しました。"
#                 elif states == "san":
#                     san = SA_0864 + plus
#                     SA_0864 = san
#                     msg1 = f"SANを+{plus}しました。"
#                 an = f"現在の滝口 明夫のステータスを表示します。"
#                 msg = f"滝口 明夫\n耐久値 {HP_0864}/12. MP {MP_0864}/11. 正気度 {SA_0864}/99."
#             elif pl_di == "0191":
#                 if states == "hp":
#                     hp = HP_0191 + plus
#                     HP_0191 = hp
#                     msg1 = f"HPを+{plus}しました。"
#                 elif states == "mp":
#                     mp = MP_0191 + plus
#                     MP_0191 = mp
#                     msg1 = f"MPを+{plus}しました。"
#                 elif states == "san":
#                     san = SA_0191 + plus
#                     SA_0191 = san
#                     msg1 = f"SANを+{plus}しました。"
#                 an = f"現在の苑田 晋助を表示します。"
#                 msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/11. 正気度 {SA_0191}/99."
#             elif pl_di == "8199":
#                 if states == "hp":
#                     hp = HP_8199 + plus
#                     HP_8199 = hp
#                     msg1 = f"HPを+{plus}しました。"
#                 elif states == "mp":
#                     mp = MP_8199 + plus
#                     MP_8199 = mp
#                     msg1 = f"MPを+{plus}しました。"
#                 elif states == "san":
#                     san = SA_8199 + plus
#                     SA_8199 = san
#                     msg1 = f"SANを+{plus}しました。"
#                 an =f"現在の鈴木 耕一のステータスを表示します。"
#                 msg = f"鈴木 耕一\n耐久値 {HP_8199}/16. MP {MP_8199}/6. 正気度 {SA_8199}/99."
        
#         an = an 
#         msg = msg
#     elif stu in "-":
#         status, minus = map(str, stu.split('-'))
#         minus = int(minus)
#         a_id = ctx.author.id
#         if a_id == 294106055397474314:
#             states, minus = map(str, stu.split('-'))
#             minus = int(minus)
#             if states == "hp":
#                 hp = HP_0864 - minus
#                 HP_0864 = hp
#                 msg1 = f"HPを-{minus}しました。"
#             elif states == "mp":
#                 mp = MP_0864 - minus
#                 MP_0864 = mp
#                 msg1 = f"MPを-{minus}しました。"
#             elif states == "san":
#                 san = SA_0864 - minus
#                 SA_0864 = san
#                 msg1 = f"SANを-{minus}しました。"
#             an = f"現在の滝口 明夫のステータスを表示します。"
#             msg = f"滝口 明夫\n耐久値 {HP_0864}/12. MP {MP_0864}/11. 正気度 {SA_0864}/99."
#             mbed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#             await ctx.send(f"{ctx.author.mention}")
#             await ctx.send(embed=embed) 
#         elif a_id == 649984563292012545:
#             states, minus = map(str, stu.split('-'))
#             minus = int(minus)
#             if states == "hp":
#                 hp = HP_0191 - minus
#                 HP_0191 = hp
#                 msg1 = f"HPを-{minus}しました。"
#             elif states == "mp":
#                 mp = MP_0191 - minus
#                 MP_0191 = mp
#                 msg1 = f"MPを-{minus}しました。"
#             elif states == "san":
#                 san = SA_0191 - minus
#                 SA_0191 = san
#                 msg1 = f"SANを-{minus}しました。"
#             an = f"現在の苑田 晋助を表示します。"
#             msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/11. 正気度 {SA_0191}/99."
#             embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#             await ctx.send(f"{ctx.author.mention}")
#             await ctx.send(embed=embed) 
#         elif a_id == 452095387990229002:
#             states, minus = map(str, stu.split('-'))
#             minus = int(minus)
#             if states == "hp":
#                 hp = HP_8199 - minus
#                 HP_8199 = hp
#                 msg1 = f"HPを-{minus}しました。"
#             elif states == "mp":
#                 mp = MP_8199 - minus
#                 MP_8199 = mp
#                 msg1 = f"MPを-{minus}しました。"
#             elif states == "san":
#                 san = SA_8199 - minus
#                 SA_8199 = san
#                 msg1 = f"SANを-{minus}しました。"
#             an = f"現在の鈴木 耕一のステータスを表示します。"
#             msg = f"鈴木 耕一\n耐久値 {HP_8199}/16. MP {MP_8199}/6. 正気度 {SA_8199}/99."
#             embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#             await ctx.send(f"{ctx.author.mention}")
#             await ctx.send(embed=embed) 
#         elif a_id == 556772231011631104:
#             pl_di, str1 = map(str, stu.split('&'))
#             states, minus = map(str, str1.split('-'))
#             minus = int(minus)
#             if pl_di == "0864":
#                 if states == "hp":
#                     hp = HP_0864 - minus
#                     HP_0864 = hp
#                     msg1 = f"HPを-{minus}しました。"
#                 elif states == "mp":
#                     mp = MP_0864 - minus
#                     MP_0864 = mp
#                     msg1 = f"MPを-{minus}しました。"
#                 elif states == "san":
#                     san = SA_0864 - minus
#                     SA_0864 = san
#                     msg1 = f"SANを-{minus}しました。"
#                 an = f"現在の滝口 明夫のステータスを表示します。"
#                 msg = f"滝口 明夫\n耐久値 {HP_0864}/12. MP {MP_0864}/11. 正気度 {SA_0864}/99."
#             elif pl_di == "0191":
#                 if states == "hp":
#                     hp = HP_0191 - minus
#                     HP_0191 = hp
#                     msg1 = f"HPを-{minus}しました。"
#                 elif states == "mp":
#                     mp = MP_0191 - minus
#                     MP_0191 = mp
#                     msg1 = f"MPを-{minus}しました。"
#                 elif states == "san":
#                     san = SA_0191 - minus
#                     SA_0191 = san
#                     msg1 = f"SANを-{minus}しました。"
#                 an = f"現在の苑田 晋助を表示します。"
#                 msg = f"苑田 晋助\n耐久値 {HP_0191}/12. MP {MP_0191}/11. 正気度 {SA_0191}/99."
#             elif pl_di == "8199":
#                 if states == "hp":
#                     hp = HP_8199 - minus
#                     HP_8199 = hp
#                     msg1 = f"HPを-{minus}しました。"
#                 elif states == "mp":
#                     mp = MP_8199 - minus
#                     MP_8199 = mp
#                     msg1 = f"MPを-{minus}しました。"
#                 elif states == "san":
#                     san = SA_8199 - minus
#                     SA_8199 = san
#                     msg1 = f"SANを-{minus}しました。"
#                 an =f"現在の鈴木 耕一のステータスを表示します。"
#                 msg = f"鈴木 耕一\n耐久値 {HP_8199}/16. MP {MP_8199}/6. 正気度 {SA_8199}/99."
#             embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(0,255,0))
#             await ctx.send(f"{ctx.author.mention}")
#             await ctx.send(embed=embed) 
 

# @bot.command(name="s0864")
# async def s0864(ctx: str):
#     global STR_0864
#     global DEX_0864
#     global INT_0864
#     global CON_0864
#     global APP_0864
#     global POW_0864
#     global SIZ_0864
#     global SAN_0864
#     global EDU_0864
#     global HP_0864
#     msg0 = f"STR:{STR_0864}\nDEX:{DEX_0864}\nINT:{INT_0864}\nCON:{CON_0864}\nAPP:{APP_0864}\nPOW:{POW_0864}\nSIZ:{SIZ_0864}\nSAN:{SAN_0864}\nEDU:{EDU_0864}\nHP:{HP_0864}"
#     await ctx.send(msg0)
    
# @bot.command(name="shp")
# async def s0864(ctx,stu: str):
#     global STR_0864
#     global DEX_0864
#     global INT_0864
#     global CON_0864
#     global APP_0864
#     global POW_0864
#     global SIZ_0864
#     global SAN_0864
#     global EDU_0864
#     global HP_0864
#     global HP_0191
#     global HP_8199  
#     status, plus = map(str, stu.split('+'))
#     plus = int(plus)
#     a_id = ctx.author.id
#     if a_id == 0864:
#         hp = HP_0864
#         HP_0864 = hp + plus
#         msg0 = f"STR:{STR_0864}\nDEX:{DEX_0864}\nINT:{INT_0864}\nCON:{CON_0864}\nAPP:{APP_0864}\nPOW:{POW_0864}\nSIZ:{SIZ_0864}\nSAN:{SAN_0864}\nEDU:{EDU_0864}\nHP:{HP_0864}"
#     elif a_id == 0191:
#         hp = HP_0191
#         HP_0191 = hp + plus
#         msg0 = f"STR:{STR_0191}\nDEX:{DEX_0191}\nINT:{INT_0191}\nCON:{CON_0191}\nAPP:{APP_0191}\nPOW:{POW_0191}\nSIZ:{SIZ_0191}\nSAN:{SAN_0191}\nEDU:{EDU_0191}\nHP:{HP_0191}"
#     elif a_id == 8199:
#         hp = HP_8199
#         HP_8199 = hp + plus
#         msg0 = f"STR:{STR_8199}\nDEX:{DEX_8199}\nINT:{INT_8199}\nCON:{CON_8199}\nAPP:{APP_8199}\nPOW:{POW_8199}\nSIZ:{SIZ_8199}\nSAN:{SAN_8199}\nEDU:{EDU_8199}\nHP:{HP_8199}"
#     await ctx.send(msg0)
    
    
# # @bot.command(name="sp0864")
# # async def sp0864(ctx, stu: str):
# #     global STR_0864
# #     global DEX_0864
# #     global INT_0864
# #     global CON_0864
# #     global APP_0864
# #     global POW_0864
# #     global SIZ_0864
# #     global SAN_0864
# #     global EDU_0864
# #     global HP_0864
# #     st = STR_0864
# #     dex = DEX_0864
# #     in =  INT_0864
# #     con = CON_0864
# #     app = APP_0864
# #     pw = POW_0864
# #     siz = SIZ_0864
# #     san = SAN_0864
# #     edu = EDU_0864
# #     hp = HP_0864
# #     status, plus = map(int, stu.split('+'))
# #     if status == 1:
# #         hp = hp + plus
# #         HP_0864 = hp
# #     else:
# #         HP_0864 = HP_0864
# #     msg0 = f"STR:{STR_0864}\nDEX:{DEX_0864}\nINT:{INT_0864}\nCON:{CON_0864}\nAPP:{APP_0864}\nPOW:{POW_0864}\nSIZ:{SIZ_0864}\nSAN:{SAN_0864}\nEDU:{EDU_0864}\nHP:{HP_0864}"
# #     await ctx.send(msg0)
    
# @bot.command(name="s0191")
# async def s0191(ctx: str):
#     global STR_0191
#     global DEX_0191
#     global INT_0191
#     global CON_0191
#     global APP_0191
#     global POW_0191
#     global SIZ_0191
#     global SAN_0191
#     global EDU_0191
#     global HP_0191
#     msg1 = f"STR:{STR_0191}\nDEX:{DEX_0191}\nINT:{INT_0191}\nCON:{CON_0191}\nAPP:{APP_0191}\nPOW:{POW_0191}\nSIZ:{SIZ_0191}\nSAN:{SAN_0191}\nEDU:{EDU_0191}\nHP:{HP_0191}"
#     await ctx.send(msg1)
 

# @bot.command(name="s8199")
# async def s8199(ctx: str):
#     global STR_8199
#     global DEX_8199
#     global INT_8199
#     global CON_8199
#     global APP_8199
#     global POW_8199
#     global SIZ_8199
#     global SAN_8199
#     global EDU_8199
#     global HP_8199
#     msg2 = f"STR:{STR_8199}\nDEX:{DEX_8199}\nINT:{INT_8199}\nCON:{CON_8199}\nAPP:{APP_8199}\nPOW:{POW_8199}\nSIZ:{SIZ_8199}\nSAN:{SAN_8199}\nEDU:{EDU_8199}\nHP:{HP_8199}"
#     await ctx.send(msg2)
 

#     global STR_0864
#     global DEX_0864
#     global INT_0864
#     global CON_0864
#     global APP_0864
#     global POW_0864
#     global SIZ_0864
#     global SAN_0864
#     global EDU_0864
#     global HP_0864

#     global STR_0191
#     global DEX_0191
#     global INT_0191
#     global CON_0191
#     global APP_0191
#     global POW_0191
#     global SIZ_0191
#     global SAN_0191
#     global EDU_0191
#     global HP_0191

#     global STR_8199
#     global DEX_8199
#     global INT_8199
#     global CON_8199
#     global APP_8199
#     global POW_8199
#     global SIZ_8199
#     global SAN_8199
#     global EDU_8199
#     global HP_8199
 
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
#     if (ctx.author.id == 0864):  
# 	msg0 = f"STR:{STR_0864}\nDEX:{DEX_0864}\nINT:{INT_0864}\nCON:{CON_0864}\nAPP:{APP_0864}\nPOW:{POW_0864}\nSIZ:{SIZ_0864}\nSAN:{SAN_0864}\nEDU:{EDU_0864}\nHP:{HP_0864}"
#         await ctx.send(msg0)
#     elif (ctx.author.id == 0191):
#         msg1 = f"STR:{STR_0191}\nDEX:{DEX_0191}\nINT:{INT_0191}\nCON:{CON_0191}\nAPP:{APP_0191}\nPOW:{POW_0191}\nSIZ:{SIZ_0191}\nSAN:{SAN_0191}\nEDU:{EDU_0191}\nHP:{HP_0191}"
#         await ctx.send(msg1)
#     elif (ctx.author.id == 8199):      
#         msg2 = f"STR:{STR_8199}\nDEX:{DEX_8199}\nINT:{INT_8199}\nCON:{CON_8199}\nAPP:{APP_8199}\nPOW:{POW_8199}\nSIZ:{SIZ_8199}\nSAN:{SAN_8199}\nEDU:{EDU_8199}\nHP:{HP_8199}"
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

