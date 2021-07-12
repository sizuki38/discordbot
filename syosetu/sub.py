from sqlalchemy.orm import session
from bs4 import BeautifulSoup
import urllib.request
from create_db import CreateNovel, engine

base = 'https://ncode.syosetu.com/'
channel_name = 'なろう更新'

def scrapy(ncode):
    if base in ncode:
        url = ncode
    else:
        url = base + ncode
    print(url)
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html,"html.parser")
    topicsindex = soup.find_all('dl', attrs={'class': 'novel_sublist2'})
    text = CreateNovel(ncode, len(topicsindex))
    return text

    # 発言したチャンネルのカテゴリ内にチャンネルを作成する非同期関数
async def create_channel(message):
    category_id = message.channel.category_id
    category = message.guild.get_channel(category_id)
    if channel_name in str(message.guild.text_channels):
        return
    new_channel = await category.create_text_channel(name=channel_name)
    # チャンネルのリンクと作成メッセージを送信
    text = f'{new_channel.mention} を作成しました.'
    await message.channel.send(text)
    await new_channel.send('aaa\nbbb')


