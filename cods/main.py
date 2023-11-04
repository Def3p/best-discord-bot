import disnake
from disnake.ext import commands

token = "xxxxx"

bot = commands.Bot(command_prefix="/", help_command=None, intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is ready to work!")

@bot.event
async def on_message(message):
    if message.content.lower() == "bot":
        await message.channel.send("test")

bot.run(token)