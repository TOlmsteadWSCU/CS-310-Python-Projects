#Travis Olmstead
#310
# Bank class
import Account

class Bank:
    '''
    Bank class holds a group of Accounts in a dictionary with owner as the
    key.  The Bank class processes intra bank transactions.
    '''

    number_of_banks = 0  # class variable

    def __init__(self,routing_number): # a bank is initially empty
        Bank.number_of_banks += 1
        self.number_of_accounts = 0
        self.routing_number = routing_number
        self.accounts = {}

    def __str__(self):
        total_deposits = 0
        for owner, account in self.accounts.items():
            total_deposits += account.query()
        # return ("A bank with " + str(self.number_of_accounts) +
        #     " accounts." +"Total deposits:" +
        #     str(total_deposits))

        return "A bank with {} accounts and total deposits ${}".format(self.number_of_accounts,total_deposits)

    def debit_acc(self, account_num, amount):
        if account_num in self.accounts:
            self.accounts[account_num].debit(amount)
            return True
        else:
            return False

    def credit_acc(self, account_num, amount):
        if account_num in self.accounts:
            self.accounts[account_num].credit(amount)
            return True
        else:
            return False


    def query_acc(self, account_num):
        if account_num in self.accounts:
            return self.accounts[account_num].query()
            return True
        else:
            return False

    def query_name(self,name):
        for i in self.accounts:
            if self.accounts[i].owner == name:
                return self.accounts[i].balance
        print(name + " does not have an account!")

    def credit_name(self, name, amt):
        for i in self.accounts:
            if self.accounts[i].owner == name:
                self.accounts[i].credit(amt)
                return True
        print(name + " does not have an account!")
        return False

    def debit_name(self, name, amt):
        for i in self.accounts:
            if self.accounts[i].owner == name:
                self.accounts[i].debit(amt)
                return True
        print(name + " does not have an account!")
        return False


    def add_account(self,acc):
        if isinstance(acc,Account.Account):
            self.accounts[acc.account_num]=acc
            self.number_of_accounts+=1
        else:
            print("Added account " + str(acc) + " is not really an account.")

    def process_transaction(self, origin_routing_num,origin_acct,
            dest_routing_num, dest_acct, amt):
        if origin_routing_num != self.routing_number | dest_routing_num != self.routing_number:
            return False # not an internal transaction

        self.accounts[origin_acct].debit(amt)
        self.accounts[dest_acct].credit(amt)
        return True



if __name__ == "__main__":
    # make a new bank
    b=Bank(42)
    print(b)

    # try to add a bad account
    b.add_account(5)
    print(b)

    # add a good account
    b.add_account(Account.Account(1,"bobo",50.05))
    print(b)

    # look up account number 1
    print(b.accounts[1])

    b = Bank(42)
    print(b)

    # try to add a bad account
    b.add_account(5)
    print(b)

    # add a good account
    b.add_account(Account.Account(24, "bobo", 50.05))
    b.add_account((Account.Account(10, "Travis Olmstead", 100)))

    print(b)

    # look up account number 1
    print(b.accounts[10])

    # querry by account number
    print(b.query_acc(10), "querry_acc")

    # credit by account number
    # print("Credit by account number")
    b.credit_acc(10, 10)
    print(b.query_acc(10), "credit_acc 10")

    # #debit by account number
    b.debit_acc(10, 40)
    print(b.query_acc(10), "debit_acc 40")

    # #querry by account name
    print(b.query_name("Travis Olmstead"), "querry_name")

    # credit by account name
    b.credit_name("Travis Olmstead", 10000)
    print(b.query_name("Travis Olmstead"), "credit_name 100")

    # debit by account name
    b.debit_name("Travis Olmstead", 700)
    print(b.query_name("Travis Olmstead"), "debit_name 500")