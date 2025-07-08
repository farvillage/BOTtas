from nextcord.ext import commands
import json, random
import nextcord
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise ValueError("DISCORD_TOKEN ins't defined in .env")

    intents = nextcord.Intents.default()
    intents.message_content = True

    with open("pics.json") as f:
        links = json.load(f)

    bot = commands.Bot(command_prefix="bottas ", intents=intents)

    @bot.command(name="pic")
    async def Bottas(ctx):
        linkDrawn = random.choice(links["pic"])
        await ctx.send(file=nextcord.File(linkDrawn))

    @bot.event
    async def on_ready():
        print(f"{bot.user.name} is online!")

    bot.run(token)

if __name__ == "__main__":
    main()
