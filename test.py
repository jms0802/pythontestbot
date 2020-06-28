import discord
import random

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("#명령어")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    global ctx
    ctx = message.channel

    if message.content.startswith("#안녕"):
        hello = ["☆세모 왔쪄염☆", "☆민수 왔쪄염☆", "☆수미니 왔쪄염☆", "☆소혀니 왔쪄염☆", "☆지워니 왔쪄염☆","☆미누기 왔쪄염☆"]
        t1 = random.randint(0, len(hello)-1)
        await message.channel.send(hello[t1])

    if message.content.startswith("#잘자"):
        await message.channel.send("세모 자러가욧")
        await message.channel.send(file=discord.File("잠자는 세모.jpg"))

    if message.content.startswith("#잘가") or message.content.startswith("#꺼져"):
        bye = ["세모 좀 더 놀고시푼뎅,,,,,", "아가리", "정수민 야발아 난 간다", "세모 버리지마,,, ( ˃̣̣̥᷄⌓˂̣̣̥᷅ ) ", "세모는 가기시러욧!☆!"]
        t2 = random.randint(0, len(bye)-1)
        await message.channel.send(bye[t2])

    if message.content.startswith("#뭐해"):
        what = ["세모는 메이플 중이야 \n(づ｡◕‿‿◕｡)づ", "세모 너모 심심한데,,, \n세모랑 놀아줘 (◕`ε´◕) ", "세모 모하게~?~? ( ͡° ͜ʖ ͡° ) ",
                "세모세모 빔  \n◝(・ω・)◟  ", "세모 짝사랑중이얌 \n༼๑⁰⊖⁰๑༽❤ ", "세모 배고파 \n ༼ ༎ຶ ෴ ༎ຶ༽  "]
        t3 = random.randint(0, len(what) - 1)
        await message.channel.send(what[t3])

    global num1, ran  # 뽑기 명령어
    if message.content.startswith("#뽑기"):
        ran = []
        num1 = int(message.content.split(" ")[1])
        await message.channel.send("세모를 ☆PICK☆ 해줬음 좋겠어❤")

    if message.content.startswith("#목록"):
        for i in range(1, num1 + 1):
            text1 = str(message.content.split(" ")[i])
            ran.append(text1)
        num3 = random.randint(0, num1 - 1)
        await message.channel.send(ran[num3]+" 당첨!")
        await message.channel.send("왜 세모를 뽑아주지않은거야..?\n ༼;´༎ຶ ۝༎ຶ`༽ ")
        num1 = 0

    if message.content.startswith("#명령어"):
        embed = discord.Embed(title="명령어", color=0xf3bb76)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/726834573891207291/726880501981380618/0a31ee767f32178f.jpg")
        embed.add_field(name="#안녕", value="인사")
        embed.add_field(name="#잘가 or #꺼져", value="인사")
        embed.add_field(name="#뭐해", value="그냥")
        embed.add_field(name="#뽑기 (숫자)", value="(숫자)개 목록에서 뽑기", inline=False)
        embed.add_field(name="#목록 (...)  (...)", value="#뽑기 의 (숫자)만큼 작성 (예: #뽑기 3 , #목록 1 2 3)")
        await ctx.send(embed=embed)

client.run("NzI2ODI5MDY5MjQ0Njk0NTc4.XvjjWQ._ux6mD5JjGENsBE_45e5LJyIl00")
