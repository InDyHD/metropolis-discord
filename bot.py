import discord
from discord.ext import commands

TOKEN = "NTE0MTQzNTgwMzAyODY4NTQ1.DuSY9Q.ig3tVqfPEUfVkWLuwY6s50UyH5M"

client = commands.Bot(command_prefix = "_")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="For The Win Servers"))
    print('Logado em:')
    print(client.user.name)
    print(client.user.id)
    print('----------')
    print("Bot Ready!")

client.run(TOKEN)
