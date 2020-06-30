import discord
import random
import os
import openpyxl

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game(".명령어")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    global ctx
    ctx = message.channel

    if message.content.startswith(".안녕"):
        hello = ["☆세모 왔쪄염☆", "☆민수 왔쪄염☆", "☆수미니 왔쪄염☆", "☆소혀니 왔쪄염☆", "☆지워니 왔쪄염☆","☆미누기 왔쪄염☆"]
        t1 = random.randint(0, len(hello)-1)
        await message.channel.send(hello[t1])

    if message.content.startswith(".잘자"):
        await message.channel.send("세모 자러가욧")
        await message.channel.send(file=discord.File("잠자는 세모.jpg"))

    if message.content.startswith(".잘가") or message.content.startswith("#꺼져"):
        bye = ["세모 좀 더 놀고시푼뎅,,,,,", "아가리", "정수민 야발아 난 간다", "세모 버리지마,,, ( ˃̣̣̥᷄⌓˂̣̣̥᷅ ) ", "세모는 가기시러욧!☆!"]
        t2 = random.randint(0, len(bye)-1)
        await message.channel.send(bye[t2])

    if message.content.startswith(".뭐해"):
        what = ["세모는 메이플 중이야 \n(づ｡◕‿‿◕｡)づ", "세모 너모 심심한데,,, \n세모랑 놀아줘 (◕`ε´◕) ", "세모 모하게~?~? ( ͡° ͜ʖ ͡° ) ",
                "세모세모 빔  \n◝(・ω・)◟  ", "세모 짝사랑중이얌 \n༼๑⁰⊖⁰๑༽❤ ", "세모 배고파 \n ༼ ༎ຶ ෴ ༎ຶ༽  "]
        t3 = random.randint(0, len(what) - 1)
        await message.channel.send(what[t3])
        
    if message.content.startswith(".명령어"):
        embed = discord.Embed(title="명령어", color=0xF08080)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/726834573891207291/726880501981380618/0a31ee767f32178f.jpg")
        embed.add_field(name=".안녕", value="인사")
        embed.add_field(name=".잘가 or #꺼져", value="인사")
        embed.add_field(name=".뭐해", value="그냥")
        embed.add_field(name=".뽑기 (숫자)", value="(숫자)개 목록에서 뽑기", inline=False)
        embed.add_field(name=".목록 (...)  (...)", value=".뽑기 의 (숫자)만큼 작성 (예: .뽑기 3 , .목록 1 2 3)")
        embed.add_field(name=".낚시명령어", value="낚시 도움말", inline=False)
        await ctx.send(embed=embed)
        
    if message.content.startswith(".낚시명령어"):
        embed = discord.Embed(title="낚시명령어", color=0x87CEFA)
        embed.set_thumbnail(url="https://mblogthumb-phinf.pstatic.net/MjAyMDAzMjVfMjAx/MDAxNTg1MTE1NDA2OTU0.3lxaLaNZVdSuJOievVy"
                                "rY647RhMCHTvPLr2LjrhL6cog.9XZkTtiIz_SM0hzpNrKlKQ_6AZYRzyEsdVzCpOgFN5Qg.JPEG.12512512/%EB%B6%80"
                                "%EB%91%A3%EA%B0%80.jpg?type=w800")
        embed.add_field(name=".낚시등록", value="낚시 회원권을 등록한다.", inline=False)
        embed.add_field(name=".낚시확인", value="자신의 낚시 정보를 확인한다.", inline=False)
        embed.add_field(name=".낚시하기", value="낚시를 시작한다. (미끼 -1)", inline=False)
        embed.add_field(name=".생선팔기", value="자신이 가진 생선을 모두 판다. (다소 시간이 걸린다.)", inline=False)
        embed.add_field(name=".미끼사기  (숫자)", value="미끼를 (숫자)만큼 살 수 있다. (미끼 1개 당 100원)", inline=False)
        embed.add_field(name=".시세확인", value="생선의 시세를 확인한다.", inline=False)
        await ctx.send(embed=embed)

    #뽑기--------------------------------------------------------------------------------------------------------------
    global num1, ran  # 뽑기 명령어
    if message.content.startswith(".뽑기"):
        ran = []
        num1 = int(message.content.split(" ")[1])
        await message.channel.send("세모를 ☆PICK☆ 해줬음 좋겠어❤")

    if message.content.startswith(".목록"):
        for i in range(1, num1 + 1):
            text1 = str(message.content.split(" ")[i])
            ran.append(text1)
        num3 = random.randint(0, num1 - 1)
        await message.channel.send(ran[num3]+" 당첨!")
        await message.channel.send("왜 세모를 뽑아주지않은거야..?\n ༼;´༎ຶ ۝༎ຶ`༽ ")
        num1 = 0
        
    #낚시--------------------------------------------------------------------------------------------------------------

    fishes = ["A", "B", "C", "D", "E", "F", "G"]

    file1 = openpyxl.load_workbook("물고기.xlsx")
    sheet1 = file1.active

    file2 = openpyxl.load_workbook("낚시.xlsx")
    sheet2 = file2.active

    if message.content.startswith(".낚시등록"):
        i = 1
        while 1:
            if sheet2["A" + str(i)].value == str(message.author.id):
                await ctx.send("이미 등록된 회원")
                break

            elif sheet2["A" + str(i)].value == None:
                sheet2["A" + str(i)].value = str(message.author.id) #ID
                sheet2["B" + str(i)].value = 0      #돈
                sheet2["C" + str(i)].value = 10     #미끼
                sheet2["E" + str(i)].value = ","    #물고기 목록
                await ctx.send(str(i) +"번째 회원 등록완료")
                file2.save("낚시.xlsx")
                break
            i += 1

    if message.content.startswith(".낚시확인"):
        i = 1
        while 1:
            if sheet2["A" + str(i)].value == str(message.author.id):
                await ctx.send("돈 : "+ str(sheet2["B" + str(i)].value)+
                               "\n미끼 : "+ str(sheet2["C" + str(i)].value)+
                               "\n생선 목록 : "+ str(sheet2["E" + str(i)].value))
                break
            elif sheet2["A" + str(i)].value == None:
                await ctx.send("회원권이 없습니다.")
                break
            else:
                i += 1

    if message.content.startswith(".생선팔기"):
        x = 0 #시트1 물고기 번호
        i = 1
        while 1:
            if (sheet2["A" + str(i)].value) == str(message.author.id):
                fish_list = sheet2["E" + str(i)].value.split(",")
                while 1:
                    fish_na = fish_list[1]
                    x1 = fishes[x]

                    if fish_na == sheet1[x1 + str(3)].value:
                        sheet2["B" + str(i)].value += sheet1[x1 + str(2)].value #생선 값 추가
                        await ctx.send(fish_na + " 판매완료")
                        fish_list.remove(fish_na)
                        file2.save("낚시.xlsx")
                        x = 0

                    elif fish_na == "":
                        sheet2["E" + str(i)].value = ","
                        file2.save("낚시.xlsx")
                        await ctx.send("모두 팔림")
                        break
                    else:
                        x += 1
                break

            elif sheet2["A" + str(i)].value == None:
                await ctx.send("회원권이 없습니다.")
                break
            else:
                i += 1

    if message.content.startswith(".미끼사기"):
        bait_n = int(message.content.split(" ")[1])
        bait = 100
        i = 1
        while 1:
            if sheet2["A" + str(i)].value == str(message.author.id):
                if sheet2["B" + str(i)].value < 100:
                    await ctx.send("미끼를 살 수 없습니다.")
                    break

                sheet2["B" + str(i)].value -= 100 * bait_n
                sheet2["C" + str(i)].value += bait_n
                await ctx.send(str(bait_n) + "개의 미끼를 구매하였습니다.")
                file2.save("낚시.xlsx")
                break

            elif sheet2["A" + str(i)].value == None:
                await ctx.send("회원권이 없습니다.")
                break
            else:
                i += 1

    if message.content.startswith(".낚시하기"):
        r1 = random.randint(0, 2)  # 성공여부
        i = 1
        while 1:
            if sheet2["A" + str(i)].value == str(message.author.id): #아이디 체크
                if sheet2["C" + str(i)].value == 0: #미끼 없음
                    await ctx.send("미끼가 없습니다.")
                    break

                if r1 == 0: #낚시 실패
                    sheet2["C" + str(i)].value -= 1
                    await ctx.send("실패!")
                    await ctx.send(str(sheet2["C" + str(i)].value) + "개 미끼 남음")
                    file2.save("낚시.xlsx")
                    break

                if r1 != 0: #낚시 성공
                    r2 = random.randint(0, len(fishes)-1)
                    fish_num = fishes[r2]
                    fish_name = sheet1[fish_num + str(1)].value
                    sheet2["C" + str(i)].value -= 1
                    sheet2["E" + str(i)].value += str(fish_name)
                    #await ctx.send(str(fish_name) + "를(을) 낚았습니다!")
                    #await ctx.send(str(sheet2["C" + str(i)].value) + "개 미끼 남음")
                    file2.save("낚시.xlsx")

                    embed1 = discord.Embed(title="낚시 성공!", color=0x9ED6C0)
                    if fish_num == "A":
                        embed1.set_thumbnail(url="https://pbs.twimg.com/media/EYyznV1U0AA242D.jpg:small")
                    elif fish_num == "B":
                        embed1.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTXDx8Vd00"
                                                 "_ofDv8guDFqoDpsS8IgERbWIbMA&usqp=CAU")
                    elif fish_num == "C":
                        embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/722800057170001920/"
                                                 "727650374395363348/df5adce927b9288b.jpg")
                    elif fish_num == "D":
                        embed1.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSc5JcHU8wv"
                                                 "PVkom6BA0kzbG5P3y6cqbhieeA&usqp=CAU")
                    elif fish_num == "E":
                        embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/722800057170001920/"
                                                 "727650392355373106/4e1dc2cb96208a9d.jpg")
                    elif fish_num == "F":
                        embed1.set_thumbnail(url="https://pbs.twimg.com/media/EXEJhTfUMAI6NvV.jpg")
                    elif fish_num == "G":
                        embed1.set_thumbnail(url="https://t1.daumcdn.net/cfile/tistory/9914EA505E7549F411")
                    embed1.add_field(name=sheet1[fish_num + str(3)].value + "를(을) 낚았다!", value="야호!", inline=False)
                    embed1.add_field(name="미끼", value=str(sheet2["C" + str(i)].value) + "개 남음")
                    await ctx.send(embed=embed1)
                    break

            elif sheet2["A" + str(i)].value == None:
                await ctx.send("회원권이 없습니다.")
                break

            i += 1

    if message.content.startswith(".시세확인"):
        embed = discord.Embed(title="생선 시세", color=0xFFD700)
        embed.set_thumbnail(
            url="https://i.ytimg.com/vi/URMnWe0ElYQ/maxresdefault.jpg")
        embed.add_field(name="붕어", value="200")
        embed.add_field(name="복어", value="400")
        embed.add_field(name="갈치", value="600")
        embed.add_field(name="참치", value="800")
        embed.add_field(name="세현", value="1000")
        embed.add_field(name="돌", value="50")
        embed.add_field(name="장화", value="50")
        await ctx.send(embed=embed)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
