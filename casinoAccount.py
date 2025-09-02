import json

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
