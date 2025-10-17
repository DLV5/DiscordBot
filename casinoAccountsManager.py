import os
import casinoAccount

class casinoAccountsManager:
    def init_saved_accounts(self):
        accounts = []

        if not os.path.exists(self.accountsFileName):
            with open(self.accountsFileName, "w") as file:
                pass

        with open(self.accountsFileName, "r") as file:
            for line in file:
                acc = casinoAccount.casinoAccount()
                acc.load_string(line.strip())
                accounts.append(acc)
        return accounts
    
    def __init__(self):
        self.accountsFileName = 'accounts.txt'
        self.accounts = self.init_saved_accounts()
    
    def add_account(self, account):
        with open(self.accountsFileName, "a") as file:
            file.write(account.get_as_string() + '\n')
            self.accounts.append(account)
    
    def print_account(self):
        print(self.accounts)

# accountManager = casinoAccountManager()
# accountManager.print_account()
# testAccount = casinoAccount.casinoAccount('Test5', 10000, 2, 3)
# accountManager.add_account(testAccount)