import asyncio, discord, os
from discord.ext import commands

file_path = os.path.dirname(os.path.abspath(__file__))
token_path = file_path+"/token.txt"
t = open(token_path, "r", encoding="utf-8")
token = t.read().split()[0]
print("!Token_key : ", token)
game = discord.Game("대기")
bot = commands.Bot(command_prefix='호성아 ', status=discord.Status.online, activity=game)

@bot.event
async def on_ready():
    print("봇 시작")

@bot.event
async def on_member_join(member):
    await member.send("안녕하세요 당신의 영원한 노예 호성PC입니다.")
    embed = discord.Embed(title=f"호성PC에 오신 것을 환영합니다.", description=f"당신을 위한 최고의 공간 호성PC", color=0xf3bb76)
    embed.add_field(name=f"2021년 1월 1일부로 호성 PC는 전액 무료로 전환합니다.", value="많은 이용 부탁드립니다", inline=False)
    await member.send(embed=embed)

@bot.event
async def on_message(message):
    message_content = message.content
    if message_content.find("씨발")>=0:
        await message.channel.send("씨발은 좀 너무하잖아")
    await bot.process_commands(message)

@bot.command()
async def 도움(ctx):
    await ctx.send("무엇을 도와드릴까요?")

@bot.command()
async def 인사해야지(ctx):
    embed=discord.Embed(title=f"호성PC에 오신 것을 환영합니다.", description=f"당신을 위한 최고의 공간 호성PC", color=0xf3bb76)
    embed.add_field(name=f"2021년 1월 1일부로 호성 PC는 전액 무료로 전환합니다.", value="많은 이용 부탁드립니다", inline=False)
    embed.set_thumbnail(url=file_path+'\호성피시.jpg')
    await ctx.send(embed=embed)
bot.run(token)



