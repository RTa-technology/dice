import os
import re
import traceback
import random
import discord
import urllib.request
import json

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
#=============================== ================#
#Player_data____________________________________#

HP_0191 = 15
MP_0191 = 15
SA_0191 = 65

HP_4091 = 13
MP_4091 = 6
SA_4091 = 30

HP_8199 = 11
MP_8199 = 13
SA_8199 = 65
#===============================================#

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
    
#@bot.event
#async def on_ready():
    # CHANNEL_ID = 706950934013673562 チャンネルID(AT)  
#    CHANNEL_ID = 706969662516101181#チャンネルID(AT)  
#    channel = bot.get_channel(CHANNEL_ID)  
#    await channel.send("Dice-botちゃん参上!")


#===============================================#

@bot.command(name="pray")
async def pray(ctx: str):
    a_id = ctx.author.id
    rand = random.randint(1,7)
    pic  = random.randint(1,100)
    if a_id == ID_7568:
        msg =f"私は前言われたこと忘れてないにゃ。"
        picimg ="https://media.discordapp.net/attachments/683147981456801947/706496315453997076/download20200500222353.png"
    else:
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

@bot.command(name="eew")
async def d(ctx:str):
    msg = "お姉ちゃんをよぶにゃ!"
    embed=discord.Embed(title="呼び出し",description=msg, color=0xbb0011)
    picnerv = "https://media.discordapp.net/attachments/706969662516101181/707545920039813150/download20200503093423.png"
    embed.set_thumbnail(url=picnerv)
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
#    """!id ID表示"""
    embed = discord.Embed(title="Help ID",description="IDを表示します。",color=discord.Colour.from_rgb(0,0,100))
    embed.add_field(name="小沼さん",value="0864",inline=True)
    embed.add_field(name="六谷さん",value="0191",inline=True)
    embed.add_field(name="羅闇さん",value="8199",inline=True)
    embed.add_field(name="マスター",value="4091",inline=True)
    embed.add_field(name="来須さん",value="7568",inline=True)
    embed.add_field(name="Lenzさん",value="4176",inline=True)
    embed.add_field(name="Extraさん",value="4560",inline=True)
    embed.add_field(name="花難破納さん",value="8464",inline=True)
    embed.add_field(name="ぬぬぬさん",value="9995",inline=True)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 

@bot.command(name="h")
async def dice(ctx: str):
#    """!h 短縮help"""
    embed = discord.Embed(title="Help Command",description="各種コマンドの説明を行います。",color=discord.Colour.from_rgb(255,140,0))
    embed.add_field(name="!d",value="`!d {n}d{n}`の書式で入力\n合計値のみ表示",inline=False)
    embed.add_field(name="!dice",value="`!dice {n}d{n}`の書式で入力\n配列表示あり",inline=False)
    embed.add_field(name="!dj",value="`!dj {n}d{n}<k`の書式で入力",inline=False)
    embed.add_field(name="!dp",value="`!dj 技能値?{n}d{n}+k`の書式で入力",inline=False)
    embed.add_field(name="!dd",value="`!dd {n}d{n}+{n}D{n}`の書式で入力",inline=False)
    embed.add_field(name="!p",value="`!p {states}+{N}`の書式で入力\nステータスの表示は!p s",inline=False)
    embed.add_field(name="!m",value="`!m {states}-{N}`の書式で入力\nステータスの表示は!m s",inline=False)
    embed.add_field(name="!h",value="これを表示",inline=False)
    embed.add_field(name="!s",value="`!s {何かを入力}`の書式で能力値を表示",inline=False)
    embed.add_field(name="----------------------------------------------------",value="キーパーメニュー",inline=False)
    embed.add_field(name="!id",value="`!id` IDを表示",inline=False)
    embed.add_field(name="!p",value="`!p {id}&{states}+{N}`の書式で入力\n{id}は各playerの#以降\nステータスの表示は!p s",inline=False)
    embed.add_field(name="!m",value="`!m {id}&{states}-{N}`の書式で入力\n{id}は各playerの#以降\nステータスの表示は!m s",inline=False)
    embed.add_field(name="!s",value="`!s {id}&{何かを入力}`の書式で能力値を表示\n{id}は各playerの#以降",inline=False)
    embed.add_field(name="----------------------------------------------------",value="その他",inline=False)
    embed.add_field(name="!ww",value="`!ww {都市名}`でお姉ちゃんが天気を表示します。\n{都市名}は!w",inline=False)
    embed.add_field(name="!w",value="`!w`表示可能な都市名を表示",inline=False)
    embed.add_field(name="!eew quakeinfo",value="`!eew quakeinfo`直近の地震情報を表示",inline=False)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)  


#===============================================#
@bot.command(name="w")
async def dice(ctx: str):
#    """!id 天気都市表示"""
    embed = discord.Embed(title="Help Weather",description="表示可能な都市名を表示します。",color=discord.Colour.from_rgb(140,196,220))
    embed.add_field(name="東北:宮城県",value="仙台",inline=True)
    embed.add_field(name="関東:東京都",value="東京",inline=True)
    embed.add_field(name="関東:神奈川県",value="横浜",inline=True)
    embed.add_field(name="関東:愛知県",value="名古屋",inline=True)
    embed.add_field(name="関西:大阪",value="大阪",inline=True)
    embed.add_field(name="中国:岡山県",value="岡山",inline=True)
    embed.add_field(name="中国:広島県",value="広島",inline=True)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 
  


@bot.command(name="ww")
async def d(ctx, tenki: str):
#    """!ww {都市名}"""
    if tenki == "仙台":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=040010').read()
    elif tenki =="東京":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010').read()
    elif tenki =="横浜":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=140010').read()
    elif tenki =="名古屋":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=230010').read()
    elif tenki =="大阪":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=270000').read()
    elif tenki =="岡山":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=330010').read()
    elif tenki =="広島":
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=340010').read()    
    resp = json.loads(resp.decode('utf-8'))
    msg = "[bot]" + resp['location']['city']
    msg += "の天気は、\n"
    for f in resp['forecasts']:
        msg += f['dateLabel'] + "が" + f['telop'] + "\n"
        msg += "です。"
    await ctx.send(msg)
    
#===============================================#

@bot.command(name="d")
async def d(ctx, dice: str):
#    """!d {n}d{n}の書式で入力(合計表示のみ)"""
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
#    """!dice {n}d{n}の書式で入力"""
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
#    """!dp {n}d{n}+kの書式で入力"""
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
#    """!dd {n}d{n}+{n}D{n}の書式で入力"""
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
    firesult = sumresult + sumresult2
    mention= f"<@{ctx.author.id}>"
    msg = f"{ctx.author.mention}\n 1:`{result}`\n 2:`{result2}`"
    msg2 = f"{firesult} = {sumresult} + {sumresult2}"
    embed = discord.Embed(title=firesult ,description=f"{mention}\n1:`{result}`\n2:`{result2}`\n{sumresult}\n{msg2}\n{ctx.message.content}",color=discord.Colour.from_rgb(238,139,150))

    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)
    
    
    
@bot.command(name="dj")
async def dj(ctx, dice: str):
#    """!dj {n}d{n}<kの書式で入力"""
    try:
        skills, str0 = map(str, dice.split('d'))
        rolls, str1 = map(str, str0.split('d'))
        limit, judge =map(int, str1.split('<'))
    except Exception:
        await ctx.send('!d NdN<kの書式で入力')
        return
    skills = int(skills)
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
    
    if sumresult = 1:
        msg1 = f"{msg1}\nクリティカル(01)です。"
    elif sumresult >= 96 and skills < 50:
        msg1 = f"{msg1}\nファンブル(96-00)です。"
    elif sumresult = 100 and skills >= 50:
        msg1 = f"{msg1}\nファンブル(00)です。"

        
    msg = f"{ctx.author.mention}\n" + result
    embed = discord.Embed(title=msg1 ,description=f"{mention}\n{result}\n{sumresult}\n{ctx.message.content}",color=discord.Colour.from_rgb(255,0,0))
#     embed.set_author(name=msg1)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

#===============================================#
@bot.command(name="p")
async def s0864(ctx,stu: str):
#   """!p {states}+{N}の書式で入力 ステータスの加算を行います。"""
    global HP_8199
    global MP_8199
    global SA_8199
    
    global HP_0191
    global MP_0191
    global SA_0191
    
    global HP_4091
    global MP_4091
    global SA_4091
    
    
    a_id = ctx.author.id
    if a_id == ID_8199:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の笹山 孝史のステータスを表示します。"
            msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99."
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
        an = f"現在の笹山 孝史のステータスを表示します。"
        msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99."

    elif a_id == ID_0191:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の針替 順弘のステータスを表示します。"
            msg = f"針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99."
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
        an = f"現在の針替 順弘のステータスを表示します。"
        msg = f"針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99."


    elif a_id == ID_4176: #keeper
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, plus = map(str, str1.split('+'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99.\n\n針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99.\n\n鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        plus = int(plus)
        if pl_di == "8199":
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
            an = f"現在の笹山 孝史のステータスを表示します。"
            msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99."
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
            an = f"現在の針替 順弘のステータスを表示します。"
            msg = f"針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99."
        elif pl_di == "4091":
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
                SA_4091 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の鈴木 正和のステータスを表示します。"
            msg = f"鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."


    elif a_id == ID_4091: #admin
        if "&" in stu:
            try:
                pl_di, str1 = map(str, stu.split('&'))
                states, plus = map(str, str1.split('+'))
            except Exception:
                an = f"現在の全Playerのステータスを表示します。"
                msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99.\n\n針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99.\n\n鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."
                embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
                await ctx.send(f"{ctx.author.mention}")
                await ctx.send(embed=embed)    
                return
            plus = int(plus)
            if pl_di == "8199":
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
                an = f"現在の笹山 孝史のステータスを表示します。"
                msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99."
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
                an = f"現在の針替 順弘のステータスを表示します。"
                msg = f"針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99."
            elif pl_di == "4091":
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
                    SA_4091 = san
                    msg1 = f"SANを+{plus}しました。"
                an = f"現在の鈴木 正和のステータスを表示します。"
                msg = f"鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."
        else:
            try:
                states, plus = map(str, stu.split('+'))
            except Exception:
                an = f"現在の鈴木 正和のステータスを表示します。"
                msg = f"鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."
                embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
                await ctx.send(f"{ctx.author.mention}")
                await ctx.send(embed=embed) 
                return
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
                SA_4091 = san
                msg1 = f"SANを+{plus}しました。"
            an = f"現在の鈴木 正和のステータスを表示します。"
            msg = f"鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."

            
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 

#===============================================#

@bot.command(name="m")
async def s0864(ctx,stu: str):
#   """!p {states}-{N}の書式で入力 ステータスの減算を行います。"""
    global HP_8199
    global MP_8199
    global SA_8199
    
    global HP_0191
    global MP_0191
    global SA_0191
    
    global HP_4091
    global MP_4091
    global SA_4091
    
    
    a_id = ctx.author.id
    if a_id == ID_8199:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の笹山 孝史のステータスを表示します。"
            msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99."
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
        an = f"現在の笹山 孝史のステータスを表示します。"
        msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99."

    elif a_id == ID_0191:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の針替 順弘のステータスを表示します。"
            msg = f"針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99."
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
        an = f"現在の針替 順弘のステータスを表示します。"
        msg = f"針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99."


    elif a_id == ID_4176: #keeper
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, minus = map(str, str1.split('-'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99.\n\n針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99.\n\n鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)    
            return
        minus = int(minus)
        if pl_di == "8199":
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
            an = f"現在の笹山 孝史のステータスを表示します。"
            msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99."
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
            an = f"現在の針替 順弘のステータスを表示します。"
            msg = f"針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99."
        elif pl_di == "4091":
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
                SA_4091 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の鈴木 正和のステータスを表示します。"
            msg = f"鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."


    elif a_id == ID_4091: #admin
        if "&" in stu:
            try:
                pl_di, str1 = map(str, stu.split('&'))
                states, minus = map(str, str1.split('-'))
            except Exception:
                an = f"現在の全Playerのステータスを表示します。"
                msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99.\n\n針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99.\n\n鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."
                embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
                await ctx.send(f"{ctx.author.mention}")
                await ctx.send(embed=embed)    
                return
            minus = int(minus)
            if pl_di == "8199":
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
                an = f"現在の笹山 孝史のステータスを表示します。"
                msg = f"笹山 孝史\n耐久値 {HP_8199}/12. MP {MP_8199}/9. 正気度 {SA_8199}/99."
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
                an = f"現在の針替 順弘のステータスを表示します。"
                msg = f"針替 順弘\n耐久値 {HP_0191}/11. MP {MP_0191}/10. 正気度 {SA_0191}/99."
            elif pl_di == "4091":
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
                    SA_4091 = san
                    msg1 = f"SANを-{minus}しました。"
                an = f"現在の鈴木 正和のステータスを表示します。"
                msg = f"鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."
        else:
            try:
                states, minus = map(str, stu.split('-'))
            except Exception:
                an = f"現在の鈴木 正和のステータスを表示します。"
                msg = f"鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."
                embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
                await ctx.send(f"{ctx.author.mention}")
                await ctx.send(embed=embed) 
                return
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
                SA_4091 = san
                msg1 = f"SANを-{minus}しました。"
            an = f"現在の鈴木 正和のステータスを表示します。"
            msg = f"鈴木 正和\n耐久値 {HP_4091}/15. MP {MP_4091}/9. 正気度 {SA_4091}/99."

            
    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed) 


#================================================#
@bot.command(name="s")
async def s(ctx,stu: str):
#    """!s {何でもいい ※ただし何か記述}の書式で入力 技能値の表示を行います。"""
    a_id = ctx.author.id
    if a_id == ID_8199:
        an = f"笹山 孝史の技能値を表示します。"
        msg =f"STR:12　CON:8　POW:9\nDEX:9　APP:5　SIZ:16\nINT:14　EDU:12\n--------------------\nHP:12　MP:9　SAN:45\nアイデア:70　幸運:45　知識:60\n--------------------\n芸術(焼き物):55\n製作(焼き物):50\n地質学:50　図書館:75\n値切り:13　中国語:20\n目星:75　歴史:55　コンピュータ:30\nキック:70"
        msg = f"{an}\n{msg}"
        await ctx.send(f"{ctx.author.mention}")
        await ctx.send(msg) 

    elif a_id == ID_0191:
        an = f"針替 順弘の技能値を表示します。"
        msg = f"STR:14　CON:12　POW:10\nDEX:15　APP:8　SIZ:10\nINT:10　EDU:17\n--------------------\nHP:11　MP:10　SAN:50\nアイデア:50　幸運:50　知識:85\n--------------------\n医学:85　説得:85　信用:75\n生物学:66　薬学:66　キック:60　精神分析:66\n"
        msg = f"{an}\n{msg}"
        await ctx.send(f"{ctx.author.mention}")
        await ctx.send(msg) 


    elif a_id == ID_4176: #keeper
        try:
            pl_di, str1 = map(str, stu.split('&'))
        except Exception:
            an = f"現在の全Playerの能力値を表示します。"
            msg = f"RTaさん\n\nSTR:11　CON:12　POW:9\nDEX:10　APP:14　SIZ:18\nINT:11　EDU:13\n------------------------\nHP:15　MP:9　SAN:45\nアイデア:55　幸運:45　知識:65\n------------------------\n拳銃:40　回避:40　忍び歩き:40\n目星:65　聞き耳:60　ナビゲート:40\n言いくるめ:35　信用:45　説得:55\nオカルト:20　図書館:60　心理学:45　法律:10\n\nぬぬぬさん\n\n\STR:12　CON:8　POW:9\nDEX:9　APP:5　SIZ:16\nINT:14　EDU:12\n--------------------\nHP:12　MP:9　SAN:45\nアイデア:70　幸運:45　知識:60\n--------------------\n芸術(焼き物):55\n製作(焼き物):50\n地質学:50　図書館:75\n値切り:13　中国語:20\n目星:75　歴史:55　コンピュータ:30\nキック:70\n\n六谷さん\n\nSTR:14　CON:12　POW:10\nDEX:15　APP:8　SIZ:10\nINT:10　EDU:17\n--------------------\nHP:11　MP:10　SAN:50\nアイデア:50　幸運:50　知識:85\n--------------------\n医学:85　説得:85　信用:75\n生物学:66　薬学:66　キック:60　精神分析:66\n"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)    
        if pl_di == "8199":
            an = f"笹山 孝史の技能値を表示します。"
            msg =f"STR:12　CON:8　POW:9\nDEX:9　APP:5　SIZ:16\nINT:14　EDU:12\n--------------------\nHP:12　MP:9　SAN:45\nアイデア:70　幸運:45　知識:60\n--------------------\n芸術(焼き物):55\n製作(焼き物):50\n地質学:50　図書館:75\n値切り:13　中国語:20\n目星:75　歴史:55　コンピュータ:30\nキック:70"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg) 

        elif pl_di == "0191":
            an = f"針替 順弘の技能値を表示します。"
            msg = f"STR:14　CON:12　POW:10\nDEX:15　APP:8　SIZ:10\nINT:10　EDU:17\n--------------------\nHP:11　MP:10　SAN:50\nアイデア:50　幸運:50　知識:85\n--------------------\n医学:85　説得:85　信用:75\n生物学:66　薬学:66　キック:60　精神分析:66\n"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg) 

        elif pl_di == "4091":
            an = f"鈴木 正和の技能値を表示します。"
            msg = f"STR:11　CON:12　POW:9\nDEX:10　APP:14　SIZ:18\nINT:11　EDU:13\n------------------------\nHP:15　MP:9　SAN:45\nアイデア:55　幸運:45　知識:65\n------------------------\n拳銃:40　回避:40　忍び歩き:40\n目星:65　聞き耳:60　ナビゲート:40\n言いくるめ:35　信用:45　説得:55\nオカルト:20　図書館:60　心理学:45　法律:10"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)

    elif a_id == ID_4091: #admin
        try:
            pl_di, str1 = map(str, stu.split('&'))
        except Exception:
            an = f"鈴木 正和の技能値を表示します。"
            msg = f"STR:11　CON:12　POW:9\nDEX:10　APP:14　SIZ:18\nINT:11　EDU:13\n------------------------\nHP:15　MP:9　SAN:45\nアイデア:55　幸運:45　知識:65\n------------------------\n拳銃:40　回避:40　忍び歩き:40\n目星:65　聞き耳:60　ナビゲート:40\n言いくるめ:35　信用:45　説得:55\nオカルト:20　図書館:60　心理学:45　法律:10"
            msg = f"{an}\n{msg}"
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed) 
            return
        if pl_di == "8199":
            an = f"笹山 孝史の技能値を表示します。"
            msg =f"STR:12　CON:8　POW:9\nDEX:9　APP:5　SIZ:16\nINT:14　EDU:12\n--------------------\nHP:12　MP:9　SAN:45\nアイデア:70　幸運:45　知識:60\n--------------------\n芸術(焼き物):55\n製作(焼き物):50\n地質学:50　図書館:75\n値切り:13　中国語:20\n目星:75　歴史:55　コンピュータ:30\nキック:70"
            await ctx.send(f"{ctx.author.mention}")


        elif pl_di == "0191":
            an = f"針替 順弘の技能値を表示します。"
            msg = f"STR:14　CON:12　POW:10\nDEX:15　APP:8　SIZ:10\nINT:10　EDU:17\n--------------------\nHP:11　MP:10　SAN:50\nアイデア:50　幸運:50　知識:85\n--------------------\n医学:85　説得:85　信用:75\n生物学:66　薬学:66　キック:60　精神分析:66\n"
            await ctx.send(f"{ctx.author.mention}")


        elif pl_di == "all":
            an = f"現在の全Playerの能力値を表示します。"
            msg = f"RTaさん\n\nSTR:11　CON:12　POW:9\nDEX:10　APP:14　SIZ:18\nINT:11　EDU:13\n------------------------\nHP:15　MP:9　SAN:45\nアイデア:55　幸運:45　知識:65\n------------------------\n拳銃:40　回避:40　忍び歩き:40\n目星:65　聞き耳:60　ナビゲート:40\n言いくるめ:35　信用:45　説得:55\nオカルト:20　図書館:60　心理学:45　法律:10\n\nぬぬぬさん\n\n\STR:12　CON:8　POW:9\nDEX:9　APP:5　SIZ:16\nINT:14　EDU:12\n--------------------\nHP:12　MP:9　SAN:45\nアイデア:70　幸運:45　知識:60\n--------------------\n芸術(焼き物):55\n製作(焼き物):50\n地質学:50　図書館:75\n値切り:13　中国語:20\n目星:75　歴史:55　コンピュータ:30\nキック:70\n\n六谷さん\n\nSTR:14　CON:12　POW:10\nDEX:15　APP:8　SIZ:10\nINT:10　EDU:17\n--------------------\nHP:11　MP:10　SAN:50\nアイデア:50　幸運:50　知識:85\n--------------------\n医学:85　説得:85　信用:75\n生物学:66　薬学:66　キック:60　精神分析:66\n"
            await ctx.send(f"{ctx.author.mention}")

        embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
        await ctx.send(embed=embed) 

bot.run(token)
