import discord
from discord.ext import commands
import aiohttp

url1 = "https://api.thecatapi.com/v1/images/search"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def get_cat_pic():
    async with aiohttp.ClientSession() as session:
        async with session.get(url1) as resp:
            data = await resp.json()
            return data[0]['url']

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == "psps":
        cat_pic = await get_cat_pic()
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
    cat_pic = await get_cat_pic()
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
