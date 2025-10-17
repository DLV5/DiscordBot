import os

class UsedMemesManager:

    def __init__(self):    
        self.filename = "usedMemes.txt"
        self.usedLinks = self.init_used_links()

    def init_used_links(self):
        usedLinks = []

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                pass

        with open(self.filename, "r") as file:
            for line in file:
                usedLinks.append(line.strip())
        return usedLinks
    
    def add_used_link(self, link):
        with open(self.filename, "a") as file:
            file.write(str(link) + '\n')
            self.usedLinks.append(link)

    def is_used(self, link):
        return link in self.usedLinks