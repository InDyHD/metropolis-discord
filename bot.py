import discord
from discord.ext import commands

TOKEN = "NTQ0NjI5ODMyMTU2NDQ2NzMw.D0N6JQ.QnBvXO-ibnSnyZkW7fVtSlfxaPk"

client = commands.Bot(command_prefix = "_")

@client.event

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="For The Win Servers"))
    print('Logado em:')
    print(client.user.name)
    print(client.user.id)
    print('----------')
    print("Bot Ready!")

client.run(TOKEN)
