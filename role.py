# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
#TOKEN = 'NjMwODQ2MzE2Njk1NjUwMzE0.XZuP3g.xOSs79Vj9j1LlLRSDXioCWhx60A'
TOKEN = 'NjY0MTkxNDE3OTQ1NTU0OTgw.XhTh2w.KEhGd58APz6UEa1R-I4xDxNQm3c'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    # 起動時に任意のチャンネルで挨拶する
    CHANNEL_ID = 708720072000143360# 任意のチャンネルID(int)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('やっほ')

@client.event 
async def on_message(message):
    if message.content.startswith("/ar sentou"):
        role = discord.utils.get(message.guild.roles,id=708689289877127241)
        reply = f'{message.author.mention} 役職【銭湯民族】を追加しました'
        await message.channel.send(reply)
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)