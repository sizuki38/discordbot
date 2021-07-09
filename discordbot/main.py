import discord
from discord import channel

from create_db import * 

TOKEN = 'ODMwMzc1NDI4NDIxNzEzOTIw.YHFxYQ.dWUwNqA9ReJJJ0-pt1dt9pc4hWY'
CHANNEL_ID = 862209054830886943
GUILD_ID = 834289296725901332
client = discord.Client()
channel_name = 'なろう更新'

# 発言したチャンネルのカテゴリ内にチャンネルを作成する非同期関数
async def create_channel(message):
    category_id = message.channel.category_id
    category = message.guild.get_channel(category_id)
    if channel_name in str(message.guild.text_channels):
        return
    else:
        new_channel = await category.create_text_channel(name=channel_name)
        return new_channel

# @client.event
# async def greet():
#         for i in CHANNEL_ID:
#             channel = client.get_channel(i)
#             await channel.send('good mornig.')

@client.event
async def on_ready():#起動時
    print('ncodebot get started.')
    # await greet()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if client.user in message.mentions:
        try:
            new_channel = await create_channel(message)
            # チャンネルのリンクと作成メッセージを送信
            text = f'{new_channel.mention} を作成しました.'
            await message.channel.send(text)
        except:
            guild = client.get_guild(GUILD_ID)
            print(type(guild))
            new_channel = guild.get_channel(CHANNEL_ID)
            print(type(new_channel))
        finally:
            await new_channel.send('aaa\nbbb')


client.run(TOKEN)