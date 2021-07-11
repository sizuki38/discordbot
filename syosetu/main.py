from sub import *
import discord, datetime, asyncio

TOKEN = ''
CHANNEL_ID = [863471180945817640,863471268070162458,863148987522482188]
client = discord.Client()
channel_name = 'なろう更新'

@client.event
async def greet(dt_now):
        for i in CHANNEL_ID:
            channel = client.get_channel(i)
            await channel.send(dt_now.minute)

@client.event
async def on_ready():#起動時
    print('ncodebot get started.')
    while True:
        dt_now = datetime.datetime.now()
        if dt_now.minute%5 == 0:
            await greet(dt_now)
        await asyncio.sleep(60)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if client.user in message.mentions:
#         try:
        new_channel = await create_channel(message)
            # チャンネルのリンクと作成メッセージを送信
        text = f'{new_channel.mention} を作成しました.'
        await message.channel.send(text)
        await new_channel.send('aaa\nbbb')

    if message.content.startswith('/add'):
        url = message.content.split()[1]
        await crapy(url)


    if message.content.startswith('/neko'):
        await message.channel.send('にゃーん')

client.run(TOKEN)