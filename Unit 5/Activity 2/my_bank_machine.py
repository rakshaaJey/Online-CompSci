'''
Rakshaa Jeyarajah
24 03 2022
ATM service
'''
#imports
import atm

#functions

#main line
bank_name = str(input("What is the name of the bank: "))
while True:
    try:
        balance = int(input("What is the initial balance? $"))
        while balance <= 0:
            print("The balance must be larger than 0")
            balance = int(input("What is the initial balance? $"))
    except ValueError:
        print("Invalid Input!")
    else:
        break
    
bank_account = atm.Atm(balance)

while True:
    
    print("\n*********************************\n* 1. Deposit\t2. Show Balance *\n* 3. Withdraw\t4. Add Interest *\n* 5. Quit\t\t\t*\n*********************************")
    while True:
        try:
            choice = int(input("What would you like to do: "))
            while choice > 5 or choice < 1:
                print("Invalid Input")
                choice = int(input("What would you like to do: "))
        except ValueError:
            print("Invalid Input")
        else:
            break
        
    if choice == 1:
        while True:
            try:
                deposit_value = float(input("How much money would you like to deposit: $"))
                while deposit_value < 0:
                    print("Invalid Input")
                    deposit_value = float(input("How much money would you like to deposit: $"))
            except ValueError:
                print("Invalid Input")
            else:
                break
        print("${} has been added to the account.".format(deposit_value))
        bank_account.deposit_money(deposit_value)
        print(bank_account)
        
    elif choice == 2:
        print(bank_account)
        
    elif choice == 3:
        while True:
            try:
                withdraw = float(input("How much money would you like to withdraw: $"))
                while withdraw < 0 or withdraw > bank_account.get_current_balance():
                    print("Invalid Input")
                    withdraw = float(input("How much money would you like to withdraw: $"))
            except ValueError:
                print("Invalid Input")
            else:
                break
        print("${} has been removed from the account.".format(withdraw))
        bank_account.withdraw_money(withdraw)
        print(bank_account)
        
    elif choice == 4:
        while True:
            try:
                percent_interest = float(input("What is the annual interest rate (%): "))
            except ValueError: 
                print("Invalid Input")
            else:
                break
            
        while True:
            try:
                days = int(input("What is the number of days? "))
                while days < 0:
                    print("Invalid Input")
                    days = int(input("What is the number of days? "))
            except ValueError:
                print("Invalid Input")
            else:
                break
        
        interest = bank_account.compound_interest_calculator(days, percent_interest)
        print("Interest : ${}".format(round(interest - bank_account.get_current_balance(), 2)))
        bank_account.set_current_balance(interest)
        print(bank_account)
        
    else:
        break

print("Thank you for using",bank_name,"atm service!")
