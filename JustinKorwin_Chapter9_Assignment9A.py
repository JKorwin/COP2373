# This program will create a BankAcct class which will house various pieces of information regarding a bank account
# Methods for changing these pieces of information such as amount in bank account and interest rate will be implemented
# The __str__ method will be used to display balances and interest amounts
# A test function will then be created to test all these methods
# Just a note, I turned a lot of values into float values because I kept getting errors

# making the BankAcct class
class BankAcct:
    # initializing all the info that the class will store
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)

    # creating method for adjusting interest rate
    def interest_rate_adjust(self, adjusted_rate):
        self.interest_rate = float(adjusted_rate)

    # creating method for depositing money
    def deposit(self, deposit_amount):
        self.amount += float(deposit_amount)

    # creating method for withdrawing money
    def withdraw(self, withdraw_amount):
        # adding if statement because you cannot withdraw more money than you have
        if float(withdraw_amount) > self.amount:
            print('Not enough money.')
        else:
            self.amount -= float(withdraw_amount)

    # creating method to get the balance
    def get_balance(self):
        return self.amount

    # creating method to calculate interest based on number of days
    def interest_calculator(self, number_of_days):
        # this calculation assumes interest rate is given in percent and the rate is annual
        interest_amount = self.amount * (float(self.interest_rate) / 100) * (float(number_of_days) / 365)
        return interest_amount

    # creating method using __str__ to display the balance and interest rate
    def __str__(self):
        return f'Balance: {self.amount}\nInterest rate: {self.interest_rate}'

# creating the test function to ensure functionality of all the methods

def test_function():
    # creating an instance of the class and accepting information from user to fill in the info
    account = BankAcct(input('Please enter your name: '), input('Please enter your bank account number: ')
                       , float(input('Please enter your bank account balance: ')), float(input('Please enter your interest rate: ')))

    # testing method to change interest rate
    adjust_amount = input('Please enter your new interest rate: ')
    account.interest_rate_adjust(adjust_amount)
    print(account)

    # testing method to withdraw
    amount_withdraw = input('Please enter the amount you would like to withdraw: ')
    account.withdraw(amount_withdraw)
    print(account)

    # testing method to deposit
    amount_deposit = input('Please enter the amount you would like to deposit: ')
    account.deposit(amount_deposit)
    print(account)

    # testing method to get balance
    balance = account.get_balance()
    print('Current balance: ', balance)


    # testing method to calculate interest
    days = input('Please enter the amount of days you will accumulate interest: ')
    interest = account.interest_calculator(days)
    print('Amount of interest for', days, f'days: {interest:.2f}')

# calling test function
test_function()






