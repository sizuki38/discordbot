from sqlalchemy.sql.expression import text
from create_db import *
from sub import *
import discord, datetime, asyncio
from text import help

TOKEN = 'ODMwMzc1NDI4NDIxNzEzOTIw.YHFxYQ.v5vVGD2vxWczuSPp1Ubg33uoeB4'
client = discord.Client()

@client.event
async def greet(dt_now):
        for i in CHANNEL_ID:
            channel = client.get_channel(i)
            await channel.send(dt_now.minute)

@client.event
async def on_ready():#起動時
    print('ncodeBot get started.')
    while True:
        dt_now = datetime.datetime.now()
        if dt_now.minute%5 == 0:
            novels = ReadNovels()
            for novel in novels:
                novelInfo = scrapy(novel.ncode)
                name = novelInfo[0]
                if nos_now > novel.nos:
                    UpdateNovel(novel, nos_now)
                    middles = ReadMiddleNovel(novel.id)
                    for middle in middles:
                        Readch = ReadChannelID(middle.channel_id)
                        channel = client.get_channel(Readch.channel_id)
                        channel.send('小説が更新されました.\n'+base+novel.ncode+novel.nos)
        await asyncio.sleep(60)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if client.user in message.mentions or message.content.startswith('/Nmkch'):
        await create_channel(message)
    if message.content.startswith('/Nstart'):
        try:
            ncode = message.content.split('/Nstart ')[1].split('/')[3]
        except:
            await message.channel.send(help)
        else:
            print('add:'+ncode)
            nos = scrapy(ncode)
            CreateNovel(ncode, name, nos)
            await message.channel.send()
    if message.content.startswith('/Nread'):
        channels = ReadChannels()
        print(channels)
        for channel in channels:
            chmes = client.get_channel(channel.channel_id)
            chmes.send('AAA')
    if message.content.startswith('/Nhelp'):
        await message.channel.send(help)

client.run(TOKEN)