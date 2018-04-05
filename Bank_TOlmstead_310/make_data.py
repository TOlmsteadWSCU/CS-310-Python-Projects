import pandas as pd
import numpy as np



names = pd.read_csv("sample_names.csv")

names["x"]

np.random.seed(42)

init_bals = pd.DataFrame({'owner':names['x'],
  'balance': np.random.randint(500,2200,100),
  'account_num':range(656332,656332+100)})

init_bals

init_bals.to_csv("initial_balances.csv",sep='|',header=False,index=False)


# account numbers: range(656332,656332+100)
# routing number: 123456789



from_acctn= np.random.choice(range(656332,656332+100),1000,replace=True)
to_acctn= np.random.choice(range(656332,656332+100),1000,replace=True)
amts = np.random.randint(250,1100,1000)

transactions = pd.DataFrame({'origin_acct':from_acctn,'dest_acct':to_acctn,'amt':amts})

good_trans=transactions[transactions['origin_acct'] != transactions['dest_acct']]
good_trans['origin_routing_num']=123456789
good_trans['dest_routing_num']=123456789

len(good_trans)

good_trans.iloc[:3,4]=987654321
good_trans.iloc[2:4,3]=987654321

good_trans.loc[:10,:]

good_trans = good_trans.reindex(columns=['origin_routing_num','origin_acct','dest_routing_num','dest_acct','amt'])

good_trans.loc[:10,:]

good_trans.to_csv("transactions.csv",sep='|',header=False,index=False)
