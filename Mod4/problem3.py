'''
Prompt the user for their bank balance. Evaluate whether the balance is less than $100.
Print True if the user’s balance is below $100; print False, otherwise.
'''

bank_balance = float( input("What is your bank balance ?: $"))

if bank_balance < 100 :
    print(True)
    
else:
    print(False)

