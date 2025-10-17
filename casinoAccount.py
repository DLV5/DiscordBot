import json
import nextcord

class casinoAccount:
    def __init__(
            self, name = "Qwerty", balance = 1000, level = 1, 
            rank = 1):
        self.name = name
        self.balance = balance
        self.level = level
        self.rank = rank

    def load_string(self, str):
        data = json.loads(str)
        self.name = data[0]
        self.balance = data[1]
        self.level = data[2]
        self.rank = data[3]

    def get_as_string(self):
        return json.dumps([self.name, self.balance, self.level, self.rank])

    def get_as_discord_message(self):
        embed = nextcord.Embed(
            title=f"{self.name}'s Casino Stats",
            color=nextcord.Color.gold()
        )
        embed.add_field(name="Username", value=self.name, inline=False)
        embed.add_field(name="Current balance", value=str(self.balance), inline=False)
        embed.add_field(name="Current level", value=str(self.level), inline=False)
        embed.add_field(name="Current rank", value="beginner gambler", inline=False)
        return embed
        # return (
        #     f"```Username: {self.name}\n"
        #     f"Current balance: {self.balance}\n"
        #     f"Current level: {self.level}\n"
        #     f"Current rank: beginner gambler```"
        # )