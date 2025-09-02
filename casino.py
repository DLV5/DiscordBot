import os
from dotenv import load_dotenv
import random
import nextcord
from nextcord.ext import commands

load_dotenv()
TESTING_GUILD_ID = int(os.getenv("TESTING_GUILD_ID"))

class Casino(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slotsVariants = [':horse:', ':roll_of_paper:', ':frog:', ':watermelon:', ':jack_o_lantern:']

    def roll(self):
        return random.choices(self.slotsVariants, k=3)
    
    async def safe_send(self, interaction: nextcord.Interaction, *args, **kwargs):
        if not interaction.response.is_done():
            await interaction.response.send_message(*args, **kwargs)
        else:
            await interaction.followup.send(*args, **kwargs)

    @nextcord.slash_command(
        name="slots",
        description="Spin the slot machine",
        guild_ids=[TESTING_GUILD_ID]
    )
    async def slots(self, interaction: nextcord.Interaction, amount: int):
        """gamble x amount"""

        if amount >= 100:
            await self.safe_send(interaction, 'Nope, you are too broke for this :(')
            return
        for i in range(0, amount):
            result = self.roll()
            await self.safe_send(interaction, str(result[0]) + ' | ' + str(result[1]) + ' | ' + str(result[2]) )
        if result[0] == ':horse:' and result[1] == ':horse:' and result[2] == ':horse:':
            await self.safe_send(interaction, 'Jackpot! :horse: :horse: :horse:')
        else:
            await self.safe_send(interaction, 'Not this time :(\nThanks for playing!')  

def setup(bot):
    bot.add_cog(Casino(bot))           