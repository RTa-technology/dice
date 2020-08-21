import os
import re
import traceback
import random
import discord
import urllib.request
import json
import time

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
SA_0191 = 75
LU_0191 = 90
HP_4091 = 13
MP_4091 = 6
SA_4091 = 30
LU_4091 = 45
HP_8199 = 11
MP_8199 = 13
SA_8199 = 65
LU_8199 = 60
# mad用
SAN_0191 = 75
SAN_8199 = 65
SAN_4091 = 30
#===============================================#

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_raw_reaction_add(payload):

    if payload.message_id == 746211989545680996:

        print(payload.emoji.name)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

        role = discord.utils.find(lambda r: r.name == payload.emoji.name, guild.roles)

        if role is not None:
            print(role.name + " was found!")
            print(role.id)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            await member.add_roles(role)
            print("done")


@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 746211989545680996:
        print(payload.emoji.name)

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        role = discord.utils.find(lambda r: r.name == payload.emoji.name, guild.roles)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
            print("done")

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
@bot.command(name="roll")
async def d(ctx:str):
    msg = "このメッセージにPlayerもしくはKeeperのサーバー絵文字を付けてください。\n自動的にロール付与を行います。"
    embed=discord.Embed(title="Roll付与をします。",description=msg, color=0xbb0011)
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
    embed.add_field(name="!h",value="これを表示",inline=False)
    embed.add_field(name="!u",value="更新履歴を表示",inline=False)
    embed.add_field(name="----------------------------------------------------",value="Diceメニュー",inline=False)
    embed.add_field(name="!d",value="`!d {n}d{n}`の書式で入力\n合計値のみ表示",inline=False)
    embed.add_field(name="!dice",value="`!dice {n}d{n}`の書式で入力\n配列表示あり",inline=False)
    embed.add_field(name="!dj",value="`!dj {n}d{n}<k`の書式で入力",inline=False)
    embed.add_field(name="!dp",value="`!dj {n}d{n}+k`の書式で入力",inline=False)
    embed.add_field(name="!dd",value="`!dd {n}d{n}+{n}D{n}`の書式で入力",inline=False)
    embed.add_field(name="!p",value="`!p {states}+{N}`の書式で入力\nステータスの表示は!p s",inline=False)
    embed.add_field(name="!m",value="`!m {states}-{N}`の書式で入力\nステータスの表示は!m s",inline=False)
    embed.add_field(name="!s",value="`!s {何かを入力}`の書式で能力値を表示",inline=False)
    embed.add_field(name="!san",value="`!san d`の書式で入力\n1d100のロールを行います。",inline=False)
    embed.add_field(name="----------------------------------------------------",value="キーパーメニュー",inline=False)
    embed.add_field(name="!id",value="`!id` IDを表示",inline=False)
    embed.add_field(name="!p",value="`!p {id}&{states}+{N}`の書式で入力\n{id}は各playerの#以降\nステータスの表示は!p s",inline=False)
    embed.add_field(name="!m",value="`!m {id}&{states}-{N}`の書式で入力\n{id}は各playerの#以降\nステータスの表示は!m s",inline=False)
    embed.add_field(name="!s",value="`!s {id}&{何かを入力}`の書式で能力値を表示\n{id}は各playerの#以降",inline=False)
    embed.add_field(name="!san",value="`!san {id}&d`の書式で入力\nプレイヤーのSAN値1d100のロールを行います。",inline=False)
    embed.add_field(name="----------------------------------------------------",value="その他",inline=False)
    embed.add_field(name="!ww",value="`!ww {都市名}`でお姉ちゃんが天気を表示します。\n{都市名}は!w",inline=False)
    embed.add_field(name="!w",value="`!w`表示可能な都市名を表示",inline=False)
    embed.add_field(name="!eew quakeinfo",value="`!eew quakeinfo`直近の地震情報を表示",inline=False)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

@bot.command(name="u")
async def dice(ctx: str):
#    """!u 更新履歴"""
    # embed = discord.Embed(title="更新履歴",description="2020/08/18にアップデートを行いました。\n以下、アップデートの詳細になります。",color=discord.Colour.from_rgb(255,140,0))
    # embed.add_field(name="!u",value="`!u`\n更新履歴を表示します。",inline=False)
    # embed.add_field(name="!san",value="`!san d`の書式で入力\nSAN値1d100のロールを行います。",inline=False)
    embed = discord.Embed(title="更新履歴",description="2020/08/21にアップデートを行いました。\n以下、アップデートの詳細になります。",color=discord.Colour.from_rgb(255,140,0))
    embed.add_field(name="!san",value="`!san {n}/{n}d{n}`の書式で入力\nSAN値1d100のロールを行い成功失敗に応じて、\nSAN値を減少させます。\n\nこの時、一時的狂気、不定の狂気の判断も行います。",inline=False)
    # embed.add_field(name="----------------------------------------------------",value="更新途中",inline=False)
    embed.add_field(name="!dj",value="第七版のルールで設定を行いました。",inline=False)
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

    if sumresult <= 1:
        msg1 = f"{msg1}\nクリティカル(01)です。"
    elif sumresult >= 96 and judge < 50:
        msg1 = f"{msg1}\nファンブル(96-00)です。"
    elif sumresult == 100 and judge >= 50:
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
    global LU_8199
    global HP_0191
    global MP_0191
    global SA_0191
    global LU_0191
    global HP_4091
    global MP_4091
    global SA_4091
    global LU_4091
    global SAN_0191
    global SAN_4091
    global SAN_8199

    a_id = ctx.author.id
    if a_id == ID_8199:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の安達　一のステータスを表示します。"
            msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99."
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
        elif states == "luck":
            luck = LU_8199 + plus
            LU_8199 = luck
            msg1 = f"LUCKを+{plus}しました。"
        an = f"現在の安達　一のステータスを表示します。"
        msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99."

    elif a_id == ID_0191:
        try:
            states, plus = map(str, stu.split('+'))
        except Exception:
            an = f"現在の倉埼 晋司のステータスを表示します。"
            msg = f"倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99."
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
        elif states == "luck":
            luck = LU_0191 + plus
            LU_0191 = luck
            msg1 = f"LUCKを+{plus}しました。"
        an = f"現在の倉埼 晋司のステータスを表示します。"
        msg = f"倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99."


    elif a_id == ID_4176: #keeper
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, plus = map(str, str1.split('+'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99.\n\n倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99.\n\n伊島 馨\n耐久値 {HP_4091}/13. MP {MP_4091}/6. 正気度 {SA_4091}/99. 幸運 {LU_4091}/99."
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
            elif states == "luck":
                luck = LU_8199 + plus
                LU_8199 = luck
                msg1 = f"LUCKを+{plus}しました。"
            an = f"現在の安達　一のステータスを表示します。"
            msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99."
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
            elif states == "luck":
                luck = LU_0191 + plus
                LU_0191 = luck
                msg1 = f"LUCKを+{plus}しました。"
            an = f"現在の倉埼 晋司のステータスを表示します。"
            msg = f"倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99."
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
            elif states == "luck":
                luck = LU_4091 + plus
                LU_4091 = luck
                msg1 = f"LUCKを+{plus}しました。"
            an = f"現在の伊島 馨のステータスを表示します。"
            msg = f"伊島 馨\n耐久値 {HP_4091}/13. MP {MP_4091}/6. 正気度 {SA_4091}/99. 幸運 {LU_4091}/99."


    elif a_id == ID_4091: #admin
        if "&" in stu:
            try:
                pl_di, str1 = map(str, stu.split('&'))
                states, plus = map(str, str1.split('+'))
            except Exception:
                an = f"現在の全Playerのステータスを表示します。"
                msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99.\n\n倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99.\n\n伊島 馨\n耐久値 {HP_4091}/13. MP {MP_4091}/6. 正気度 {SA_4091}/99. 幸運 {LU_4091}/99."
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
                SAN_8199 = san
                msg1 = f"SANを+{plus}しました。"
            elif states == "luck":
                luck = LU_8199 + plus
                LU_8199 = luck
                msg1 = f"LUCKを+{plus}しました。"
            an = f"現在の安達　一のステータスを表示します。"
            msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99."
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
                SAN_0191 = san
                msg1 = f"SANを+{plus}しました。"
            elif states == "luck":
                luck = LU_0191 + plus
                LU_0191 = luck
                msg1 = f"LUCKを+{plus}しました。"
            an = f"現在の倉埼 晋司のステータスを表示します。"
            msg = f"倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99."
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
                SAN_4091 = san
                msg1 = f"SANを+{plus}しました。"
            elif states == "luck":
                luck = LU_4091 + plus
                LU_4091 = luck
                msg1 = f"LUCKを+{plus}しました。"
            an = f"現在の伊島 馨のステータスを表示します。"
            msg = f"伊島 馨\n耐久値 {HP_4091}/13. MP {MP_4091}/6. 正気度 {SA_4091}/99. 幸運 {LU_4091}/99."


    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

#===============================================#
@bot.command(name="m")
async def s0864(ctx,stu: str):
#   """!p {states}-{N}の書式で入力 ステータスの加算を行います。"""
    global HP_8199
    global MP_8199
    global SA_8199
    global LU_8199
    global HP_0191
    global MP_0191
    global SA_0191
    global LU_0191
    global HP_4091
    global MP_4091
    global SA_4091
    global LU_4091
    global SAN_0191
    global SAN_4091
    global SAN_8199

    a_id = ctx.author.id
    if a_id == ID_8199:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の安達　一のステータスを表示します。"
            msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99."
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
        elif states == "luck":
            luck = LU_8199 - minus
            LU_8199 = luck
            msg1 = f"LUCKを-{minus}しました。"
        an = f"現在の安達　一のステータスを表示します。"
        msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99."

    elif a_id == ID_0191:
        try:
            states, minus = map(str, stu.split('-'))
        except Exception:
            an = f"現在の倉埼 晋司のステータスを表示します。"
            msg = f"倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99."
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
        elif states == "luck":
            luck = LU_0191 - minus
            LU_0191 = luck
            msg1 = f"LUCKを-{minus}しました。"
        an = f"現在の倉埼 晋司のステータスを表示します。"
        msg = f"倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99."


    elif a_id == ID_4176: #keeper
        try:
            pl_di, str1 = map(str, stu.split('&'))
            states, minus = map(str, str1.split('-'))
        except Exception:
            an = f"現在の全Playerのステータスを表示します。"
            msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99.\n\n倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99.\n\n伊島 馨\n耐久値 {HP_4091}/13. MP {MP_4091}/6. 正気度 {SA_4091}/99. 幸運 {LU_4091}/99."
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
            elif states == "luck":
                luck = LU_8199 - minus
                LU_8199 = luck
                msg1 = f"LUCKを-{minus}しました。"
            an = f"現在の安達　一のステータスを表示します。"
            msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99."
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
            elif states == "luck":
                luck = LU_0191 - minus
                LU_0191 = luck
                msg1 = f"LUCKを-{minus}しました。"
            an = f"現在の倉埼 晋司のステータスを表示します。"
            msg = f"倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99."
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
            elif states == "luck":
                luck = LU_4091 - minus
                LU_4091 = luck
                msg1 = f"LUCKを-{minus}しました。"
            an = f"現在の伊島 馨のステータスを表示します。"
            msg = f"伊島 馨\n耐久値 {HP_4091}/13. MP {MP_4091}/6. 正気度 {SA_4091}/99. 幸運 {LU_4091}/99."


    elif a_id == ID_4091: #admin
        if "&" in stu:
            try:
                pl_di, str1 = map(str, stu.split('&'))
                states, minus = map(str, str1.split('-'))
            except Exception:
                an = f"現在の全Playerのステータスを表示します。"
                msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99.\n\n倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99.\n\n伊島 馨\n耐久値 {HP_4091}/13. MP {MP_4091}/6. 正気度 {SA_4091}/99. 幸運 {LU_4091}/99."
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
                SAN_8199 = san
                msg1 = f"SANを-{minus}しました。"
            elif states == "luck":
                luck = LU_8199 - minus
                LU_8199 = luck
                msg1 = f"LUCKを-{minus}しました。"
            an = f"現在の安達　一のステータスを表示します。"
            msg = f"安達　一\n耐久値 {HP_8199}/11. MP {MP_8199}/13. 正気度 {SA_8199}/99. 幸運 {LU_8199}/99."
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
                SAN_0191 = san
                msg1 = f"SANを-{minus}しました。"
            elif states == "luck":
                luck = LU_0191 - minus
                LU_0191 = luck
                msg1 = f"LUCKを-{minus}しました。"
            an = f"現在の倉埼 晋司のステータスを表示します。"
            msg = f"倉埼 晋司\n耐久値 {HP_0191}/15. MP {MP_0191}/15. 正気度 {SA_0191}/99. 幸運 {LU_0191}/99."
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
                SAN_4091 = san
                msg1 = f"SANを-{minus}しました。"
            elif states == "luck":
                luck = LU_4091 - minus
                LU_4091 = luck
                msg1 = f"LUCKを-{minus}しました。"
            an = f"現在の伊島 馨のステータスを表示します。"
            msg = f"伊島 馨\n耐久値 {HP_4091}/13. MP {MP_4091}/6. 正気度 {SA_4091}/99. 幸運 {LU_4091}/99."


    embed = discord.Embed(title=an ,description=f"{msg1}\n結果:\n{msg}",color=discord.Colour.from_rgb(100,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

#===============================================#
#                  STATES                       #
#===============================================#
@bot.command(name="s")
async def s(ctx,stu: str):
#    """!s {何でもいい ※ただし何か記述}の書式で入力 技能値の表示を行います。"""

    global HP_8199
    global MP_8199
    global SA_8199
    global LU_8199
    global HP_0191
    global MP_0191
    global SA_0191
    global LU_0191
    global HP_4091
    global MP_4091
    global SA_4091
    global LU_4091
    a_id = ctx.author.id
    if a_id == ID_8199:
        an = f"安達　一の技能値を表示します。"
        msg =f"STR:45 CON:55 POW:65\nDEX:60 APP:40 SIZ:60\nINT:70 EDU:50\n--------------------\nHP:{HP_8199} MP:{MP_8199} SAN:{SA_8199}\nアイデア:70　幸運:{LU_8199}　知識:50\n--------------------\n精神分析:71目星:80魅惑:85\nコンピューター:80心理学:80"
        msg = f"{an}\n{msg}"
        await ctx.send(f"{ctx.author.mention}")
        await ctx.send(msg)

    elif a_id == ID_0191:
        an = f"倉埼 晋司の技能値を表示します。"
        msg = f"STR:65 CON:70 POW:75\nDEX:25 APP:60 SIZ:80\nINT:65 EDU:50\n--------------------\nHP:{HP_0191} MP:{MP_0191} SAN:{SA_0191}\nアイデア:65 幸運:{LU_0191} 知識:50\n--------------------\nサブマシンガン:70応急手当:70聞き耳:50\n隠密:50図書館:75目星:40\n説得:60威圧:60海:50"
        msg = f"{an}\n{msg}"
        await ctx.send(f"{ctx.author.mention}")
        await ctx.send(msg)


    elif a_id == ID_4176: #keeper
        try:
            pl_di, str1 = map(str, stu.split('&'))
        except Exception:
            an = f"現在の全Playerの能力値を表示します。"
            msg = f"RTaさん\n\nSTR:30 CON:60 POW:30\nDEX:35 APP:25 SIZ:70\nINT:80 EDU:60\n--------------------\nHP:{HP_4091} MP:{MP_4091} SAN:{SA_4091}\nアイデア:80　幸運:{LU_4091}　知識:60\n--------------------\n回避:50応急手当:50精神分析:40\n図書館:60目星:60電気修理:40\n信用:50説得:50日本語:80\n医学:30コンピューター:10心理学:40電子工学:30\n\n羅闇さん\n\n\STR:45 CON:55 POW:65\nDEX:60 APP:40 SIZ:60\nINT:70 EDU:50\n--------------------\nHP:{HP_8199} MP:{MP_8199} SAN:{SA_8199}\nアイデア:70　幸運:{LU_8199}　知識:50\n--------------------\n精神分析:71目星:80魅惑:85\nコンピューター:80心理学:80\n\n六谷さん\n\nSTR:65 CON:70 POW:75\nDEX:25 APP:60 SIZ:80\nINT:65 EDU:50\n--------------------\nHP:{HP_0191} MP:{MP_0191} SAN:{SA_0191}\nアイデア:65 幸運:{LU_0191} 知識:50\n--------------------\nサブマシンガン:70応急手当:70聞き耳:50\n隠密:50図書館:75目星:40\n説得:60威圧:60海:50"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)
        if pl_di == "8199":
            an = f"安達　一の技能値を表示します。"
            msg =f"STR:45 CON:55 POW:65\nDEX:60 APP:40 SIZ:60\nINT:70 EDU:50\n--------------------\nHP:{HP_8199} MP:{MP_8199} SAN:{SA_8199}\nアイデア:70　幸運:{LU_8199}　知識:50\n--------------------\n精神分析:71目星:80魅惑:85\nコンピューター:80心理学:80"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)

        elif pl_di == "0191":
            an = f"倉埼 晋司の技能値を表示します。"
            msg = f"STR:65 CON:70 POW:75\nDEX:25 APP:60 SIZ:80\nINT:65 EDU:50\n--------------------\nHP:{HP_0191} MP:{MP_0191} SAN:{SA_0191}\nアイデア:65 幸運:{LU_0191} 知識:50\n--------------------\nサブマシンガン:70応急手当:70聞き耳:50\n隠密:50図書館:75目星:40\n説得:60威圧:60海:50"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)

        elif pl_di == "4091":
            an = f"伊島 馨の技能値を表示します。"
            msg = f"STR:30 CON:60 POW:30\nDEX:35 APP:25 SIZ:70\nINT:80 EDU:60\n--------------------\nHP:{HP_4091} MP:{MP_4091} SAN:{SA_4091}\nアイデア:80　幸運:{LU_4091}　知識:60\n--------------------\n回避:50応急手当:50精神分析:40\n図書館:60目星:60電気修理:40\n信用:50説得:50日本語:80\n医学:30コンピューター:10心理学:40電子工学:30"
            msg = f"{an}\n{msg}"
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(msg)

    elif a_id == ID_4091: #admin
        try:
            pl_di, str1 = map(str, stu.split('&'))
        except Exception:
            an = f"伊島 馨の技能値を表示します。"
            msg = f"STR:30 CON:60 POW:30\nDEX:35 APP:25 SIZ:70\nINT:80 EDU:60\n--------------------\nHP:{HP_4091} MP:{MP_4091} SAN:{SA_4091}\nアイデア:80　幸運:{LU_4091}　知識:60\n--------------------\n回避:50応急手当:50精神分析:40\n図書館:60目星:60電気修理:40\n信用:50説得:50日本語:80\n医学:30コンピューター:10心理学:40電子工学:30"
            msg = f"{an}\n{msg}"
            embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)
            return
        if pl_di == "8199":
            an = f"安達　一の技能値を表示します。"
            msg =f"STR:45 CON:55 POW:65\nDEX:60 APP:40 SIZ:60\nINT:70 EDU:50\n--------------------\nHP:{HP_8199} MP:{MP_8199} SAN:{SA_8199}\nアイデア:70　幸運:{LU_8199}　知識:50\n--------------------\n精神分析:71目星:80魅惑:85\nコンピューター:80心理学:80"
            await ctx.send(f"{ctx.author.mention}")


        elif pl_di == "0191":
            an = f"倉埼 晋司の技能値を表示します。"
            msg = f"STR:65 CON:70 POW:75\nDEX:25 APP:60 SIZ:80\nINT:65 EDU:50\n--------------------\nHP:{HP_0191} MP:{MP_0191} SAN:{SA_0191}\nアイデア:65 幸運:{LU_0191} 知識:50\n--------------------\nサブマシンガン:70応急手当:70聞き耳:50\n隠密:50図書館:75目星:40\n説得:60威圧:60海:50"
            await ctx.send(f"{ctx.author.mention}")


        elif pl_di == "all":
            an = f"現在の全Playerの能力値を表示します。"
            msg = f"RTaさん\n\nSTR:30 CON:60 POW:30\nDEX:35 APP:25 SIZ:70\nINT:80 EDU:60\n--------------------\nHP:{HP_4091} MP:{MP_4091} SAN:{SA_4091}\nアイデア:80　幸運:{LU_4091}　知識:60\n--------------------\n回避:50応急手当:50精神分析:40\n図書館:60目星:60電気修理:40\n信用:50説得:50日本語:80\n医学:30コンピューター:10心理学:40電子工学:30\n\n羅闇さん\n\n\STR:45 CON:55 POW:65\nDEX:60 APP:40 SIZ:60\nINT:70 EDU:50\n--------------------\nHP:{HP_8199} MP:{MP_8199} SAN:{SA_8199}\nアイデア:70　幸運:{LU_8199}　知識:50\n--------------------\n精神分析:71目星:80魅惑:85\nコンピューター:80心理学:80\n\n六谷さん\n\nSTR:65 CON:70 POW:75\nDEX:25 APP:60 SIZ:80\nINT:65 EDU:50\n--------------------\nHP:{HP_0191} MP:{MP_0191} SAN:{SA_0191}\nアイデア:65 幸運:{LU_0191} 知識:50\n--------------------\nサブマシンガン:70応急手当:70聞き耳:50\n隠密:50図書館:75目星:40\n説得:60威圧:60海:50"
            await ctx.send(f"{ctx.author.mention}")

        embed = discord.Embed(title=an ,description=msg,color=discord.Colour.from_rgb(87,100,74))
        await ctx.send(embed=embed)

#===============================================#
#                  SAN                          #
#===============================================#
@bot.command(name="san")
async def s0864(ctx,stu: str):
#   """!sanの書式で入力 ステータスの加算を行います。"""
    global SA_8199
    global SA_0191
    global SA_4091
    global SAN_0191
    global SAN_4091
    global SAN_8199

    a_id = ctx.author.id
    if a_id == ID_8199:
        try:
            succ, str1 = map(str, stu.split('/'))
            rolls, limit = map(int, str1.split('d'))
        except Exception:
            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            if sumresult <= SA_8199:
                msg = f"成功"
                msg1 = f"{sumresult} <= {SA_8199} => 成功"
            else:
                msg = f"失敗"
                msg1 = f"{sumresult} > {SA_8199} => 失敗"
            embed = discord.Embed(title=msg ,description=msg1,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)
            return
        succ = int(succ)
        result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        mappedData = map(int, result.split(","))
        output = list(mappedData)
        sumresult = sum(output)
        sumresult = int(sumresult)
        if sumresult <= SA_8199:
            msg = f"成功"
            msg1 = f"{sumresult} <= {SA_8199} => 成功"
            san_j = SA_8199 - succ
            SA_8199 = san_j
            msg1 = f"{msg1}\nSANを-{succ}しました。\n現在のSAN値は{SA_8199}です。"
            if succ >= 5:
                msg2 = f"SAN値ロール\n出目:**{sumresult}**\nより{sumresult} <= {SA_8199} => 成功でした。"
                await ctx.send(msg2)
                msg3 = f"また、SAN値が一度に5ポイント以上減ったので\n一時的狂気の条件を満たしました。\n3秒後にアイデアロールを実行します。\nアイデアロール成功で狂気に陥ります。"
                await ctx.send(msg3)
                time.sleep(3)
                result_m = ', '.join(str(random.randint(1, 100)) for r in range(1))
                mappedData_m = map(int, result_m.split(","))
                output_m = list(mappedData_m)
                sumresult_m = sum(output_m)
                sumresult_m = int(sumresult_m)
                if 70 >= sumresult_m:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} <= 70 => アイデアロール成功により一時的狂気に陥りました。\n`!mad t`を行ってください。"
                    await ctx.send(msg2)
                else:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} > 70 => アイデアロール失敗により回避しました。**良かったですね。**"
                    await ctx.send(msg2)
            if ((SAN_8199 - SA_8199) * 5) >= SAN_8199:
                msg2 = f"SAN値が一時間に2割以上減ったので\n不定の狂気の条件を満たしました。\n`!mad i`を行ってください。"
                await ctx.send(msg2)
        else:
            msg = f"失敗"
            msg1 = f"{sumresult} > {SA_8199} => 失敗"
            result_j = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            mappedData_j = map(int, result_j.split(","))
            output_j = list(mappedData_j)
            sumresult_j = sum(output_j)
            minus_j = int(sumresult_j)
            san_j = SA_8199 - minus_j
            SA_8199 = san_j
            msg1 = f"{msg1}\n{rolls}d{limit}のロールを行います。\n出目:**{result_j}**\nSANを-{minus_j}しました。\n現在のSAN値は{SA_8199}です。"
            if minus_j >= 5:
                msg2 = f"SAN値ロール\n出目:**{sumresult}**\nより{sumresult} > {SA_8199} => 失敗でした。"
                await ctx.send(msg2)
                msg3 = f"また、SAN値が一度に5ポイント以上減ったので\n一時的狂気の条件を満たしました。\n3秒後にアイデアロールを実行します。\nアイデアロール成功で狂気に陥ります。"
                await ctx.send(msg3)
                time.sleep(3)
                result_m = ', '.join(str(random.randint(1, 100)) for r in range(1))
                mappedData_m = map(int, result_m.split(","))
                output_m = list(mappedData_m)
                sumresult_m = sum(output_m)
                sumresult_m = int(sumresult_m)
                if 70 >= sumresult_m:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} <= 70 => アイデアロール成功により一時的狂気に陥りました。\n`!mad t`を行ってください。"
                    await ctx.send(msg2)
                else:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} > 70 => アイデアロール失敗により回避しました。**良かったですね。**"
                    await ctx.send(msg2)
            if ((SAN_8199 - SA_8199) * 5) >= SAN_8199:
                msg2 = f"SAN値が一時間に2割以上減ったので\n不定の狂気の条件を満たしました。\n`!mad i`を行ってください。"
                await ctx.send(msg2)


    elif a_id == ID_0191:
        try:
            succ, str1 = map(str, stu.split('/'))
            rolls, limit = map(int, str1.split('d'))
        except Exception:
            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            if sumresult <= SA_0191:
                msg = f"成功"
                msg1 = f"{sumresult} <= {SA_0191} => 成功"
            else:
                msg = f"失敗"
                msg1 = f"{sumresult} > {SA_0191} => 失敗"
            embed = discord.Embed(title=msg ,description=msg1,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)
            return
        succ = int(succ)
        result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        mappedData = map(int, result.split(","))
        output = list(mappedData)
        sumresult = sum(output)
        sumresult = int(sumresult)
        if sumresult <= SA_0191:
            msg = f"成功"
            msg1 = f"{sumresult} <= {SA_0191} => 成功"
            san_j = SA_0191 - succ
            SA_0191 = san_j
            msg1 = f"{msg1}\nSANを-{succ}しました。\n現在のSAN値は{SA_0191}です。"
            if succ >= 5:
                msg2 = f"SAN値ロール\n出目:**{sumresult}**\nより{sumresult} <= {SA_0191} => 成功でした。"
                await ctx.send(msg2)
                msg3 = f"また、SAN値が一度に5ポイント以上減ったので\n一時的狂気の条件を満たしました。\n3秒後にアイデアロールを実行します。\nアイデアロール成功で狂気に陥ります。"
                await ctx.send(msg3)
                time.sleep(3)
                result_m = ', '.join(str(random.randint(1, 100)) for r in range(1))
                mappedData_m = map(int, result_m.split(","))
                output_m = list(mappedData_m)
                sumresult_m = sum(output_m)
                sumresult_m = int(sumresult_m)
                if 65 >= sumresult_m:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} <= 65 => アイデアロール成功により一時的狂気に陥りました。\n`!mad t`を行ってください。"
                    await ctx.send(msg2)
                else:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} > 65 => アイデアロール失敗により回避しました。**良かったですね。**"
                    await ctx.send(msg2)
            if ((SAN_0191 - SA_0191) * 5) >= SAN_0191:
                msg2 = f"SAN値が一時間に2割以上減ったので\n不定の狂気の条件を満たしました。\n`!mad i`を行ってください。"
                await ctx.send(msg2)
        else:
            msg = f"失敗"
            msg1 = f"{sumresult} > {SA_0191} => 失敗"
            result_j = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            mappedData_j = map(int, result_j.split(","))
            output_j = list(mappedData_j)
            sumresult_j = sum(output_j)
            minus_j = int(sumresult_j)
            san_j = SA_0191 - minus_j
            SA_0191 = san_j
            msg1 = f"{msg1}\n{rolls}d{limit}のロールを行います。\n出目:**{result_j}**\nSANを-{minus_j}しました。\n現在のSAN値は{SA_0191}です。"
            if minus_j >= 5:
                msg2 = f"SAN値ロール\n出目:**{sumresult}**\nより{sumresult} > {SA_0191} => 失敗でした。"
                await ctx.send(msg2)
                msg3 = f"また、SAN値が一度に5ポイント以上減ったので\n一時的狂気の条件を満たしました。\n3秒後にアイデアロールを実行します。\nアイデアロール成功で狂気に陥ります。"
                await ctx.send(msg3)
                time.sleep(3)
                result_m = ', '.join(str(random.randint(1, 100)) for r in range(1))
                mappedData_m = map(int, result_m.split(","))
                output_m = list(mappedData_m)
                sumresult_m = sum(output_m)
                sumresult_m = int(sumresult_m)
                if 65 >= sumresult_m:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} <= 65 => アイデアロール成功により一時的狂気に陥りました。\n`!mad t`を行ってください。"
                    await ctx.send(msg2)
                else:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} > 65 => アイデアロール失敗により回避しました。**良かったですね。**"
                    await ctx.send(msg2)
            if ((SAN_0191 - SA_0191) * 5) >= SAN_0191:
                msg2 = f"SAN値が一時間に2割以上減ったので\n不定の狂気の条件を満たしました。\n`!mad i`を行ってください。"
                await ctx.send(msg2)


    #elif a_id == ID_4176: #keeper
    #     try:
    #         pl_di, str1 = map(str, stu.split('&'))
    #         succ, str2 = map(str, str1.split('/'))
    #         rolls, limit = map(int, str2.split('d'))
    #     except Exception:
    #         msg = f"現在の全PlayerのSAN値を表示します。"
    #         msg1 = f"安達　一\n正気度 {SA_8199}/99.\n倉埼 晋司\n正気度 {SA_0191}/99.\n伊島 馨\n正気度 {SA_4091}/99."
    #         embed = discord.Embed(title=msg ,description=msg1,color=discord.Colour.from_rgb(87,100,74))
    #         await ctx.send(f"{ctx.author.mention}")
    #         await ctx.send(embed=embed)
    #         return
    #     if pl_di == "8199":
    #         succ = int(succ)
    #         result = ', '.join(str(random.randint(1, 100)) for r in range(1))
    #         mappedData = map(int, result.split(","))
    #         output = list(mappedData)
    #         sumresult = sum(output)
    #         sumresult = int(sumresult)
    #         if sumresult <= SA_8199:
    #             msg = f"成功"
    #             msg1 = f"{sumresult} <= {SA_8199} => 成功"
    #             san_j = SA_8199 - succ
    #             SA_8199 = san_j
    #             msg1 = f"{msg1}\nSANを-{succ}しました。"
    #             return msg, msg1
    #         else:
    #             msg = f"失敗"
    #             msg1 = f"{sumresult} > {SA_8199} => 失敗"
    #             result_j = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    #             mappedData_j = map(int, result_j.split(","))
    #             output_j = list(mappedData_j)
    #             sumresult_j = sum(output_j)
    #             minus_j = int(sumresult_j)
    #             san_j = SA_8199 - minus_j
    #             SA_8199 = san_j
    #             msg1 = f"{msg1}\n出目:{result_j}\nSANを-{minus_j}しました。"
    #             return msg, msg1
    #     elif pl_di == "0191":
    #         succ = int(succ)
    #         result = ', '.join(str(random.randint(1, 100)) for r in range(1))
    #         mappedData = map(int, result.split(","))
    #         output = list(mappedData)
    #         sumresult = sum(output)
    #         sumresult = int(sumresult)
    #         if sumresult <= SA_0191:
    #             msg = f"成功"
    #             msg1 = f"{sumresult} <= {SA_0191} => 成功"
    #             san_j = SA_0191 - succ
    #             SA_0191 = san_j
    #             msg1 = f"{msg1}\nSANを-{succ}しました。"
    #             return msg, msg1
    #         else:
    #             msg = f"失敗"
    #             msg1 = f"{sumresult} > {SA_0191} => 失敗"
    #             result_j = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    #             mappedData_j = map(int, result_j.split(","))
    #             output_j = list(mappedData_j)
    #             sumresult_j = sum(output_j)
    #             minus_j = int(sumresult_j)
    #             san_j = SA_0191 - minus_j
    #             SA_0191 = san_j
    #             msg1 = f"{msg1}\n出目:{result_j}\nSANを-{minus_j}しました。"
    #             return msg, msg1
    #     elif pl_di == "4091":
    #         succ = int(succ)
    #         result = ', '.join(str(random.randint(1, 100)) for r in range(1))
    #         mappedData = map(int, result.split(","))
    #         output = list(mappedData)
    #         sumresult = sum(output)
    #         sumresult = int(sumresult)
    #         if sumresult <= SA_4091:
    #             msg = f"成功"
    #             msg1 = f"{sumresult} <= {SA_4091} => 成功"
    #             san_j = SA_4091 - succ
    #             SA_4091 = san_j
    #             msg1 = f"{msg1}\nSANを-{succ}しました。"
    #             return msg, msg1
    #         else:
    #             msg = f"失敗"
    #             msg1 = f"{sumresult} > {SA_4091} => 失敗"
    #             result_j = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    #             mappedData_j = map(int, result_j.split(","))
    #             output_j = list(mappedData_j)
    #             sumresult_j = sum(output_j)
    #             minus_j = int(sumresult_j)
    #             san_j = SA_4091 - minus_j
    #             SA_4091 = san_j
    #             msg1 = f"{msg1}\n出目:{result_j}\nSANを-{minus_j}しました。"
    #             return msg, msg1

    elif a_id == ID_4091: #admin
        try:
            succ, str1 = map(str, stu.split('/'))
            rolls, limit = map(int, str1.split('d'))
        except Exception:
            result = ', '.join(str(random.randint(1, 100)) for r in range(1))
            mappedData = map(int, result.split(","))
            output = list(mappedData)
            sumresult = sum(output)
            sumresult = int(sumresult)
            if sumresult <= SA_4091:
                msg = f"成功"
                msg1 = f"{sumresult} <= {SA_4091} => 成功"
            else:
                msg = f"失敗"
                msg1 = f"{sumresult} > {SA_4091} => 失敗"
            embed = discord.Embed(title=msg ,description=msg1,color=discord.Colour.from_rgb(87,100,74))
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(embed=embed)
            return
        succ = int(succ)
        result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        mappedData = map(int, result.split(","))
        output = list(mappedData)
        sumresult = sum(output)
        sumresult = int(sumresult)
        if sumresult <= SA_4091:
            msg = f"成功"
            msg1 = f"{sumresult} <= {SA_4091} => 成功"
            san_j = SA_4091 - succ
            SA_4091 = san_j
            msg1 = f"{msg1}\nSANを-{succ}しました。\n現在のSAN値は{SA_4091}です。"
            if succ >= 5:
                msg2 = f"SAN値ロール\n出目:**{sumresult}**\nより{sumresult} <= {SA_4091} => 成功でした。"
                await ctx.send(msg2)
                msg3 = f"また、SAN値が一度に5ポイント以上減ったので\n一時的狂気の条件を満たしました。\n3秒後にアイデアロールを実行します。\nアイデアロール成功で狂気に陥ります。"
                await ctx.send(msg3)
                time.sleep(3)
                result_m = ', '.join(str(random.randint(1, 100)) for r in range(1))
                mappedData_m = map(int, result_m.split(","))
                output_m = list(mappedData_m)
                sumresult_m = sum(output_m)
                sumresult_m = int(sumresult_m)
                if 80 >= sumresult_m:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} <= 80 => アイデアロール成功により一時的狂気に陥りました。\n`!mad t`を行ってください。"
                    await ctx.send(msg2)
                else:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} > 80 => アイデアロール失敗により回避しました。**良かったですね。**"
                    await ctx.send(msg2)
            if ((SAN_4091 - SA_4091) * 5) >= SAN_4091:
                msg2 = f"SAN値が一時間に2割以上減ったので\n不定の狂気の条件を満たしました。\n`!mad i`を行ってください。"
                await ctx.send(msg2)

        else:
            msg = f"失敗"
            msg1 = f"{sumresult} > {SA_4091} => 失敗"
            result_j = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            mappedData_j = map(int, result_j.split(","))
            output_j = list(mappedData_j)
            sumresult_j = sum(output_j)
            minus_j = int(sumresult_j)
            san_j = SA_4091 - minus_j
            SA_4091 = san_j
            msg1 = f"{msg1}\n{rolls}d{limit}のロールを行います。\nSAN値ロール 出目:**{result_j}**\nSANを-{minus_j}しました。\n現在のSAN値は{SA_4091}です。"
            if minus_j >= 5:
                msg2 = f"SAN値ロール\n出目:**{sumresult}**\nより{sumresult} > {SA_4091} => 失敗でした。"
                await ctx.send(msg2)
                msg3 = f"また、SAN値が一度に5ポイント以上減ったので\n一時的狂気の条件を満たしました。\n3秒後にアイデアロールを実行します。\nアイデアロール成功で狂気に陥ります。"
                await ctx.send(msg3)
                time.sleep(3)
                result_m = ', '.join(str(random.randint(1, 100)) for r in range(1))
                mappedData_m = map(int, result_m.split(","))
                output_m = list(mappedData_m)
                sumresult_m = sum(output_m)
                sumresult_m = int(sumresult_m)
                if 80 >= sumresult_m:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} <= 80 => アイデアロール成功により一時的狂気に陥りました。\n`!mad t`を行ってください。"
                    await ctx.send(msg2)
                else:
                    msg2 = f"アイデアロール:1d100\n出目:{sumresult_m}\nより、{sumresult_m} > 80 => アイデアロール失敗により回避しました。**良かったですね。**"
                    await ctx.send(msg2)
            if ((SAN_4091 - SA_4091) * 5) >= SAN_4091:
                msg2 = f"SAN値が一時間に2割以上減ったので\n不定の狂気の条件を満たしました。\n`!mad i`を行ってください。"
                await ctx.send(msg2)


        # try:
        #     pl_di, str1 = map(str, stu.split('&'))
        #     succ, str2 = map(str, str1.split('/'))
        #     rolls, limit = map(int, str2.split('d'))
        # except Exception:
        #     result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        #     mappedData = map(int, result.split(","))
        #     output = list(mappedData)
        #     sumresult = sum(output)
        #     sumresult = int(sumresult)
        #     if sumresult <= SA_4091:
        #         msg = f"ID=4091 成功"
        #         msg1 = f"{sumresult} <= {SA_4091} => 成功"
        #     else:
        #         msg = f"ID=4091 失敗"
        #         msg1 = f"{sumresult} > {SA_4091} => 失敗"
        #     embed = discord.Embed(title=msg ,description=msg1,color=discord.Colour.from_rgb(87,100,74))
        #     await ctx.send(f"{ctx.author.mention}")
        #     await ctx.send(embed=embed)
        #     return
        # if pl_di == "8199":
        #     succ = int(succ)
        #     result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        #     mappedData = map(int, result.split(","))
        #     output = list(mappedData)
        #     sumresult = sum(output)
        #     sumresult = int(sumresult)
        #     if sumresult <= SA_8199:
        #         msg = f"成功"
        #         msg1 = f"{sumresult} <= {SA_8199} => 成功"
        #         san_j = SA_8199 - succ
        #         SA_8199 = san_j
        #         msg1 = f"{msg1}\nSANを-{succ}しました。"
        #     else:
        #         msg = f"失敗"
        #         msg1 = f"{sumresult} > {SA_8199} => 失敗"
        #         result_j = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        #         mappedData_j = map(int, result_j.split(","))
        #         output_j = list(mappedData_j)
        #         sumresult_j = sum(output_j)
        #         minus_j = int(sumresult_j)
        #         san_j = SA_8199 - minus_j
        #         SA_8199 = san_j
        #         msg1 = f"{msg1}\n出目:{result_j}\nSANを-{minus_j}しました。"
        #     return
        # elif pl_di == "0191":
        #     succ = int(succ)
        #     result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        #     mappedData = map(int, result.split(","))
        #     output = list(mappedData)
        #     sumresult = sum(output)
        #     sumresult = int(sumresult)
        #     if sumresult <= SA_0191:
        #         msg = f"成功"
        #         msg1 = f"{sumresult} <= {SA_0191} => 成功"
        #         san_j = SA_0191 - succ
        #         SA_0191 = san_j
        #         msg1 = f"{msg1}\nSANを-{succ}しました。"
        #     else:
        #         msg = f"失敗"
        #         msg1 = f"{sumresult} > {SA_0191} => 失敗"
        #         result_j = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        #         mappedData_j = map(int, result_j.split(","))
        #         output_j = list(mappedData_j)
        #         sumresult_j = sum(output_j)
        #         minus_j = int(sumresult_j)
        #         san_j = SA_0191 - minus_j
        #         SA_0191 = san_j
        #         msg1 = f"{msg1}\n出目:{result_j}\nSANを-{minus_j}しました。"
        #     return
        # elif pl_di == "4091":
        #     succ = int(succ)
        #     result = ', '.join(str(random.randint(1, 100)) for r in range(1))
        #     mappedData = map(int, result.split(","))
        #     output = list(mappedData)
        #     sumresult = sum(output)
        #     sumresult = int(sumresult)
        #     if sumresult <= SA_4091:
        #         msg = f"成功"
        #         msg1 = f"{sumresult} <= {SA_4091} => 成功"
        #         san_j = SA_4091 - succ
        #         SA_4091 = san_j
        #         msg1 = f"{msg1}\nSANを-{succ}しました。"
        #     else:
        #         msg = f"失敗"
        #         msg1 = f"{sumresult} > {SA_4091} => 失敗"
        #         result_j = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        #         mappedData_j = map(int, result_j.split(","))
        #         output_j = list(mappedData_j)
        #         sumresult_j = sum(output_j)
        #         minus_j = int(sumresult_j)
        #         san_j = SA_4091 - minus_j
        #         SA_4091 = san_j
        #         msg1 = f"{msg1}\n出目:{result_j}\nSANを-{minus_j}しました。"
        #     return
    embed = discord.Embed(title=msg ,description=msg1,color=discord.Colour.from_rgb(87,100,74))
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

@bot.command(name="mad")
async def pray(ctx,stu: str):
    rand = random.randint(1,10)
    if stu == "t":
        an = "一時的狂気"
        if rand == 1:
            msg = f"出目:1\n気絶あるいは金切り声の発作"
        elif rand == 2:
            msg = f"出目:2\nパニック状態で逃げ出す"
        elif rand == 3:
            msg = f"出目:3\n肉体的なヒステリーあるいは感情の噴出(大笑い、大泣きなど)"
        elif rand == 4:
            msg = f"出目:4\n早口でぶつぶつ言う意味不明の会話あるいは多弁症(一貫した会話の奔流)"
        elif rand == 5:
            msg = f"出目:5\n探索者をその場に釘づけにしてしまうかもしれないような極度の恐怖症"
        elif rand == 6:
            msg = f"出目:6\n殺人癖あるいは自殺癖"
        elif rand == 7:
            msg = f"出目:7\n幻覚あるいは妄想"
        elif rand == 8:
            msg = f"出目:8\n反響動作あるいは反響言語(探索者は周りの者の動作あるいは発言を反復する)"
        elif rand == 9:
            msg = f"出目:9\n奇妙なもの、異様なものを食べたがる(泥、粘着物、人肉など)"
        elif rand == 10:
            msg = f"出目:10\n昏迷(胎児のような姿勢をとる、物事を忘れる)あるいは緊張症(我慢することはできるが意思も興味もない。\n強制的に単純な行動をとらせることはできるが、自発的に行動することはない)"
    elif stu == "i":
        an = "不定の狂気"
        if rand == 1:
            msg = f"出目:1\n健忘症(親しい者のことを最初に忘れる。\n言語や肉体的な技能は働くが、知的な技能は働かない)あるいは昏迷/緊張症"
        elif rand == 2:
            msg = f"出目:2\n激しい恐怖症(逃げ出すことはできるが、恐怖の対象はどこへ行っても見える)"
        elif rand == 3:
            msg = f"出目:3\n幻覚"
        elif rand == 4:
            msg = f"出目:4\n奇妙な性的嗜好(過剰性欲、奇形愛好症など)"
        elif rand == 5:
            msg = f"出目:5\nフェティッシュ(探索者はある物、ある種類の物、人物に対し異常なまでに執着する)"
        elif rand == 6:
            msg = f"出目:6\n制御不能のチック、震え、あるいは会話や文章で人と交流することができなくなる"
        elif rand == 7:
            msg = f"出目:7\n心因性視覚障害、心因性難聴、単数あるいは複数の四肢の機能障害"
        elif rand == 8:
            msg = f"出目:8\n短期的の心因反応(支離滅裂、妄想、常軌を逸した振る舞い、幻覚など)"
        elif rand == 9:
            msg = f"出目:9\n一時的偏執症"
        elif rand == 10:
            msg = f"出目:10\n強迫観念に取り付かれた行動\n(手を洗い続ける、祈る、特定のリズムで歩く、割れ目をまたがない、銃を絶え間なくチェックし続けるなど)"
    embed=discord.Embed(title=an, description=msg, color=0xC7EAEA)
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)
#===============================================#
#===============================================#
bot.run(token)
