import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트봇")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("안녕")
        await message.channel.send("반가워요")
    if message.content.startswith("잘가")
        await message.channel.send("잘가세요")


client.run("NzUzOTg5MTg4MTYzOTkzNjEw.X1uNJg.cKdw1N_qzVQ7XAtqEeCqUpD8T7Q")


