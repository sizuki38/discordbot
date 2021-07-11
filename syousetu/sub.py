from bs4 import BeautifulSoup
import urllib.request

base = 'https://ncode.syosetu.com/'

async def scrapy(ncode):
    if base in ncode:
        url = ncode
    else:
        url = base + ncode
    print(url)
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html,"html.parser")
    topicsindex = soup.find_all('dl', attrs={'class': 'novel_sublist2'})
    return len(topicsindex)

    # 発言したチャンネルのカテゴリ内にチャンネルを作成する非同期関数
async def create_channel(message):
    category_id = message.channel.category_id
    category = message.guild.get_channel(category_id)
    if channel_name in str(message.guild.text_channels):
        return
    else:
        new_channel = await category.create_text_channel(name=channel_name)
        return new_channel