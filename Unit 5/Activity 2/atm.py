import math

class Atm(object):
    
    def __init__(self, current_balance):
        self.current_balance = current_balance
    
    def get_current_balance(self):
        '''
        Returns the current balance of the atm object
        '''
        return self.current_balance
    
    def set_current_balance(self, balance):
        '''
        @param balance is the new balance

        Changes the balance of the robot to the given balance
        '''
        self.current_balance = balance
    
    def withdraw_money(self, withdraw_amount):
        '''
        @param withdraw_amount is the amount to withdraw from the account

        Withdraws the given amount from the balance
        '''
        self.current_balance -= withdraw_amount
    
    def deposit_money(self, deposit_amount):
        '''
        @param deposit_amount is the amount to deposit from the account

        Deposit the given amount from the balance
        '''
        self.current_balance += deposit_amount

    def compound_interest_calculator(self, days, interest_percent):
        '''
        @param days is the amount of days the interest has to accumulate
        @param interest_percent is the percent interest

        Calculates the compound interest of the bank account using the given variables
        '''

        p = self.current_balance
        i = (interest_percent/100)/365
        n = 365 * (days/365)
        p * math.pow((1+i), n)
        return p * math.pow((1+i), n)

    def __str__(self):
        '''
        Returns the properties of the car
        '''
        return 'Current Balance: ${}'.format(round(self.current_balance, 2))