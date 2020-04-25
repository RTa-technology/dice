import os
import re
import traceback
import random
import discord

from discord.ext import commands as rta


bot = rta.Bot(command_prefix='!')#, help_command=JapaneseHelpCommand()

token = os.environ['DISCORD_BOT_TOKEN']

#===============================================#
#===============================================#
#ID_data________________________________________#

ID_0864 = 294106055397474314 #konuma
ID_4091 = 556772231011631104 #rta
ID_4560 = 572765257630744596 #extra
ID_7568 = 283272953104302080 #raisu
ID_8199 = 452095387990229002 #raan
ID_4176 = 406447479622729728 #lenz
ID_8464 = 402072860832563228 #hanahana
ID_9995 = 603378477852524545 #nununu
ID_0191 = 649984563292012545 #rokutani

#===============================================#
#===============================================#
#Player_data____________________________________#

HP_0191 = 13
MP_0191 = 12
SA_0191 = 60

MP_8199 = 12
HP_8199 = 16
SA_8199 = 30

MP_7568 = 13
HP_7568 = 6
SA_7568 = 75

MP_9995 = 9
HP_9995 = 8
SA_9995 = 40

MP_8464 = 9
HP_8464 = 16
SA_8464 = 80

# ===============================================#

    # id_0191
a_1 = 28 #回避
a_2 = 45 #心理学
a_3 = 60 #博物学
a_4 = 20 #隠れる
a_5 = 55 #鍵開け
a_6 = 50 #運転
a_7 = 60 #信用
a_8 = 40 #ライフル

    # id_7568
b_1 = 65 #回避
b_2 = 70 #こぶし
b_3 = 65 #隠れる
b_4 = 70 #聞き耳
b_5 = 65 #忍び歩き
b_6 = 44 #目星
b_7 = 70 #言いくるめ

    # id_8199
c_1 = 61 #鍵開け
c_2 = 75 #拳銃
c_3 = 74 #回避
c_4 = 71 #コンピューター
c_5 = 65 #忍び歩き
c_6 = 71 #変装
c_7 = 70 #目星
c_8 = 65 #隠れる

    # id_8464
d_1 = 36 #回避
d_2 = 50 #キック
d_3 = 65 #こぶし
d_4 = 50 #応急手当
d_5 = 40 #聞き耳
d_6 = 60 #写真術
d_7 = 40 #追跡
d_8 = 55 #図書館
d_9 = 50 #乗馬
d_10 = 45 #説得
d_11 = 60 #英語
d_12 = 50 #オカルト
d_13 = 70 #心理学
d_14 = 31 #人類学
d_15 = 50 #歴史

    # ie_9995
e_1 = 50 #応急手当
e_2 = 40 #機械修理
e_3 = 40 #重機機械操作
e_4 = 26 #回避
e_5 = 40 #製作
e_6 = 40 #追跡
e_7 = 40 #電気修理
e_8 = 50 #博物学
e_9 = 61 #目星
e_10 = 15 #化学
e_11 = 55 #生物学
e_12 = 47 #図書館
e_13 = 65 #キック




#===============================================#

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
#===============================================#

@bot.command(name="sushi")
async def sushi(ctx: str):
    embed=discord.Embed(title="すし刃",description="それは寿司の魂の衝突です。\n高尾はクラスDの人物で、世界で最高のスシブレダーになることを目指し、現在もトレーニングを続けています。\n彼は運命という渦に巻き込まれ、ダークスシとの戦いに身を投じます。彼は本当にDark Sushiを倒し、Sushi bladeの平和を取り戻すことができますか?\n\n風船🎈", color=0xffffff)
    await ctx.send(embed=embed)

@bot.command(name="evil")
async def evil(ctx: str):
    embed=discord.Embed(title="evilFoundation-安全です。含む。支配する。",description="私たちは、財団が不必要に邪悪になることをできるだけ避けようとしていると信じていました。\n私たちは、人類が光の中に住み続けることができるように、暗闇の中で戦う人々として彼らを説明しました。\nしかし、この宇宙の財団は彼らの目的を達成するためのあらゆる手段を追求し、彼らの進歩を高めるために何かを犠牲にします。\n\nmary0228", color=0xff0000)
    await ctx.send(embed=embed)

@bot.command(name="odss")
async def odss(ctx: str):
    embed=discord.Embed(title="この狭い日本では、正常性を維持する機関が動き回っています。", description="地表の下で政治とスパイ活動を行い、最後にのみ波を作成します。\n\nカラカロフ", color=0x80ff80)
    embed.set_author(name="〈役員、ドクター、ソルジャー、スピー〉")
    await ctx.send(embed=embed)

@bot.command(name="1998")
async def odss(ctx: str):
    embed=discord.Embed(title="98年初夏に発生したポーランドでの神格存在の降臨は、人類をクソ強くした。\n事件はまた次の事件を生む――WTCでの超常テロ、拡散する異常疾患、エトセトラエトセトラ...。\nそれでも、彼らはクソ強いので前へと進んでゆく。", description="クソ強いポーランドは明日、世界へ先駆けて新たな一歩を踏み出します。ヴェールの先へ、闇へ立ち向かうために。ポーランドよ、クソ強くあれ。\n\n「クソ強い初夏」―クソ強いアイランズマスター師匠より", color=0xffff00)
    embed.set_author(name="クソ強人類")
    await ctx.send(embed=embed)

#===============================================#

@bot.command(name="id")
async def dice(ctx: str):
    """!id ID表示"""
    embed = discord.Embed(title="Help ID",description="IDを表示します。",color=discord.Colour.from_rgb(0,0,100))
    embed.add_field(name="id",value="小沼さん\n0864\n\n六谷さん\n0191\n\n羅闇さん\n8199\n\nRTa\n4091\n\n来須さん\n7568\n\nLenzさん\n4176\n\nExtraさん\n4560\n\n花難破納さん\n8464\n\nぬぬぬさん\n9995")
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 

@bot.command(name="h")
async def dice(ctx: str):
    """!h 短縮help"""
    embed = discord.Embed(title="Help Command",description="各種コマンドの説明を行います。",color=discord.Colour.from_rgb(255,140,0))
    embed.add_field(name="!d",value="!d {n}d{n}の書式で入力\n合計値のみ表示",inline=False)
    embed.add_field(name="!dice",value="!dice {n}d{n}の書式で入力\n配列表示あり",inline=False)
    embed.add_field(name="!dj",value="!dj {n}d{n}<kの書式で入力",inline=False)
    embed.add_field(name="!dp",value="!dj {n}d{n}+kの書式で入力",inline=False)
    embed.add_field(name="!p",value="!p {states}+{N}の書式で入力\nステータスの表示は!p s",inline=False)
    embed.add_field(name="!m",value="!m {states}-{N}の書式で入力\nステータスの表示は!m s",inline=False)
    embed.add_field(name="!h",value="これを表示",inline=False)
    embed.add_field(name="---------------------------------",value="キーパーメニュー",inline=False)
    embed.add_field(name="!id",value="IDを表示",inline=False)
    embed.add_field(name="!p",value="!p {id}&{states}+{N}の書式で入力\n{id}は各playerの#以降\nステータスの表示は!p s",inline=False)
    embed.add_field(name="!m",value="!m {id}&{states}-{N}の書式で入力\n{id}は各playerの#以降\nステータスの表示は!m s",inline=False)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 

#===============================================#

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
    if sumresult <= judge:
        msg1 = f"{sumresult} <= {judge} => 成功"
    else:
        msg1 = f"{sumresult} > {judge} => 失敗"
    msg = f"{ctx.author.mention}\n" + result
    embed = discord.Embed(title=msg1 ,description=f"{mention}\n{result}\n{sumresult}\n{ctx.message.content}",color=discord.Colour.from_rgb(255,0,0))
#     embed.set_author(name=msg1)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

#===============================================#
@bot.command(name="p")
async def s0864(ctx,stu: str):
    """!p {states}+{N}の書式で入力 ステータスの加算を行います。"""
    global HP_9995
    global MP_9995
    global SA_9995
    
    global HP_0191
    global MP_0191
    global SA_0191
    
    global HP_8199
    global MP_8199
    global SA_8199
    
    global HP_7568
    global MP_7568
    global SA_7568
    
    global HP_8464
    global MP_8464
    global SA_8464
    
    a_id = ctx.author.id
    if a_id == ID_9995:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在のぬぬぬのステータスを表示します。"
            msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        plus = int(plus)
        if states == "hp":
            hp = HP_9995 + plus
            HP_9995 = hp
            msg1 = f"HPを+{plus}しました。"
        elif states == "mp":
            mp = MP_9995 + plus
            MP_9995 = mp
            msg1 = f"MPを+{plus}しました。"
        elif states == "san":
            san = SA_9995 + plus
            SA_9995 = san
            msg1 = f"SANを+{plus}しました。"
        an = f"現在のぬぬぬのステータスを表示します。"
        msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99."
    elif a_id == ID_0191:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の六谷潤のステータスを表示します。"
            msg = f"六谷潤\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
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
        an = f"現在の六谷潤のステータスを表示します。"
        msg = f"六谷潤\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
    elif a_id == ID_8199:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の羅闇のステータスを表示します。"
            msg = f"羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."
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
        an = f"現在の羅闇のステータスを表示します。"
        msg = f"羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."

    elif a_id == ID_7568:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の来須ましろのステータスを表示します。"
            msg = f"来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        plus = int(plus)
        if states == "hp":
            hp = HP_7568 + plus
            HP_7568 = hp
            msg1 = f"HPを+{plus}しました。"
        elif states == "mp":
            mp = MP_7568 + plus
            MP_7568 = mp
            msg1 = f"MPを+{plus}しました。"
        elif states == "san":
            san = SA_7568 + plus
            SA_7568 = san
            msg1 = f"SANを+{plus}しました。"
        an = f"現在の来須ましろのステータスを表示します。"
        msg = f"来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99."

    elif a_id == ID_8464:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の花難破納のステータスを表示します。"
            msg = f"花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        plus = int(plus)
        if states == "hp":
            hp = HP_8464 + plus
            HP_8464 = hp
            msg1 = f"HPを+{plus}しました。"
        elif states == "mp":
            mp = MP_8464 + plus
            MP_8464 = mp
            msg1 = f"MPを+{plus}しました。"
        elif states == "san":
            san = SA_8464 + plus
            SA_8464 = san
            msg1 = f"SANを+{plus}しました。"
        an = f"現在の花難破納のステータスを表示します。"
        msg = f"花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."

    elif a_id == ID_0864: #keeper
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, plus = map(str, str1.split('+'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99.\n\n六谷潤\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99.\n\n羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99.\n\n来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99.\n\n花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        plus = int(plus)
        if pl_di == "9995":
            if states == "hp":
                hp = HP_9995 + plus
                HP_9995 = hp
                msg1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_9995 + plus
                MP_9995 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_9995 + plus
                SA_9995 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在のぬぬぬのステータスを表示します。"
            msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99."
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
        elif pl_di == "7568":
            if states == "hp":
                hp = HP_7568 + plus
                HP_7568 = hp
                msg1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_7568 + plus
                MP_7568 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_7568 + plus
                SA_7568 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の来須ましろのステータスを表示します。"
            msg = f"来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99."
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
            an = f"現在の羅闇のステータスを表示します。"
            msg = f"羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."
        elif pl_di == "8464":
            if states == "hp":
                hp = HP_8464 + plus
                HP_8464 = hp
                msg1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_8464 + plus
                MP_8464 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_8464 + plus
                SA_8464 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の花難破納のステータスを表示します。"
            msg = f"花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."

    elif a_id == ID_4091: #admin
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, plus = map(str, str1.split('+'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99.\n\n六谷潤\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99.\n\n羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99.\n\n来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99.\n\n花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        plus = int(plus)
        if pl_di == "9995":
            if states == "hp":
                hp = HP_9995 + plus
                HP_9995 = hp
                msg1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_9995 + plus
                MP_9995 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_9995 + plus
                SA_9995 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在のぬぬぬのステータスを表示します。"
            msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99."
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
        elif pl_di == "7568":
            if states == "hp":
                hp = HP_7568 + plus
                HP_7568 = hp
                msg1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_7568 + plus
                MP_7568 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_7568 + plus
                SA_7568 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の来須ましろのステータスを表示します。"
            msg = f"来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99."
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
            an = f"現在の羅闇のステータスを表示します。"
            msg = f"羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."
        elif pl_di == "8464":
            if states == "hp":
                hp = HP_8464 + plus
                HP_8464 = hp
                msg1 = f"HPを+{plus}しました。"
            elif states == "mp":
                mp = MP_8464 + plus
                MP_8464 = mp
                msg1 = f"MPを+{plus}しました。"
            elif states == "san":
                san = SA_8464 + plus
                SA_8464 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の花難破納のステータスを表示します。"
            msg = f"花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."
            
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 

#===============================================#

@bot.command(name="m")
async def s0864(ctx,stu: str):
    """!m {states}-{N}の書式で入力 ステータスの加算を行います。"""
    global HP_9995
    global MP_9995
    global SA_9995
    
    global HP_0191
    global MP_0191
    global SA_0191
    
    global HP_8199
    global MP_8199
    global SA_8199
    
    global HP_7568
    global MP_7568
    global SA_7568
    
    global HP_8464
    global MP_8464
    global SA_8464
    
    a_id = ctx.author.id
    if a_id == ID_9995:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在のぬぬぬのステータスを表示します。"
            msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        minus = int(minus)
        if states == "hp":
            hp = HP_9995 - minus
            HP_9995 = hp
            msg1 = f"HPを-{minus}しました。"
        elif states == "mp":
            mp = MP_9995 - minus
            MP_9995 = mp
            msg1 = f"MPを-{minus}しました。"
        elif states == "san":
            san = SA_9995 - minus
            SA_9995 = san
            msg1 = f"SANを-{minus}しました。"
        an = f"現在のぬぬぬのステータスを表示します。"
        msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99."
    elif a_id == ID_0191:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の六谷潤のステータスを表示します。"
            msg = f"六谷潤\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
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
        an = f"現在の六谷潤のステータスを表示します。"
        msg = f"六谷潤\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99."
    elif a_id == ID_8199:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の羅闇のステータスを表示します。"
            msg = f"羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."
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
        an = f"現在の羅闇のステータスを表示します。"
        msg = f"羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."

    elif a_id == ID_7568:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の来須ましろのステータスを表示します。"
            msg = f"来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        minus = int(minus)
        if states == "hp":
            hp = HP_7568 - minus
            HP_7568 = hp
            msg1 = f"HPを-{minus}しました。"
        elif states == "mp":
            mp = MP_7568 - minus
            MP_7568 = mp
            msg1 = f"MPを-{minus}しました。"
        elif states == "san":
            san = SA_7568 - minus
            SA_7568 = san
            msg1 = f"SANを-{minus}しました。"
        an = f"現在の来須ましろのステータスを表示します。"
        msg = f"来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99."

    elif a_id == ID_8464:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の花難破納のステータスを表示します。"
            msg = f"花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        minus = int(minus)
        if states == "hp":
            hp = HP_8464 - minus
            HP_8464 = hp
            msg1 = f"HPを-{minus}しました。"
        elif states == "mp":
            mp = MP_8464 - minus
            MP_8464 = mp
            msg1 = f"MPを-{minus}しました。"
        elif states == "san":
            san = SA_8464 - minus
            SA_8464 = san
            msg1 = f"SANを-{minus}しました。"
        an = f"現在の花難破納のステータスを表示します。"
        msg = f"花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."

    elif a_id == ID_0864: #keeper
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, minus = map(str, str1.split('-'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99.\n\n六谷潤\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99.\n\n羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99.\n\n来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99.\n\n花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        minus = int(minus)
        if pl_di == "9995":
            if states == "hp":
                hp = HP_9995 - minus
                HP_9995 = hp
                msg1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_9995 - minus
                MP_9995 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_9995 - minus
                SA_9995 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在のぬぬぬのステータスを表示します。"
            msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99."
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
        elif pl_di == "7568":
            if states == "hp":
                hp = HP_7568 - minus
                HP_7568 = hp
                msg1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_7568 - minus
                MP_7568 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_7568 - minus
                SA_7568 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の来須ましろのステータスを表示します。"
            msg = f"来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99."
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
            an = f"現在の羅闇のステータスを表示します。"
            msg = f"羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."
        elif pl_di == "8464":
            if states == "hp":
                hp = HP_8464 - minus
                HP_8464 = hp
                msg1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_8464 - minus
                MP_8464 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_8464 - minus
                SA_8464 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の花難破納のステータスを表示します。"
            msg = f"花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."

    elif a_id == ID_4091: #admin
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, minus = map(str, str1.split('-'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99.\n\n六谷潤\n耐久値 {HP_0191}/12. MP {MP_0191}/15. 正気度 {SA_0191}/99.\n\n羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99.\n\n来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99.\n\n花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        minus = int(minus)
        if pl_di == "9995":
            if states == "hp":
                hp = HP_9995 - minus
                HP_9995 = hp
                msg1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_9995 - minus
                MP_9995 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_9995 - minus
                SA_9995 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在のぬぬぬのステータスを表示します。"
            msg = f"ぬぬぬ\n耐久値 {HP_9995}/10. MP {MP_9995}/12. 正気度 {SA_9995}/99."
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
        elif pl_di == "7568":
            if states == "hp":
                hp = HP_7568 - minus
                HP_7568 = hp
                msg1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_7568 - minus
                MP_7568 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_7568 - minus
                SA_7568 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の来須ましろのステータスを表示します。"
            msg = f"来須ましろ\n耐久値 {HP_7568}/11. MP {MP_7568}/14. 正気度 {SA_7568}/99."
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
            an = f"現在の羅闇のステータスを表示します。"
            msg = f"羅闇\n耐久値 {HP_8199}/11. MP {MP_8199}/14. 正気度 {SA_8199}/99."
        elif pl_di == "8464":
            if states == "hp":
                hp = HP_8464 - minus
                HP_8464 = hp
                msg1 = f"HPを-{minus}しました。"
            elif states == "mp":
                mp = MP_8464 - minus
                MP_8464 = mp
                msg1 = f"MPを-{minus}しました。"
            elif states == "san":
                san = SA_8464 - minus
                SA_8464 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の花難破納のステータスを表示します。"
            msg = f"花難破納\n耐久値 {HP_8464}/11. MP {MP_8464}/14. 正気度 {SA_8464}/99."
            
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 



@bot.command(name="j")
async def s0864(ctx,sk: str):
    """!j {技能}の書式で入力 技能の判定を行います。"""

    global a_1
    global a_2
    global a_3
    global a_4
    global a_5
    global a_6
    global a_7
    global a_8

    global b_1
    global b_2
    global b_3
    global a_4
    global a_5
    global a_6
    global a_7

    global c_1
    global c_2
    global c_3
    global c_4
    global c_5
    global c_6
    global c_7
    global c_8

    global d_1
    global d_2
    global d_3
    global d_4
    global d_5
    global d_6
    global d_7
    global d_8
    global d_9
    global d_10
    global d_11
    global d_12
    global d_13
    global d_14
    global d_15

    global e_1
    global e_2
    global e_3
    global e_4
    global e_5
    global e_6
    global e_7
    global e_8
    global e_9
    global e_10
    global e_11
    global e_12
    global e_13





    a_id = ctx.author.id
    if a_id == ID_0191:

        if sk == "回避":
            judge = a_1 
            
        elif sk == "心理学":
            judge = a_2

        elif sk == "博物学":
            judge = a_3

        elif sk == "隠れる":
            judge = a_4

        elif sk == "鍵開け":
            judge = a_5

        elif sk == "運転":
            judge = a_6

        elif sk == "信用":
            judge = a_7

        elif sk == "ライフル":
            judge = a_8

        result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        mappedData = map(int, result.split(","))
        output = list(mappedData)
        sumresult = sum(output)
        sumresult = int(sumresult)
        msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
        if sumresult <= judge:
            msg1 = f"{sumresult} <= {judge} => 成功"
        else:
            msg1 = f"{sumresult} > {judge} => 失敗"
        an = f"六谷潤の判定結果{sk}を表示します。"   

    elif a_id == ID_7568:
        if sk == "回避":
            judge = b_1 
            
        elif sk == "こぶし":
            judge = b_2

        elif sk == "隠れる":
            judge = b_3

        elif sk == "聞き耳":
            judge = b_4

        elif sk == "忍び歩き":
            judge = b_5

        elif sk == "目星":
            judge = b_6

        elif sk == "言いくるめ":
            judge = b_7

        result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        mappedData = map(int, result.split(","))
        output = list(mappedData)
        sumresult = sum(output)
        sumresult = int(sumresult)
        msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
        if sumresult <= judge:
            msg1 = f"{sumresult} <= {judge} => 成功"
        else:
            msg1 = f"{sumresult} > {judge} => 失敗"
        an = f"来須ましろの判定結果{sk}を表示します。"        

    elif a_id == ID_8199:
        if sk == "鍵開け":
            judge = c_1 
            
        elif sk == "拳銃":
            judge = c_2

        elif sk == "回避":
            judge = c_3

        elif sk == "コンピューター":
            judge = c_4

        elif sk == "忍び歩き":
            judge = c_5

        elif sk == "変装":
            judge = c_6

        elif sk == "目星":
            judge = c_7

        elif sk == "隠れる":
            judge = c_8

        result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        mappedData = map(int, result.split(","))
        output = list(mappedData)
        sumresult = sum(output)
        sumresult = int(sumresult)
        msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
        if sumresult <= judge:
            msg1 = f"{sumresult} <= {judge} => 成功"
        else:
            msg1 = f"{sumresult} > {judge} => 失敗"
        an = f"羅闇の判定結果{sk}を表示します。"        

    elif a_id == ID_8464:
        if sk == "回避":
            judge = d_1 
            
        elif sk == "キック":
            judge = d_2

        elif sk == "こぶし":
            judge = d_3

        elif sk == "応急手当":
            judge = d_4

        elif sk == "聞き耳":
            judge = d_5

        elif sk == "写真術":
            judge = d_6

        elif sk == "追跡":
            judge = d_7

        elif sk == "図書館":
            judge = d_8

        elif sk == "乗馬":
            judge = d_9

        elif sk == "説得":
            judge = d_10

        elif sk == "英語:
            judge = d_11

        elif sk == "オカルト":
            judge = d_12

        elif sk == "心理学":
            judge = d_13

        elif sk == "人類学":
            judge = d_14

        elif sk == "歴史":
            judge = d_15

        result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        mappedData = map(int, result.split(","))
        output = list(mappedData)
        sumresult = sum(output)
        sumresult = int(sumresult)
        msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
        if sumresult <= judge:
            msg1 = f"{sumresult} <= {judge} => 成功"
        else:
            msg1 = f"{sumresult} > {judge} => 失敗"
        an = f"花難破納の判定結果{sk}を表示します。"        

    elif a_id == ID_9995:
        if sk == "応急手当":
            judge = e_1 
            
        elif sk == "機械修理":
            judge = e_2

        elif sk == "重機械操作":
            judge = e_3

        elif sk == "回避":
            judge = e_4

        elif sk == "製作":
            judge = e_5

        elif sk == "追跡":
            judge = e_6

        elif sk == "電気修理":
            judge = e_7

        elif sk == "博物学":
            judge = e_8

        elif sk == "目星":
            judge = e_9

        elif sk == "化学":
            judge = e_10

        elif sk == "生物学:
            judge = e_11

        elif sk == "図書館":
            judge = e_12

        elif sk == "キック":
            judge = e_13

        result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        mappedData = map(int, result.split(","))
        output = list(mappedData)
        sumresult = sum(output)
        sumresult = int(sumresult)
        msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
        if sumresult <= judge:
            msg1 = f"{sumresult} <= {judge} => 成功"
        else:
            msg1 = f"{sumresult} > {judge} => 失敗"
        an = f"ぬぬぬの判定結果{sk}を表示します。"  

    elif a_id == ID_0864: #keeper
        try:
            pl_di, sk = map(str, sk.split('&'))
        except Exception:
            an = f"Error"
            msg = f"書式不一致\n!j ID&技能値"
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        if pl_di == "9995":
            if sk == "応急手当":
                judge = e_1 
            
            elif sk == "機械修理":
                judge = e_2

            elif sk == "重機械操作":
                judge = e_3

            elif sk == "回避":
                judge = e_4

            elif sk == "製作":
                judge = e_5

            elif sk == "追跡":
                judge = e_6

            elif sk == "電気修理":
                judge = e_7

            elif sk == "博物学":
                judge = e_8

            elif sk == "目星":
                judge = e_9

            elif sk == "化学":
                judge = e_10

            elif sk == "生物学:
                judge = e_11

            elif sk == "図書館":
                judge = e_12

            elif sk == "キック":
                judge = e_13

            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
            if sumresult <= judge:
                msg1 = f"{sumresult} <= {judge} => 成功"
            else:
                msg1 = f"{sumresult} > {judge} => 失敗"
            an = f"ぬぬぬの判定結果{sk}を表示します。"  

        elif pl_di == "0191":

            if sk == "回避":
                judge = a_1 
            
            elif sk == "心理学":
                judge = a_2

            elif sk == "博物学":
                judge = a_3

            elif sk == "隠れる":
                judge = a_4

            elif sk == "鍵開け":
                judge = a_5

            elif sk == "運転":
                judge = a_6

            elif sk == "信用":
                judge = a_7

            elif sk == "ライフル":
                judge = a_8

            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
            if sumresult <= judge:
                msg1 = f"{sumresult} <= {judge} => 成功"
            else:
                msg1 = f"{sumresult} > {judge} => 失敗"
            an = f"六谷潤の判定結果{sk}を表示します。" 
        elif pl_di == "7568":
            if sk == "回避":
                judge = b_1 
            
            elif sk == "こぶし":
                judge = b_2

            elif sk == "隠れる":
                judge = b_3

            elif sk == "聞き耳":
                judge = b_4

            elif sk == "忍び歩き":
                judge = b_5

            elif sk == "目星":
                judge = b_6

            elif sk == "言いくるめ":
                judge = b_7

            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
            if sumresult <= judge:
                msg1 = f"{sumresult} <= {judge} => 成功"
            else:
                msg1 = f"{sumresult} > {judge} => 失敗"
            an = f"来須ましろの判定結果{sk}を表示します。"       
        elif pl_di == "8199":
            if sk == "鍵開け":
                judge = c_1 
            
            elif sk == "拳銃":
                judge = c_2

            elif sk == "回避":
                judge = c_3

            elif sk == "コンピューター":
                judge = c_4

            elif sk == "忍び歩き":
                judge = c_5

            elif sk == "変装":
                judge = c_6

            elif sk == "目星":
                judge = c_7

            elif sk == "隠れる":
                judge = c_8

            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
            if sumresult <= judge:
                msg1 = f"{sumresult} <= {judge} => 成功"
            else:
                msg1 = f"{sumresult} > {judge} => 失敗"
            an = f"羅闇の判定結果{sk}を表示します。" 
        elif pl_di == "8464":
            if sk == "回避":
                judge = d_1 
            
            elif sk == "キック":
                judge = d_2

            elif sk == "こぶし":
                judge = d_3

            elif sk == "応急手当":
                judge = d_4

            elif sk == "聞き耳":
                judge = d_5

            elif sk == "写真術":
                judge = d_6

            elif sk == "追跡":
                judge = d_7

            elif sk == "図書館":
                judge = d_8

            elif sk == "乗馬":
                judge = d_9

            elif sk == "説得":
                judge = d_10

            elif sk == "英語:
                judge = d_11

            elif sk == "オカルト":
                judge = d_12

            elif sk == "心理学":
                judge = d_13

            elif sk == "人類学":
                judge = d_14

            elif sk == "歴史":
                judge = d_15

            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
            if sumresult <= judge:
                msg1 = f"{sumresult} <= {judge} => 成功"
            else:
                msg1 = f"{sumresult} > {judge} => 失敗"
            an = f"花難破納の判定結果{sk}を表示します。"   

    elif a_id == ID_4091: #admin
        try:
            pl_di, sk = map(str, sk.split('&'))
        except Exception:
            an = f"Error"
            msg = f"書式不一致\n!j ID&技能値"
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        if pl_di == "9995":
            if sk == "応急手当":
                judge = e_1 
            
            elif sk == "機械修理":
                judge = e_2

            elif sk == "重機械操作":
                judge = e_3

            elif sk == "回避":
                judge = e_4

            elif sk == "製作":
                judge = e_5

            elif sk == "追跡":
                judge = e_6

            elif sk == "電気修理":
                judge = e_7

            elif sk == "博物学":
                judge = e_8

            elif sk == "目星":
                judge = e_9

            elif sk == "化学":
                judge = e_10

            elif sk == "生物学:
                judge = e_11

            elif sk == "図書館":
                judge = e_12

            elif sk == "キック":
                judge = e_13

            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
            if sumresult <= judge:
                msg1 = f"{sumresult} <= {judge} => 成功"
            else:
                msg1 = f"{sumresult} > {judge} => 失敗"
            an = f"ぬぬぬの判定結果{sk}を表示します。"  

        elif pl_di == "0191":

            if sk == "回避":
                judge = a_1 
            
            elif sk == "心理学":
                judge = a_2

            elif sk == "博物学":
                judge = a_3

            elif sk == "隠れる":
                judge = a_4

            elif sk == "鍵開け":
                judge = a_5

            elif sk == "運転":
                judge = a_6

            elif sk == "信用":
                judge = a_7

            elif sk == "ライフル":
                judge = a_8

            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
            if sumresult <= judge:
                msg1 = f"{sumresult} <= {judge} => 成功"
            else:
                msg1 = f"{sumresult} > {judge} => 失敗"
            an = f"六谷潤の判定結果{sk}を表示します。" 
        elif pl_di == "7568":
            if sk == "回避":
                judge = b_1 
            
            elif sk == "こぶし":
                judge = b_2

            elif sk == "隠れる":
                judge = b_3

            elif sk == "聞き耳":
                judge = b_4

            elif sk == "忍び歩き":
                judge = b_5

            elif sk == "目星":
                judge = b_6

            elif sk == "言いくるめ":
                judge = b_7

            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
            if sumresult <= judge:
                msg1 = f"{sumresult} <= {judge} => 成功"
            else:
                msg1 = f"{sumresult} > {judge} => 失敗"
            an = f"来須ましろの判定結果{sk}を表示します。"       
        elif pl_di == "8199":
            if sk == "鍵開け":
                judge = c_1 
            
            elif sk == "拳銃":
                judge = c_2

            elif sk == "回避":
                judge = c_3

            elif sk == "コンピューター":
                judge = c_4

            elif sk == "忍び歩き":
                judge = c_5

            elif sk == "変装":
                judge = c_6

            elif sk == "目星":
                judge = c_7

            elif sk == "隠れる":
                judge = c_8

            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
            if sumresult <= judge:
                msg1 = f"{sumresult} <= {judge} => 成功"
            else:
                msg1 = f"{sumresult} > {judge} => 失敗"
            an = f"羅闇の判定結果{sk}を表示します。" 
        elif pl_di == "8464":
            if sk == "回避":
                judge = d_1 
            
            elif sk == "キック":
                judge = d_2

            elif sk == "こぶし":
                judge = d_3

            elif sk == "応急手当":
                judge = d_4

            elif sk == "聞き耳":
                judge = d_5

            elif sk == "写真術":
                judge = d_6

            elif sk == "追跡":
                judge = d_7

            elif sk == "図書館":
                judge = d_8

            elif sk == "乗馬":
                judge = d_9

            elif sk == "説得":
                judge = d_10

            elif sk == "英語:
                judge = d_11

            elif sk == "オカルト":
                judge = d_12

            elif sk == "心理学":
                judge = d_13

            elif sk == "人類学":
                judge = d_14

            elif sk == "歴史":
                judge = d_15

            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
            if sumresult <= judge:
                msg1 = f"{sumresult} <= {judge} => 成功"
            else:
                msg1 = f"{sumresult} > {judge} => 失敗"
            an = f"花難破納の判定結果{sk}を表示します。"   
            
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 

    
bot.run(token)
