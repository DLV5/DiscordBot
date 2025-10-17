import os
from dotenv import load_dotenv
import random
import nextcord
from nextcord.ext import commands
import casinoAccount
import casinoAccountsManager

load_dotenv()
TESTING_GUILD_ID = int(os.getenv("TESTING_GUILD_ID"))

class Casino(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.slotsVariants = [':horse:', ':roll_of_paper:', ':frog:', ':watermelon:', ':jack_o_lantern:']
        self.accountManager = casinoAccountsManager.casinoAccountsManager()

    def roll(self):
        return random.choices(self.slotsVariants, k=3)
    
    async def safe_send(self, interaction: nextcord.Interaction, *args, **kwargs):
        if not interaction.response.is_done():
            await interaction.response.send_message(*args, **kwargs)
        else:
            await interaction.followup.send(*args, **kwargs)

    def get_account_by_username(self, username):
        for i, acc in enumerate(self.accountManager.accounts):
            if acc.name == username:
                return i
        return None

    @nextcord.slash_command(
        name="stats",
        description="Get the stats for the player",
        guild_ids=[TESTING_GUILD_ID]
    )
    async def stats(self, interaction: nextcord.Interaction):
        """Show some stats"""
        userData = self.get_account_by_username(interaction.user.global_name)

        if userData is None:
            newAccount = casinoAccount.casinoAccount(interaction.user.global_name)
            self.accountManager.add_account(newAccount)
            userData = self.get_account_by_username(interaction.user.global_name)
        account = self.accountManager.accounts[userData]
        embed=account.get_as_discord_message()
        await self.safe_send(interaction, embed=embed)

        

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