import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import music
load_dotenv()

TESTING_GUILD_ID = int(os.getenv("TESTING_GUILD_ID"))

description = """Umamusume bot, with some fun functionality"""

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.load_extension("casino")
bot.load_extension("memeShower")
bot.add_cog(music.Music(bot))
bot.run(os.environ["BOT_TOKEN"])