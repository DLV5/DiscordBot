import os
from dotenv import load_dotenv
import requests
import time
import json
import nextcord
from nextcord.ext import commands
import usedMemesManager
import confirmMeme
load_dotenv()
TESTING_GUILD_ID = int(os.getenv("TESTING_GUILD_ID"))

class memeShower(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.memesFileManager = usedMemesManager.UsedMemesManager()
    
    def get_pack_of_memes(self):
        response = requests.get('https://meme-api.com/gimme/UmaMusume/25')
        return json.loads(response.text)['memes']

    def get_unique_meme(self, max_retries=50):
        retries = 0
        while retries < max_retries:
            memes = self.get_pack_of_memes()
            for meme in memes:
                if not self.memesFileManager.is_used(meme['url']):
                    self.memesFileManager.add_used_link(meme['url'])
                    return meme['url']
            retries += 1
            time.sleep(1)
        return "Not this time"

    @nextcord.slash_command(
        name="carat",
        description="Get a meme from umamusume reddit",
        guild_ids=[TESTING_GUILD_ID]
    )
    async def showMeme(self, interaction: nextcord.Interaction):
        """Get a meme from the umamusume discord"""
        view = confirmMeme.ConfirmMeme()
        if not interaction.response.is_done():
            await interaction.response.send_message(self.get_unique_meme())
        else:
            await interaction.followup.send(self.get_unique_meme())
        
        await interaction.followup.send(f'Do you want another meme?', view=view)
        await view.wait()
        if view.value:
            await self.showMeme(interaction)
        else:
            await interaction.followup.send(f'I collected a total of {len(self.memesFileManager.usedLinks)} carats so far🥕')

def setup(bot):
    bot.add_cog(memeShower(bot))