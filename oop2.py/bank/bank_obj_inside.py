#this file is inside bank package
#call module
from customer import Customer
from account import Account

cus1 = Customer()
cus1.new_customer()

cus1_acc = Account()
cus1_acc.open_account(cus1.name,"Saving",'10-123-456',500)

print("**** Opem Bank Account Deatail ****")
print(cus1.cus_info())
print(cus1_acc.diplay_balance())
#print(cus1.cus_info()),