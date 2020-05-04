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

MP_8199 = 6
HP_8199 = 12
SA_8199 = 30

MP_7568 = 15
HP_7568 = 13
SA_7568 = 75

MP_9995 = 8
HP_9995 = 9
SA_9995 = 40

MP_8464 = 16
HP_8464 = 9
SA_8464 = 80

#===============================================#

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
    
@bot.event
async def on_ready():
    CHANNEL_ID = 706950934013673562#チャンネルID(int)  
    channel = bot.get_channel(CHANNEL_ID)  
    await channel.send("Dice-botちゃん参上!")  
#===============================================#

@bot.command(name="pray")
async def pray(ctx: str):
    rand = random.randint(1,7)
    pic  = random.randint(1,100)
    if pic > 10:
        picimg = "https://media.discordapp.net/attachments/683147981456801947/706427466151100426/download20200500175023.png"
        if rand == 1:
            msg = f"にゃにゃにゃ！今の運命ではご不満かにゃ？\n\nお祈り......聞き届けたにゃ!!"
        elif rand == 2:
            msg = f"にゃにゃ??今の運命ではご不満ですかにゃ？\n\nシードを再生成するにゃ...!!!"
        elif rand == 3:
            msg = f"にゃ??\n\n信じるものは救われますにゃ!!!"
        elif rand == 4:
            msg = f"にゃにゃにゃ??\n\nあなたの願いは聞き入れられましたにゃ!!!"
        elif rand == 5:
            msg = f"にゃにゃ??運命が少し変わりました．良いか悪いかはともかくだにゃ!"
        elif rand == 6:
            msg = f"あなたにはきっと、素敵な未来が待ってますにゃ!!!！"
        elif rand == 7:
            msg = f"にゃ?\nまだ見ぬ未来に手を加えちゃうにゃ〜! な〜んてにゃ!"
    elif pic <= 10:
        picimg = "https://media.discordapp.net/attachments/683147981456801947/706496315453997076/download20200500222353.png"
        msg = f"人に頼み事をするときにはなんて言ったらいいのかにゃ???\n本当にその言葉であってるのかにゃ?"
    embed=discord.Embed(title="Dice-bot",description=msg, color=0xC7EAEA)
    embed.set_thumbnail(url=picimg)
    await ctx.send(embed=embed)
#===============================================#

@bot.command(name="hi")
async def pray(ctx: str):
    a_id = ctx.author.id
    rand = random.randint(1,20)
    if a_id == ID_4091: #admin
        if rand <= 3:
            msg = f"マスターなんて.....\n\n嫌いです！"
            picimg = f"https://media.discordapp.net/attachments/683147981456801947/706748861460381766/download20200501150727.png"
            embed=discord.Embed(title="Dice-bot",description=msg, color=0xC7EAEA)
            embed.set_thumbnail(url=picimg)
            await ctx.send(embed=embed)

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
    embed.add_field(name="id",value="小沼さん\n0864\n\n六谷さん\n0191\n\n遠江 俱璃夢さん\n8199\n\nRTa\n4091\n\n来須さん\n7568\n\nLenzさん\n4176\n\nExtraさん\n4560\n\n黒佐 智恵さん\n8464\n\n土屋 桑さん\n9995")
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
    embed.add_field(name="!dd",value="!dd {n}d{n}+{n}D{n}の書式で入力",inline=False)
    embed.add_field(name="!p",value="!p {states}+{N}の書式で入力\nステータスの表示は!p s",inline=False)
    embed.add_field(name="!m",value="!m {states}-{N}の書式で入力\nステータスの表示は!m s",inline=False)
    embed.add_field(name="!h",value="これを表示",inline=False)
    embed.add_field(name="!s",value="!s {何かを入力}の書式で能力値を表示",inline=False)
    embed.add_field(name="---------------------------------",value="キーパーメニュー",inline=False)
    embed.add_field(name="!id",value="IDを表示",inline=False)
    embed.add_field(name="!p",value="!p {id}&{states}+{N}の書式で入力\n{id}は各playerの#以降\nステータスの表示は!p s",inline=False)
    embed.add_field(name="!m",value="!m {id}&{states}-{N}の書式で入力\n{id}は各playerの#以降\nステータスの表示は!m s",inline=False)
    embed.add_field(name="!s",value="!s {id}&{何かを入力}の書式で能力値を表示\n{id}は各playerの#以降",inline=False)
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

    
@bot.command(name="dd")
async def dd(ctx, dice: str):
    """!dd {n}d{n}+{n}D{n}の書式で入力"""
    rolls, str1 = map(str, dice.split('d'))# {n},{n}+{n}D{n}
    limit, str2 =map(str, str1.split('+'))# {n},{n}D{n}
    rolls2, limit2 =map(int, str2.split('D'))
    rolls = int(rolls)    
    limit = int(limit)
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    mappedData = map(int, result.split(","))
    output = list(mappedData)
    sumresult = sum(output)
    result2 = ', '.join(str(random.randint(1, limit2)) for r in range(rolls2))
    mappedData2 = map(int, result2.split(","))
    output2 = list(mappedData2)
    sumresult2 = sum(output2)    
    firesult = sumresult + sumresult
    mention= f"<@{ctx.author.id}>"
    msg = f"{ctx.author.mention}\n 1:`{result}`\n 2:`{result2}`"
    msg2 = f"{firesult} = {sumresult} + {sumresult2}"
    embed = discord.Embed(title=firesult ,description=f"{mention}\n1:`{result}`\n2:`{result2}`\n{sumresult}\n{msg2}\n{ctx.message.content}",color=discord.Colour.from_rgb(238,139,150))

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
    
    if sumresult <= 5:
        msg1 = f"{msg1}\nクリティカル(01-05)です。"
    elif sumresult >= 96:
        msg1 = f"{msg1}\nファンブル(95-00)です。"
        
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
            an = f"現在の土屋 桑のステータスを表示します。"
            msg = f"土屋 桑\n耐久値 {HP_9995}/8. MP {MP_9995}/9. 正気度 {SA_9995}/99."
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
        an = f"現在の土屋 桑のステータスを表示します。"
        msg = f"土屋 桑\n耐久値 {HP_9995}/8. MP {MP_9995}/9. 正気度 {SA_9995}/99."
    elif a_id == ID_0191:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の加敷 碧郎のステータスを表示します。"
            msg = f"加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99."
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
        an = f"現在の加敷 碧郎のステータスを表示します。"
        msg = f"加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99."
    elif a_id == ID_8199:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の遠江 俱璃夢のステータスを表示します。"
            msg = f"遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99."
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
        an = f"現在の遠江 俱璃夢のステータスを表示します。"
        msg = f"遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99."

    elif a_id == ID_7568:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の花ヶ崎 恵梨佳のステータスを表示します。"
            msg = f"花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99."
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
        an = f"現在の花ヶ崎 恵梨佳のステータスを表示します。"
        msg = f"花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99."

    elif a_id == ID_8464:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の黒佐 智恵のステータスを表示します。"
            msg = f"黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."
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
        an = f"現在の黒佐 智恵のステータスを表示します。"
        msg = f"黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."

    elif a_id == ID_0864: #keeper
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, plus = map(str, str1.split('+'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"土屋 桑\n耐久値 {HP_9995}/9. MP {MP_9995}/8. 正気度 {SA_9995}/99.\n\n加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99.\n\n遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99.\n\n花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99.\n\n黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."
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
            an = f"現在の土屋 桑のステータスを表示します。"
            msg = f"土屋 桑\n耐久値 {HP_9995}/9. MP {MP_9995}/8. 正気度 {SA_9995}/99."
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
            an = f"現在の加敷 碧郎のステータスを表示します。"
            msg = f"加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99."
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
            an = f"現在の花ヶ崎 恵梨佳のステータスを表示します。"
            msg = f"花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99."
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
            an = f"現在の遠江 俱璃夢のステータスを表示します。"
            msg = f"遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99."
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
            an = f"現在の黒佐 智恵のステータスを表示します。"
            msg = f"黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."

    elif a_id == ID_4091: #admin
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, plus = map(str, str1.split('+'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"土屋 桑\n耐久値 {HP_9995}/9. MP {MP_9995}/8. 正気度 {SA_9995}/99.\n\n加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99.\n\n遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99.\n\n花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99.\n\n黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."
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
            an = f"現在の土屋 桑のステータスを表示します。"
            msg = f"土屋 桑\n耐久値 {HP_9995}/9. MP {MP_9995}/8. 正気度 {SA_9995}/99."
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
            an = f"現在の加敷 碧郎のステータスを表示します。"
            msg = f"加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99."
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
            an = f"現在の花ヶ崎 恵梨佳のステータスを表示します。"
            msg = f"花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99."
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
            an = f"現在の遠江 俱璃夢のステータスを表示します。"
            msg = f"遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99."
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
            an = f"現在の黒佐 智恵のステータスを表示します。"
            msg = f"黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."
            
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 

#===============================================#

@bot.command(name="m")
async def s0864(ctx,stu: str):
    """!p {states}-{N}の書式で入力 ステータスの減算を行います。"""
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
            an = f"現在の土屋 桑のステータスを表示します。"
            msg = f"土屋 桑\n耐久値 {HP_9995}/8. MP {MP_9995}/9. 正気度 {SA_9995}/99."
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
        an = f"現在の土屋 桑のステータスを表示します。"
        msg = f"土屋 桑\n耐久値 {HP_9995}/8. MP {MP_9995}/9. 正気度 {SA_9995}/99."
    elif a_id == ID_0191:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の加敷 碧郎のステータスを表示します。"
            msg = f"加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99."
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
        an = f"現在の加敷 碧郎のステータスを表示します。"
        msg = f"加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99."
    elif a_id == ID_8199:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の遠江 俱璃夢のステータスを表示します。"
            msg = f"遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99."
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
        an = f"現在の遠江 俱璃夢のステータスを表示します。"
        msg = f"遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99."

    elif a_id == ID_7568:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の花ヶ崎 恵梨佳のステータスを表示します。"
            msg = f"花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99."
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
        an = f"現在の花ヶ崎 恵梨佳のステータスを表示します。"
        msg = f"花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99."

    elif a_id == ID_8464:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の黒佐 智恵のステータスを表示します。"
            msg = f"黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."
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
        an = f"現在の黒佐 智恵のステータスを表示します。"
        msg = f"黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."

    elif a_id == ID_0864: #keeper
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, minus = map(str, str1.split('-'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"土屋 桑\n耐久値 {HP_9995}/9. MP {MP_9995}/8. 正気度 {SA_9995}/99.\n\n加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99.\n\n遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99.\n\n花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99.\n\n黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."
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
            an = f"現在の土屋 桑のステータスを表示します。"
            msg = f"土屋 桑\n耐久値 {HP_9995}/9. MP {MP_9995}/8. 正気度 {SA_9995}/99."
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
            an = f"現在の加敷 碧郎のステータスを表示します。"
            msg = f"加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99."
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
            an = f"現在の花ヶ崎 恵梨佳のステータスを表示します。"
            msg = f"花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99."
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
            an = f"現在の遠江 俱璃夢のステータスを表示します。"
            msg = f"遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99."
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
            an = f"現在の黒佐 智恵のステータスを表示します。"
            msg = f"黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."

    elif a_id == ID_4091: #admin
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, minus = map(str, str1.split('-'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"土屋 桑\n耐久値 {HP_9995}/9. MP {MP_9995}/8. 正気度 {SA_9995}/99.\n\n加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99.\n\n遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99.\n\n花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99.\n\n黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."
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
            an = f"現在の土屋 桑のステータスを表示します。"
            msg = f"土屋 桑\n耐久値 {HP_9995}/9. MP {MP_9995}/8. 正気度 {SA_9995}/99."
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
            an = f"現在の加敷 碧郎のステータスを表示します。"
            msg = f"加敷 碧郎\n耐久値 {HP_0191}/13. MP {MP_0191}/12. 正気度 {SA_0191}/99."
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
            an = f"現在の花ヶ崎 恵梨佳のステータスを表示します。"
            msg = f"花ヶ崎 恵梨佳\n耐久値 {HP_7568}/13. MP {MP_7568}/15. 正気度 {SA_7568}/99."
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
            an = f"現在の遠江 俱璃夢のステータスを表示します。"
            msg = f"遠江 俱璃夢\n耐久値 {HP_8199}/12. MP {MP_8199}/6. 正気度 {SA_8199}/99."
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
            an = f"現在の黒佐 智恵のステータスを表示します。"
            msg = f"黒佐 智恵\n耐久値 {HP_8464}/9. MP {MP_8464}/16. 正気度 {SA_8464}/99."
            
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 
#================================================#
@bot.command(name="s")
async def s(ctx,stu: str):
    """!s {何でもいい ※ただし何か記述}の書式で入力 技能値の表示を行います。"""
    a_id = ctx.author.id
    if a_id == ID_9995:
        an = f"土屋 桑の技能値を表示します。"
        msg = f"土屋 桑 26歳女性 農林業作業者\nSTR 9. DEX 13. INT 13. アイディア 65.\nCON 9. APP 13. POW 8. 幸運 40.\nSIZ 14. SAN 40. EDU 13. 知識 65. \nDB +0.\n応急手当50. 機械修理40. 重機械操作40. 回避 26. 製作(罠、案山子含む)40. 追跡40. 電気修理40. 博物学50. 目星61. 化学 15. 生物学 55. 図書館 47. キック 65.\n\n武器:\nチェーンソー(40%) 2D8ダメージ\n耐久力20 97で故障"
        msg = f"{an}\n{msg}"
        await ctx.send(f"{ctx.author.mention}")
        await ctx.send(msg) 

    elif a_id == ID_0191:
        an = f"加敷 碧郎の技能値を表示します。"
        msg = f"加敷 碧郎 22歳男性 放浪者\nSTR 7. DEX 14. INT 15. アイディア 75.\nCON 12. APP 15. POW 12. 幸運 60.\nSIZ 13. SAN 60. EDU 9. 知識 45.\nDB +0.\n回避 28. 心理学45. 博物学60. 隠れる20. 鍵開け55. 運転50. 信用60. ライフル40."
        msg = f"{an}\n{msg}"
        await ctx.send(f"{ctx.author.mention}")
        await ctx.send(msg) 
    elif a_id == ID_8199:
        an = f"遠江 俱璃夢の技能値を表示します。"
        msg = f"遠江 俱璃夢 22歳男性 犯罪者\nSTR 8. DEX 7. INT 13. アイディア 65.\nCON 16. APP 13. POW 6. 幸運 30.\nSIZ 9. SAN 30. EDU 17. 知識 85. \nDB +0.\n鍵開け 61. 拳銃 75. 回避 74. コンピューター 71. 忍び歩き 65. 変装 71. 目星 70. 隠れる 65.\n\n武器:\nノーリンコT-54 1D8ダメージ\n基本射程15m 攻撃は2回/1ラウンド 装弾数8 耐久力8 98で故障"
        msg = f"{an}\n{msg}"
        await ctx.send(f"{ctx.author.mention}")
        await ctx.send(msg) 

    elif a_id == ID_7568:
        an = f"花ヶ崎 恵梨佳の技能値を表示します。"
        msg = f"花ヶ崎 恵梨佳 20歳女性 放浪者\nSTR 14. DEX 7. INT 9. アイディア 45.\nCON 12. APP 13. POW 15. 幸運 75.\nSIZ 15. SAN 75. EDU 11. 知識 55. \nDB +1D4.\n回避 65. こぶし 70. 隠れる 65. 聞き耳 70. 忍び歩き 65. 目星 44. 言いくるめ 70."
        msg = f"{an}\n{msg}"
        await ctx.send(f"{ctx.author.mention}")
        await ctx.send(msg) 

    elif a_id == ID_8464:
        an = f"黒佐 智恵の技能値を表示します。"
        msg = f"黒佐 智恵 28歳女性 超心理学者\nSTR 11. DEX 8. INT 17. アイディア 85.\nCON 7. APP 14. POW 16. 幸運 80.\nSIZ 10. SAN 80. EDU 17. 知識 85. \nDB +0.\n回避36. キック50. こぶし65. 応急手当50. 聞き耳40. 写真術60. 追跡40. 図書館55. 乗馬50. 説得45. 英語60. オカルト50.心理学70. 人類学31. 歴史50."
        msg = f"{an}\n{msg}"
        await ctx.send(f"{ctx.author.mention}")
        await ctx.send(msg) 

    elif a_id == ID_0864: #keeper
        try:
            pl_di, str1 = map(str, stu.split('&'))
        except Exception:
            an = f"現在の全Playerの能力値を表示します。"
            msg = f"加敷 碧郎 22歳男性 放浪者(六)\nSTR 7. DEX 14. INT 15. アイディア 75.\nCON 12. APP 15. POW 12. 幸運 60.\nSIZ 13. SAN 60. EDU 9. 知識 45. \nDB +0.\n回避 28. 心理学45. 博物学60. 隠れる20. 鍵開け55. 運転50. 信用60. ライフル40.\n\n\n花ヶ崎 恵梨佳 20歳女性 放浪者(来)\nSTR 14. DEX 7. INT 9. アイディア 45.\nCON 12. APP 13. POW 15. 幸運 75.\nSIZ 15. SAN 75. EDU 11. 知識 55. \nDB +1D4.\n回避 65. こぶし 70. 隠れる 65. 聞き耳 70. 忍び歩き 65. 目星 44. 言いくるめ 70.\n\n\n遠江 俱璃夢 22歳男性 犯罪者 (羅)\nSTR 8. DEX 7. INT 13. アイディア 65.\nCON 16. APP 13. POW 6. 幸運 30.\nSIZ 9. SAN 30. EDU 17. 知識 85. \nDB +0.\n鍵開け 61. 拳銃 75. 回避 74. コンピューター 71. 忍び歩き 65. 変装 71. 目星 70. 隠れる 65.\n\n武器:\nノーリンコT-54 1D8ダメージ\n基本射程15m 攻撃は2回/1ラウンド 装弾数8 耐久力8 98で故障\n\n\n黒佐 智恵 28歳女性 超心理学者 (花)\nSTR 11. DEX 8. INT 17. アイディア 85.\nCON 7. APP 14. POW 16. 幸運 80.\nSIZ 10. SAN 80. EDU 17. 知識 85. \nDB +0.\n回避36. キック50. こぶし65. 応急手当50. 聞き耳40. 写真術60. 追跡40. 図書館55. 乗馬50. 説得45. 英語60. オカルト50.心理学70. 人類学31. 歴史50.\n\n\n土屋 桑 26歳女性 農林業作業者(ぬ)\nSTR 9. DEX 13. INT 13. アイディア 65.\nCON 9. APP 13. POW 8. 幸運 40.\nSIZ 14. SAN 40. EDU 13. 知識 65. \nDB +0.\n応急手当50. 機械修理40. 重機械操作40. 回避 26. 製作(罠、案山子含む)40. 追跡40. 電気修理40. 博物学50. 目星61. 化学 15. 生物学 55. 図書館 47. キック 65.\n\n武器:\nチェーンソー(40%) 2D8ダメージ\n耐久力20 97で故障"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)    
        if pl_di == "9995":
            an = f"土屋 桑の技能値を表示します。"
            msg = f"土屋 桑 26歳女性 農林業作業者\nSTR 9. DEX 13. INT 13. アイディア 65.\nCON 9. APP 13. POW 8. 幸運 40.\nSIZ 14. SAN 40. EDU 13. 知識 65. \nDB +0.\n応急手当50. 機械修理40. 重機械操作40. 回避 26. 製作(罠、案山子含む)40. 追跡40. 電気修理40. 博物学50. 目星61. 化学 15. 生物学 55. 図書館 47. キック 65.\n\n武器:\nチェーンソー(40%) 2D8ダメージ\n耐久力20 97で故障"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)
        elif pl_di == "0191":
            an = f"加敷 碧郎の技能値を表示します。"
            msg = f"加敷 碧郎 22歳男性 放浪者\nSTR 7. DEX 14. INT 15. アイディア 75.\nCON 12. APP 15. POW 12. 幸運 60.\nSIZ 13. SAN 60. EDU 9. 知識 45.\nDB +0.\n回避 28. 心理学45. 博物学60. 隠れる20. 鍵開け55. 運転50. 信用60. ライフル40."
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)
        elif pl_di == "7568":
            an = f"花ヶ崎 恵梨佳の技能値を表示します。"
            msg = f"花ヶ崎 恵梨佳 20歳女性 放浪者\nSTR 14. DEX 7. INT 9. アイディア 45.\nCON 12. APP 13. POW 15. 幸運 75.\nSIZ 15. SAN 75. EDU 11. 知識 55. \nDB +1D4.\n回避 65. こぶし 70. 隠れる 65. 聞き耳 70. 忍び歩き 65. 目星 44. 言いくるめ 70."
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg) 
        elif pl_di == "8199":
            an = f"遠江 俱璃夢の技能値を表示します。"
            msg = f"遠江 俱璃夢 22歳男性 犯罪者\nSTR 8. DEX 7. INT 13. アイディア 65.\nCON 16. APP 13. POW 6. 幸運 30.\nSIZ 9. SAN 30. EDU 17. 知識 85. \nDB +0.\n鍵開け 61. 拳銃 75. 回避 74. コンピューター 71. 忍び歩き 65. 変装 71. 目星 70. 隠れる 65.\n\n武器:\nノーリンコT-54 1D8ダメージ\n基本射程15m 攻撃は2回/1ラウンド 装弾数8 耐久力8 98で故障"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg) 
        elif pl_di == "8464":
            an = f"黒佐 智恵の技能値を表示します。"
            msg = f"黒佐 智恵 28歳女性 超心理学者\nSTR 11. DEX 8. INT 17. アイディア 85.\nCON 7. APP 14. POW 16. 幸運 80.\nSIZ 10. SAN 80. EDU 17. 知識 85. \nDB +0.\n回避36. キック50. こぶし65. 応急手当50. 聞き耳40. 写真術60. 追跡40. 図書館55. 乗馬50. 説得45. 英語60. オカルト50.心理学70. 人類学31. 歴史50."
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg) 

    elif a_id == ID_4091: #admin
        try:
            pl_di, str1 = map(str, stu.split('&'))
        except Exception:
            an = f"現在の全Playerの能力値を表示します。"
            msg = f"加敷 碧郎 22歳男性 放浪者(六)\nSTR 7. DEX 14. INT 15. アイディア 75.\nCON 12. APP 15. POW 12. 幸運 60.\nSIZ 13. SAN 60. EDU 9. 知識 45. \nDB +0.\n回避 28. 心理学45. 博物学60. 隠れる20. 鍵開け55. 運転50. 信用60. ライフル40.\n\n\n花ヶ崎 恵梨佳 20歳女性 放浪者(来)\nSTR 14. DEX 7. INT 9. アイディア 45.\nCON 12. APP 13. POW 15. 幸運 75.\nSIZ 15. SAN 75. EDU 11. 知識 55. \nDB +1D4.\n回避 65. こぶし 70. 隠れる 65. 聞き耳 70. 忍び歩き 65. 目星 44. 言いくるめ 70.\n\n\n遠江 俱璃夢 22歳男性 犯罪者 (羅)\nSTR 8. DEX 7. INT 13. アイディア 65.\nCON 16. APP 13. POW 6. 幸運 30.\nSIZ 9. SAN 30. EDU 17. 知識 85. \nDB +0.\n鍵開け 61. 拳銃 75. 回避 74. コンピューター 71. 忍び歩き 65. 変装 71. 目星 70. 隠れる 65.\n\n武器:\nノーリンコT-54 1D8ダメージ\n基本射程15m 攻撃は2回/1ラウンド 装弾数8 耐久力8 98で故障\n\n\n黒佐 智恵 28歳女性 超心理学者 (花)\nSTR 11. DEX 8. INT 17. アイディア 85.\nCON 7. APP 14. POW 16. 幸運 80.\nSIZ 10. SAN 80. EDU 17. 知識 85. \nDB +0.\n回避36. キック50. こぶし65. 応急手当50. 聞き耳40. 写真術60. 追跡40. 図書館55. 乗馬50. 説得45. 英語60. オカルト50.心理学70. 人類学31. 歴史50.\n\n\n土屋 桑 26歳女性 農林業作業者(ぬ)\nSTR 9. DEX 13. INT 13. アイディア 65.\nCON 9. APP 13. POW 8. 幸運 40.\nSIZ 14. SAN 40. EDU 13. 知識 65. \nDB +0.\n応急手当50. 機械修理40. 重機械操作40. 回避 26. 製作(罠、案山子含む)40. 追跡40. 電気修理40. 博物学50. 目星61. 化学 15. 生物学 55. 図書館 47. キック 65.\n\n武器:\nチェーンソー(40%) 2D8ダメージ\n耐久力20 97で故障"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)    
            return
        if pl_di == "9995":
            an = f"土屋 桑の技能値を表示します。"
            msg = f"土屋 桑 26歳女性 農林業作業者\nSTR 9. DEX 13. INT 13. アイディア 65.\nCON 9. APP 13. POW 8. 幸運 40.\nSIZ 14. SAN 40. EDU 13. 知識 65. \nDB +0.\n応急手当50. 機械修理40. 重機械操作40. 回避 26. 製作(罠、案山子含む)40. 追跡40. 電気修理40. 博物学50. 目星61. 化学 15. 生物学 55. 図書館 47. キック 65.\n\n武器:\nチェーンソー(40%) 2D8ダメージ\n耐久力20 97で故障"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)
        elif pl_di == "0191":
            an = f"加敷 碧郎の技能値を表示します。"
            msg = f"加敷 碧郎 22歳男性 放浪者\nSTR 7. DEX 14. INT 15. アイディア 75.\nCON 12. APP 15. POW 12. 幸運 60.\nSIZ 13. SAN 60. EDU 9. 知識 45.\nDB +0.\n回避 28. 心理学45. 博物学60. 隠れる20. 鍵開け55. 運転50. 信用60. ライフル40."
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)
        elif pl_di == "7568":
            an = f"花ヶ崎 恵梨佳の技能値を表示します。"
            msg = f"花ヶ崎 恵梨佳 20歳女性 放浪者\nSTR 14. DEX 7. INT 9. アイディア 45.\nCON 12. APP 13. POW 15. 幸運 75.\nSIZ 15. SAN 75. EDU 11. 知識 55. \nDB +1D4.\n回避 65. こぶし 70. 隠れる 65. 聞き耳 70. 忍び歩き 65. 目星 44. 言いくるめ 70."
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg) 
        elif pl_di == "8199":
            an = f"遠江 俱璃夢の技能値を表示します。"
            msg = f"遠江 俱璃夢 22歳男性 犯罪者\nSTR 8. DEX 7. INT 13. アイディア 65.\nCON 16. APP 13. POW 6. 幸運 30.\nSIZ 9. SAN 30. EDU 17. 知識 85. \nDB +0.\n鍵開け 61. 拳銃 75. 回避 74. コンピューター 71. 忍び歩き 65. 変装 71. 目星 70. 隠れる 65.\n\n武器:\nノーリンコT-54 1D8ダメージ\n基本射程15m 攻撃は2回/1ラウンド 装弾数8 耐久力8 98で故障"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg) 
        elif pl_di == "8464":
            an = f"黒佐 智恵の技能値を表示します。"
            msg = f"黒佐 智恵 28歳女性 超心理学者\nSTR 11. DEX 8. INT 17. アイディア 85.\nCON 7. APP 14. POW 16. 幸運 80.\nSIZ 10. SAN 80. EDU 17. 知識 85. \nDB +0.\n回避36. キック50. こぶし65. 応急手当50. 聞き耳40. 写真術60. 追跡40. 図書館55. 乗馬50. 説得45. 英語60. オカルト50.心理学70. 人類学31. 歴史50."
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg) 

# ===============================================#

#    # id_0191
#A_1 = 28 #回避
#A_2 = 45 #心理学
#A_3 = 60 #博物学
#A_4 = 20 #隠れる
#A_5 = 55 #鍵開け
#A_6 = 50 #運転
#A_7 = 60 #信用
#A_8 = 40 #ライフル

#    # id_7568
#B_1 = 65 #回避
#B_2 = 70 #こぶし
#B_3 = 65 #隠れる
#B_4 = 70 #聞き耳
#B_5 = 65 #忍び歩き
#B_6 = 44 #目星
#B_7 = 70 #言いくるめ

#    # id_8199
#C_1 = 61 #鍵開け
#C_2 = 75 #拳銃
#C_3 = 74 #回避
#C_4 = 71 #コンピューター
#C_5 = 65 #忍び歩き
#C_6 = 71 #変装
#C_7 = 70 #目星
#C_8 = 65 #隠れる

#    # id_8464
#D_1 = 36 #回避
#D_2 = 50 #キック
#D_3 = 65 #こぶし
#D_4 = 50 #応急手当
#D_5 = 40 #聞き耳
#D_6 = 60 #写真術
#D_7 = 40 #追跡
#D_8 = 55 #図書館
#D_9 = 50 #乗馬
#D_10 = 45 #説得
#D_11 = 60 #英語
#D_12 = 50 #オカルト
#D_13 = 70 #心理学
#D_14 = 31 #人類学
#D_15 = 50 #歴史

#    # ie_9995
#E_1 = 50 #応急手当
#E_2 = 40 #機械修理
#E_3 = 40 #重機機械操作
#E_4 = 26 #回避
#E_5 = 40 #製作
#E_6 = 40 #追跡
#E_7 = 40 #電気修理
#E_8 = 50 #博物学
#E_9 = 61 #目星
#E_10 = 15 #化学
#E_11 = 55 #生物学
#E_12 = 47 #図書館
#E_13 = 65 #キック




#================================================#


# @bot.command(name="j")
# async def s0864(ctx,sk: str):
#     """!j {技能}の書式で入力 技能の判定を行います。"""

#     global A_1
#     global A_2
#     global A_3
#     global A_4
#     global A_5
#     global A_6
#     global A_7
#     global A_8

#     global B_1
#     global B_2
#     global B_3
#     global B_4
#     global B_5
#     global B_6
#     global B_7

#     global C_1
#     global C_2
#     global C_3
#     global C_4
#     global C_5
#     global C_6
#     global C_7
#     global C_8
    
#     global D_1
#     global D_2
#     global D_3
#     global D_4
#     global D_5
#     global D_6
#     global D_7
#     global D_8
#     global D_9
#     global D_10
#     global D_11
#     global D_12
#     global D_13
#     global D_14
#     global D_15

#     global E_1
#     global E_2
#     global E_3
#     global E_4
#     global E_5
#     global E_6
#     global E_7
#     global E_8
#     global E_9
#     global E_10
#     global E_11
#     global E_12
#     global E_13





#     a_id = ctx.author.id
#     if a_id == ID_0191:

#         if sk == "回避":
#             judge = A_1 
            
#         elif sk == "心理学":
#             judge = A_2

#         elif sk == "博物学":
#             judge = A_3

#         elif sk == "隠れる":
#             judge = A_4

#         elif sk == "鍵開け":
#             judge = A_5

#         elif sk == "運転":
#             judge = A_6

#         elif sk == "信用":
#             judge = A_7

#         elif sk == "ライフル":
#             judge = A_8

#         result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#         mappedData = map(int, result.split(","))
#         output = list(mappedData)
#         sumresult = sum(output)
#         sumresult = int(sumresult)
#         msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#         if sumresult <= judge:
#             msg1 = f"{sumresult} <= {judge} => 成功"
#         else:
#             msg1 = f"{sumresult} > {judge} => 失敗"
#         an = f"六谷潤の判定結果{sk}を表示します。"   

#     elif a_id == ID_7568:
#         if sk == "回避":
#             judge = B_1 
            
#         elif sk == "こぶし":
#             judge = B_2

#         elif sk == "隠れる":
#             judge = B_3

#         elif sk == "聞き耳":
#             judge = B_4

#         elif sk == "忍び歩き":
#             judge = B_5

#         elif sk == "目星":
#             judge = B_6

#         elif sk == "言いくるめ":
#             judge = B_7

#         result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#         mappedData = map(int, result.split(","))
#         output = list(mappedData)
#         sumresult = sum(output)
#         sumresult = int(sumresult)
#         msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#         if sumresult <= judge:
#             msg1 = f"{sumresult} <= {judge} => 成功"
#         else:
#             msg1 = f"{sumresult} > {judge} => 失敗"
#         an = f"来須ましろの判定結果{sk}を表示します。"        

#     elif a_id == ID_8199:
#         if sk == "鍵開け":
#             judge = C_1 
            
#         elif sk == "拳銃":
#             judge = C_2

#         elif sk == "回避":
#             judge = C_3

#         elif sk == "コンピューター":
#             judge = C_4

#         elif sk == "忍び歩き":
#             judge = C_5

#         elif sk == "変装":
#             judge = C_6

#         elif sk == "目星":
#             judge = C_7

#         elif sk == "隠れる":
#             judge = C_8

#         result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#         mappedData = map(int, result.split(","))
#         output = list(mappedData)
#         sumresult = sum(output)
#         sumresult = int(sumresult)
#         msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#         if sumresult <= judge:
#             msg1 = f"{sumresult} <= {judge} => 成功"
#         else:
#             msg1 = f"{sumresult} > {judge} => 失敗"
#         an = f"羅闇の判定結果{sk}を表示します。"        

#     elif a_id == ID_8464:
#         if sk == "回避":
#             judge = D_1 
            
#         elif sk == "キック":
#             judge = D_2

#         elif sk == "こぶし":
#             judge = D_3

#         elif sk == "応急手当":
#             judge = D_4

#         elif sk == "聞き耳":
#             judge = D_5

#         elif sk == "写真術":
#             judge = D_6

#         elif sk == "追跡":
#             judge = D_7

#         elif sk == "図書館":
#             judge = d_8

#         elif sk == "乗馬":
#             judge = D_9

#         elif sk == "説得":
#             judge = d_10

#         elif sk == "英語:
#             judge = D_11

#         elif sk == "オカルト":
#             judge = D_12

#         elif sk == "心理学":
#             judge = D_13

#         elif sk == "人類学":
#             judge = D_14

#         elif sk == "歴史":
#             judge = D_15

#         result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#         mappedData = map(int, result.split(","))
#         output = list(mappedData)
#         sumresult = sum(output)
#         sumresult = int(sumresult)
#         msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#         if sumresult <= judge:
#             msg1 = f"{sumresult} <= {judge} => 成功"
#         else:
#             msg1 = f"{sumresult} > {judge} => 失敗"
#         an = f"花難破納の判定結果{sk}を表示します。"        

#     elif a_id == ID_9995:
#         if sk == "応急手当":
#             judge = E_1 
            
#         elif sk == "機械修理":
#             judge = E_2

#         elif sk == "重機械操作":
#             judge = E_3

#         elif sk == "回避":
#             judge = E_4

#         elif sk == "製作":
#             judge = E_5

#         elif sk == "追跡":
#             judge = E_6

#         elif sk == "電気修理":
#             judge = E_7

#         elif sk == "博物学":
#             judge = E_8

#         elif sk == "目星":
#             judge = E_9

#         elif sk == "化学":
#             judge = E_10

#         elif sk == "生物学:
#             judge = E_11

#         elif sk == "図書館":
#             judge = E_12

#         elif sk == "キック":
#             judge = E_13

#         result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#         mappedData = map(int, result.split(","))
#         output = list(mappedData)
#         sumresult = sum(output)
#         sumresult = int(sumresult)
#         msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#         if sumresult <= judge:
#             msg1 = f"{sumresult} <= {judge} => 成功"
#         else:
#             msg1 = f"{sumresult} > {judge} => 失敗"
#         an = f"ぬぬぬの判定結果{sk}を表示します。"  

#     elif a_id == ID_0864: #keeper
#         try:
#             pl_di, sk = map(str, sk.split('&'))
#         except Exception:
#             an = f"Error"
#             msg = f"書式不一致\n!j ID&技能値"
#             embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
#             await ctx.send(f"{ctx.author.mention}")
#             await ctx.send(embed=embed)    
#             return
#         if pl_di == "9995":
#             if sk == "応急手当":
#                 judge = E_1 
            
#             elif sk == "機械修理":
#                 judge = E_2

#             elif sk == "重機械操作":
#                 judge = E_3

#             elif sk == "回避":
#                 judge = E_4

#             elif sk == "製作":
#                 judge = E_5

#             elif sk == "追跡":
#                 judge = E_6

#             elif sk == "電気修理":
#                 judge = E_7

#             elif sk == "博物学":
#                 judge = E_8

#             elif sk == "目星":
#                 judge = E_9

#             elif sk == "化学":
#                 judge = E_10

#             elif sk == "生物学:
#                 judge = E_11

#             elif sk == "図書館":
#                 judge = E_12

#             elif sk == "キック":
#                 judge = E_13

#             result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#             mappedData = map(int, result.split(","))
#             output = list(mappedData)
#             sumresult = sum(output)
#             sumresult = int(sumresult)
#             msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#             if sumresult <= judge:
#                 msg1 = f"{sumresult} <= {judge} => 成功"
#             else:
#                 msg1 = f"{sumresult} > {judge} => 失敗"
#             an = f"ぬぬぬの判定結果{sk}を表示します。"  

#         elif pl_di == "0191":

#             if sk == "回避":
#                 judge = A_1 
            
#             elif sk == "心理学":
#                 judge = A_2

#             elif sk == "博物学":
#                 judge = A_3

#             elif sk == "隠れる":
#                 judge = A_4

#             elif sk == "鍵開け":
#                 judge = A_5

#             elif sk == "運転":
#                 judge = A_6

#             elif sk == "信用":
#                 judge = A_7

#             elif sk == "ライフル":
#                 judge = A_8

#             result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#             mappedData = map(int, result.split(","))
#             output = list(mappedData)
#             sumresult = sum(output)
#             sumresult = int(sumresult)
#             msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#             if sumresult <= judge:
#                 msg1 = f"{sumresult} <= {judge} => 成功"
#             else:
#                 msg1 = f"{sumresult} > {judge} => 失敗"
#             an = f"六谷潤の判定結果{sk}を表示します。" 
#         elif pl_di == "7568":
#             if sk == "回避":
#                 judge = B_1 
            
#             elif sk == "こぶし":
#                 judge = B_2

#             elif sk == "隠れる":
#                 judge = B_3

#             elif sk == "聞き耳":
#                 judge = B_4

#             elif sk == "忍び歩き":
#                 judge = B_5

#             elif sk == "目星":
#                 judge = B_6

#             elif sk == "言いくるめ":
#                 judge = B_7

#             result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#             mappedData = map(int, result.split(","))
#             output = list(mappedData)
#             sumresult = sum(output)
#             sumresult = int(sumresult)
#             msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#             if sumresult <= judge:
#                 msg1 = f"{sumresult} <= {judge} => 成功"
#             else:
#                 msg1 = f"{sumresult} > {judge} => 失敗"
#             an = f"来須ましろの判定結果{sk}を表示します。"       
#         elif pl_di == "8199":
#             if sk == "鍵開け":
#                 judge = C_1 
            
#             elif sk == "拳銃":
#                 judge = C_2

#             elif sk == "回避":
#                 judge = C_3

#             elif sk == "コンピューター":
#                 judge = C_4

#             elif sk == "忍び歩き":
#                 judge = C_5

#             elif sk == "変装":
#                 judge = C_6

#             elif sk == "目星":
#                 judge = C_7

#             elif sk == "隠れる":
#                 judge = C_8

#             result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#             mappedData = map(int, result.split(","))
#             output = list(mappedData)
#             sumresult = sum(output)
#             sumresult = int(sumresult)
#             msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#             if sumresult <= judge:
#                 msg1 = f"{sumresult} <= {judge} => 成功"
#             else:
#                 msg1 = f"{sumresult} > {judge} => 失敗"
#             an = f"羅闇の判定結果{sk}を表示します。" 
#         elif pl_di == "8464":
#             if sk == "回避":
#                 judge = D_1 
            
#             elif sk == "キック":
#                 judge = D_2

#             elif sk == "こぶし":
#                 judge = D_3

#             elif sk == "応急手当":
#                 judge = D_4

#             elif sk == "聞き耳":
#                 judge = D_5

#             elif sk == "写真術":
#                 judge = D_6

#             elif sk == "追跡":
#                 judge = D_7

#             elif sk == "図書館":
#                 judge = D_8

#             elif sk == "乗馬":
#                 judge = D_9

#             elif sk == "説得":
#                 judge = D_10

#             elif sk == "英語:
#                 judge = D_11

#             elif sk == "オカルト":
#                 judge = D_12

#             elif sk == "心理学":
#                 judge = D_13

#             elif sk == "人類学":
#                 judge = D_14

#             elif sk == "歴史":
#                 judge = D_15

#             result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#             mappedData = map(int, result.split(","))
#             output = list(mappedData)
#             sumresult = sum(output)
#             sumresult = int(sumresult)
#             msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#             if sumresult <= judge:
#                 msg1 = f"{sumresult} <= {judge} => 成功"
#             else:
#                 msg1 = f"{sumresult} > {judge} => 失敗"
#             an = f"花難破納の判定結果{sk}を表示します。"   

#     elif a_id == ID_4091: #admin
#         try:
#             pl_di, sk = map(str, sk.split('&'))
#         except Exception:
#             an = f"Error"
#             msg = f"書式不一致\n!j ID&技能値"
#             embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
#             await ctx.send(f"{ctx.author.mention}")
#             await ctx.send(embed=embed)    
#             return
#         if pl_di == "9995":
#             if sk == "応急手当":
#                 judge = E_1 
            
#             elif sk == "機械修理":
#                 judge = E_2

#             elif sk == "重機械操作":
#                 judge = E_3

#             elif sk == "回避":
#                 judge = E_4

#             elif sk == "製作":
#                 judge = E_5

#             elif sk == "追跡":
#                 judge = E_6

#             elif sk == "電気修理":
#                 judge = E_7

#             elif sk == "博物学":
#                 judge = E_8

#             elif sk == "目星":
#                 judge = E_9

#             elif sk == "化学":
#                 judge = E_10

#             elif sk == "生物学:
#                 judge = E_11

#             elif sk == "図書館":
#                 judge = E_12

#             elif sk == "キック":
#                 judge = E_13

#             result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#             mappedData = map(int, result.split(","))
#             output = list(mappedData)
#             sumresult = sum(output)
#             sumresult = int(sumresult)
#             msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#             if sumresult <= judge:
#                 msg1 = f"{sumresult} <= {judge} => 成功"
#             else:
#                 msg1 = f"{sumresult} > {judge} => 失敗"
#             an = f"ぬぬぬの判定結果{sk}を表示します。"  

#         elif pl_di == "0191":

#             if sk == "回避":
#                 judge = A_1 
            
#             elif sk == "心理学":
#                 judge = A_2

#             elif sk == "博物学":
#                 judge = A_3

#             elif sk == "隠れる":
#                 judge = A_4

#             elif sk == "鍵開け":
#                 judge = A_5

#             elif sk == "運転":
#                 judge = A_6

#             elif sk == "信用":
#                 judge = A_7

#             elif sk == "ライフル":
#                 judge = A_8

#             result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#             mappedData = map(int, result.split(","))
#             output = list(mappedData)
#             sumresult = sum(output)
#             sumresult = int(sumresult)
#             msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#             if sumresult <= judge:
#                 msg1 = f"{sumresult} <= {judge} => 成功"
#             else:
#                 msg1 = f"{sumresult} > {judge} => 失敗"
#             an = f"六谷潤の判定結果{sk}を表示します。" 
#         elif pl_di == "7568":
#             if sk == "回避":
#                 judge = B_1 
            
#             elif sk == "こぶし":
#                 judge = B_2

#             elif sk == "隠れる":
#                 judge = B_3

#             elif sk == "聞き耳":
#                 judge = B_4

#             elif sk == "忍び歩き":
#                 judge = B_5

#             elif sk == "目星":
#                 judge = B_6

#             elif sk == "言いくるめ":
#                 judge = B_7

#             result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#             mappedData = map(int, result.split(","))
#             output = list(mappedData)
#             sumresult = sum(output)
#             sumresult = int(sumresult)
#             msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#             if sumresult <= judge:
#                 msg1 = f"{sumresult} <= {judge} => 成功"
#             else:
#                 msg1 = f"{sumresult} > {judge} => 失敗"
#             an = f"来須ましろの判定結果{sk}を表示します。"       
#         elif pl_di == "8199":
#             if sk == "鍵開け":
#                 judge = C_1 
            
#             elif sk == "拳銃":
#                 judge = C_2

#             elif sk == "回避":
#                 judge = C_3

#             elif sk == "コンピューター":
#                 judge = C_4

#             elif sk == "忍び歩き":
#                 judge = C_5

#             elif sk == "変装":
#                 judge = C_6

#             elif sk == "目星":
#                 judge = C_7

#             elif sk == "隠れる":
#                 judge = C_8

#             result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#             mappedData = map(int, result.split(","))
#             output = list(mappedData)
#             sumresult = sum(output)
#             sumresult = int(sumresult)
#             msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#             if sumresult <= judge:
#                 msg1 = f"{sumresult} <= {judge} => 成功"
#             else:
#                 msg1 = f"{sumresult} > {judge} => 失敗"
#             an = f"羅闇の判定結果{sk}を表示します。" 
#         elif pl_di == "8464":
#             if sk == "回避":
#                 judge = D_1 
            
#             elif sk == "キック":
#                 judge = D_2

#             elif sk == "こぶし":
#                 judge = D_3

#             elif sk == "応急手当":
#                 judge = D_4

#             elif sk == "聞き耳":
#                 judge = D_5

#             elif sk == "写真術":
#                 judge = D_6

#             elif sk == "追跡":
#                 judge = D_7

#             elif sk == "図書館":
#                 judge = D_8

#             elif sk == "乗馬":
#                 judge = D_9

#             elif sk == "説得":
#                 judge = D_10

#             elif sk == "英語:
#                 judge = D_11

#             elif sk == "オカルト":
#                 judge = D_12

#             elif sk == "心理学":
#                 judge = D_13

#             elif sk == "人類学":
#                 judge = D_14

#             elif sk == "歴史":
#                 judge = D_15

#             result = ', '.join(str(random.randint(1, 100)) for r in range(1))
#             mappedData = map(int, result.split(","))
#             output = list(mappedData)
#             sumresult = sum(output)
#             sumresult = int(sumresult)
#             msg = f"ダイスロール:{sumresult}\n技能値:{sk}"
#             if sumresult <= judge:
#                 msg1 = f"{sumresult} <= {judge} => 成功"
#             else:
#                 msg1 = f"{sumresult} > {judge} => 失敗"
#             an = f"花難破納の判定結果{sk}を表示します。"   

#     embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
#     await ctx.send(f"{ctx.author.mention}")
#     await ctx.send(embed=embed) 

    
bot.run(token)
