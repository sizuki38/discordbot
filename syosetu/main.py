from create_db import *
from sub import *
import discord, datetime, asyncio

TOKEN = ''
CHANNEL_ID = [863471180945817640,863471268070162458,863148987522482188]
client = discord.Client()

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
            novels = ReadNovel()
            for novel in novels:
                nos_now = scrapy(novel.ncode)
                if nos_now > novel.nos:
                    UpdateNovel(novel, nos_now)
                    middles = ReadMiddleNovel(novel.id)
                    for middle in middles:
                        channel_id = ReadChannelID(middle.channel_id)
                        channel = client.get_channel(channel_id)
                        channel.send('小説が更新されました.\n'+base+novel.ncode+novel.nos)
        await asyncio.sleep(60)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if client.user in message.mentions:
        await create_channel(message)
    if message.content.startswith('/add'):
        try:
            url = message.split()[1].split('/')[-1]
        except:
            await help()
        else:
            await scrapy(url)

    if message.content.startswith('/neko'):
        await message.channel.send('にゃーん')

client.run(TOKEN)