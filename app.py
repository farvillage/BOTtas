from nextcord.ext import commands
import requests, json, random
import nextcord
intents = nextcord.Intents.default()

intents.message_content = True

links = json.load(open("pics.json"))

bot = commands.Bot(command_prefix="bottas ",intents=intents)

@bot.command(name="pic")
async def Bottas(ctx):
    linkDrawn = links["pic"][random.randint(0,9)]
    #response = requests.get("https://static.independent.co.uk/2022/06/23/13/GettyImages-1328909112.jpg") **ERRADO**
    await ctx.send(linkDrawn)

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")

token = ""
with open("token.txt") as file:
    token = file.read()
bot.run(token)