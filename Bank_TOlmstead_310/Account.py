# class for one account

class Account:
    '''
    An account consists of an owner and a balance
    '''

    def __init__(self,account_num, owner,init_balance=0):
        self.account_num = account_num
        self.owner = owner
        self.balance = init_balance

    def credit(self,amt):
        self.balance+=amt

    def debit(self,amt):
        self.balance-=amt

    def query(self):
        return(self.balance)

    def __str__(self):
        return("owner:"+str(self.owner)+
        "\nbalance:"+str(self.balance)+"\n")


# tests



if __name__ == "__main__":
    a1 = Account(1,"bobo",60)
    a2 = Account(2,"coco",500)

    print(a1)
    print(a2)

    a1.credit(50)
    print(a1.query())


    a1.debit(50)
    print(a1.query())



