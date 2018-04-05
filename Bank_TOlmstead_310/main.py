# driver program
# populate a bank from a file
# process a set of transactions
# summarize bank state

import Account
import Bank

import io

# create a bank with a given routing number

my_bank = Bank.Bank(123456789)


# read the account file and populate the bank
#  accounts are of the form
#  account_num | balance | owner

with open("initial_balances.csv") as f:
    content = f.readlines() # content is a list of lines of text
    # strip trailing newlines
    content = [line.rstrip() for line in content]

account_tuples = [tuple(line.split('|')) for line in content]

account_tuples

# convert data types while adding accounts
for account_num,balance,owner in account_tuples:
    my_bank.add_account(Account.Account(int(account_num),owner,float(balance)))

print(my_bank)

for owner,account in my_bank.accounts.items():
    print("num: {} owner: {} balance: ${}".format(account.account_num,account.owner,account.query()))


# load transactions
#
#  transaction format:
# origin routing number | origin account | dest routing | dest acct| amt


with open("transactions.csv") as f:
    content = f.readlines()
    # strip trailing newlines
    content = [line.rstrip() for line in content]

transaction_tuples = [tuple(line.split('|')) for line in content]

# convert strings to int/float as necessary for a transaction
def fix_t_tuple(trans):
    origin_routing_num, origin_acct, dest_routing_num,dest_acct,amt = trans
    return(int(origin_routing_num),int(origin_acct),
        int(dest_routing_num), int(dest_acct),float(amt))

transaction_tuples = [fix_t_tuple(t) for t in transaction_tuples]
transaction_tuples[:10]


fails=[]
for trans in transaction_tuples:
    res=my_bank.process_transaction(*trans)
    if not res:
        fails.append(trans)

if fails:
    print("something is wrong with these transactions:")
    print(str(fails))



# overdraft report:

over_accounts=[]
for account in my_bank.accounts.values():
    if account.query() < 0:
        over_accounts.append(account)

for account in over_accounts:
    print(account)


max_num, max_account = max(my_bank.accounts.items(), key=lambda p:p[1].query())

max_num
print(max_account)

sort(list(my_bank.accounts.items()))

print(max_account)
