import discord
from discord.ext import commands
import requests

url1 = "https://api.thecatapi.com/v1/images/search"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == "psps":
        response = requests.get(url1)
        data = response.json()
        cat_pic = data[0]['url']
        embed = discord.Embed(
            color=discord.Color.purple(),
            title="A cat for you, lowly human",
            description="peasants"
        )
        embed.set_image(url=cat_pic)
        await message.channel.send(embed=embed)
    await bot.process_commands(message)

@bot.tree.command(name="cat", description="Get a random cat picture")
async def cat(interaction: discord.Interaction):
    response = requests.get(url1)
    data = response.json()
    cat_pic = data[0]['url']
    embed = discord.Embed(
        color=discord.Color.purple(),
        title="A cat for you, lowly human",
        description="peasants"
    )
    embed.set_image(url=cat_pic)
    await interaction.response.send_message(embed=embed)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

bot.run("")
