import discord
import asyncio
from discord.ext import commands
import time
import random
from discord.utils import get
from dice import *
import os

shop = commands.Bot(command_prefix='#')

@shop.event
async def on_ready():
    print('디스코드 테스트 봇')
    print(shop.user.name)
    game = discord.Game('#도움말 확인해줘요 :D')
    await shop.change_presence(status=discord.Status.idle, activity=game)

@shop.command()
async def 안녕(ctx):
    tag = '<@{}>'.format(ctx.author.id)
    await ctx.send('만나서 반가워, ' + tag)

@shop.command()
async def 핑(ctx):
    await ctx.send(f'퐁! {round(round(shop.latency, 4)*1000)}ms가 걸렸어요!')

@shop.command()
async def 주사위(ctx):

    await ctx.channel.purge(limit = 1)

    result, _color, bot, user = dice()
    embed = discord.Embed(title = "주사위게임 결과", description = "랜덤하게 결정되는 주사위에 몸을 맡겨봐~" , color = _color)
    embed.add_field(name = "게임 봇의 숫자", value = bot, inline = True)
    embed.add_field(name = ctx.author.name+"의 숫자", value = user, inline = True)
    embed.set_footer(text = result)
    await ctx.send(embed = embed)

@shop.command()
async def 도움말(ctx):

    await ctx.channel.purge(limit = 1)

    embed = discord.Embed(title = "도움말", description = "디스코드 봇 명령어를 알려드려요!", color = 0x00FF56)
    embed.add_field(name = "#주사위", value = "디스코드 봇과 주사위 대결을 할 수 있습니다.", inline = False)
    embed.add_field(name = "#대출", value = "#대출 [채권자] [채무자] [아이템] 으로 작성이 가능합니다.", inline = False)
    embed.add_field(name = "#판매 / #구매", value = "#판매(구매) [거래 대상 게임] [희망 아이템] 으로 작성이 가능합니다.", inline = False)
    embed.add_field(name = "개발 중...", value = "개발 중입니다...", inline = False)
    embed.set_footer(text = ctx.author.name+"님의 궁금증이 풀리셨나요?")
    await ctx.send(embed = embed)

@shop.command()
async def 대출(ctx, ctx1 = None, ctx2 = None, *, text = None):

    if ctx1 != None and ctx2 != None and text != None:

        await ctx.channel.purge(limit = 1)
        
        seller = str(ctx1)
        buyer = str(ctx2)
        item = str(text)
        
        embed = discord.Embed(title = "대출 확인 글 \U0001F4B0", description = "대출한 내역을 확인하는 글입니다.", color = 0xFF5500)
        embed.add_field(name = "채권자 닉네임", value = seller, inline = False)
        embed.add_field(name = "채무자 닉네임", value = buyer, inline = False)
        embed.add_field(name = "빌려간 금액 또는 아이템", value = item, inline = False)
        embed.set_footer(text = "작성자는 "+ ctx.author.name +"님입니다. 상환 완료 시 FREE를 눌러주세요.")
        msg = await ctx.send(embed = embed)
        await msg.add_reaction("\U0001f193")

    else:

        embed = discord.Embed(title = "대출 명령어 소개 \U0001F4B0", description = "대출 명령어를 확인할 수 있습니다.", color = 0xFF5500)
        embed.add_field(name = "#대출 [채권자] [채무자] [빌려간 아이템]", value = "채무자에게 채권자가 빌려간 아이템을 작성할 수 있습니다.", inline = False)
        embed.set_footer(text = ctx.author.name + "님의 궁금증이 풀리셨나요?")
        await ctx.send(embed = embed)

@shop.command()
async def 구매(ctx, ctx1 = None, *, text = None):

    if ctx1 != None and text != None:

        await ctx.channel.purge(limit = 1)

        game = str(ctx1)
        item = str(text)
        

        embed = discord.Embed(title = "아이템 구매 글 \U0001F9F1", description = ctx.author.name + "님이 아이템의 판매자를 찾는 글입니다.", color = 0x9CFF00)
        embed.add_field(name = "거래 대상 게임", value = game, inline = False)
        embed.add_field(name = "구매 희망 아이템", value = item, inline = False)
        embed.set_footer(text = "작성자는 " + ctx.author.name + "님입니다. 구매 완료 후 이모지를 눌러주세요.")
        msg = await ctx.send(embed = embed)
        await msg.add_reaction("\U0001F9F1")

    else:

        embed = discord.Embed(title = "구매 명령어 소개 \U0001F9F1", description = "구매 명령어를 확인할 수 있습니다.", color = 0x9CFF00)
        embed.add_field(name = "#구매 [게임 이름] [희망 아이템]", value = "해당 게임에서 구매를 희망하는 아이템을 작성합니다.", inline = False)
        embed.add_field(name = "거래 완료 시", value = "구매 완료 후 아래 이모지를 눌러야 합니다.", inline = False)
        embed.set_footer(text = ctx.author.name + "님의 궁금증이 풀리셨나요?")
        await ctx.send(embed = embed)

@shop.command()
async def 판매(ctx, ctx1 = None, *, text = None):

    if ctx1 != None and text != None:

        await ctx.channel.purge(limit = 1)

        game = str(ctx1)
        item = str(text)

        embed = discord.Embed(title = "아이템 판매 글 \U0001F9F1", description = ctx.author.name + "님이 아이템의 구매자를 찾는 글입니다.", color = 0x9CFFFD)
        embed.add_field(name = "거래 대상 게임", value = game, inline = False)
        embed.add_field(name = "판매 희망 아이템", value = item, inline = False)
        embed.set_footer(text = "작성자는 " + ctx.author.name + "님입니다. 판매 완료 후 이모지를 눌러주세요.")
        msg = await ctx.send(embed = embed)
        await msg.add_reaction("\U0001F9F1")

    else:

        embed = discord.Embed(title = "판매 명령어 소개 \U0001F9F1", description = "판매 명령어를 확인할 수 있습니다.", color = 0x9CFFFD)
        embed.add_field(name = "#구매 [게임 이름] [희망 아이템]", value = "해당 게임에서 판매를 희망하는 아이템을 작성합니다.", inline = False)
        embed.add_field(name = "거래 완료 시", value = "판매 완료 후 아래 이모지를 눌러야 합니다.", inline = False)
        embed.set_footer(text = ctx.author.name + "님의 궁금증이 풀리셨나요?")
        await ctx.send(embed = embed)

access_token = os.environ["BOT_TOKEN"]
shop.run(access_token)
