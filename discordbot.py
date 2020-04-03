import os
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
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    mappedData = map(int, result.split(","))
    output = list(mappedData)
    sumresult = sum(output)
    msg = f"{ctx.author.mention}\n" + result
    await ctx.send(msg)
    await ctx.send(sumresult)

@bot.command(name="d+")
async def d(ctx, dice: str):
    """{n}d{n}+{k}の書式で入力"""
    try:
        rolls, limplus = map(int, dice.split('d'))
        limit, plus=map(int,limplus.split('+'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    mappedData = map(int, result.split(","))
    output = list(mappedData)
    sumresult = sum(output) + plus
    msg = f"{ctx.author.mention}\n" + result
    await ctx.send(msg)
    await ctx.send(sumresult)
    
@bot.command(name="dice")
async def dice(ctx, dice: str):
    """{n}d{n}の書式で入力"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    embed = discord.Embed(title=f"{ctx.message.content}",description=f"{ctx.author.name}",color=discord.Colour.from_rgb(255,0,0))
    embed.set_author(name=result)
    
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(embed=embed)

#class JapaneseHelpCommand(commands.DefaultHelpCommand):
#   def __init__(self):
#        super().__init__()
#        self.commands_heading = "コマンド:"
#        self.no_category = "その他"
#        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"
#
#    def get_ending_note(self):
#        return (f"各コマンドの説明: $help <コマンド名>\n"
#                f"各カテゴリの説明: $help <カテゴリ名>\n")
#


bot.run(token)
