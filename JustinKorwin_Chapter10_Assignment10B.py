

from decimal import Decimal
# copy and pasting money class with some changes because it wouldn't work otherwise
class Money(Decimal):
    def __new__(cls, v, units='USD'):
        object = super(Money, cls).__new__(cls, v)
        object.units = units

    def __init__(self, v, units='USD'):
        pass

    # creating method for addition
    def addition(self, add_value):
        return Money(super().__add__(Decimal(add_value)), self.units)
    # creating method for subtraction
    def subtraction(self, sub_value):
        return Money(super().__sub__(Decimal(sub_value)), self.units)
    # creating method for multiplication
    def multiply(self, mult_value):
        return Money(super().__mul__(Decimal(mult_value)), self.units)

class BankAcct(Money):
    # rewriting some stuff because we are now using inheritance with the Money class
    def __new__(cls, amount, units='USD', name='', account_number='', interest_rate=0.0,):
        object = super(BankAcct, cls).__new__(cls, amount, units)
        object.name = name
        object.account_number = account_number
        object.interest_rate = interest_rate
        return object

    # initializing all the info that the class will store minus what already was above
    def __init__(self, amount, units='USD', name='', account_number='', interest_rate=0.0):
        super().__init__(amount, units)


    # creating method for adjusting interest rate
    def interest_rate_adjust(self, adjusted_rate):
        self.interest_rate = float(adjusted_rate)

    # creating method for depositing money using addition from Money
    def deposit(self, deposit_amount):
        deposit_amount = Money(deposit_amount, self.units)
        return BankAcct(self.addition(deposit_amount), self.units, self.name, self.account_number, self.interest_rate)

    # creating method for withdrawing money using subtraction from Money
    def withdraw(self, withdraw_amount):
        withdraw_amount = Money(withdraw_amount, self.units)
        # adding if statement because you cannot withdraw more money than you have
        if withdraw_amount > self:
            print('Not enough money.')
            return self
        return BankAcct(self.subtraction(withdraw_amount),self.units, self.name, self.account_number, self.interest_rate)


    # creating method to get the balance
    def get_balance(self):
        return self

    # creating method to calculate interest based on number of days
    def interest_calculator(self, number_of_days):
        # this calculation assumes interest rate is given in percent and the rate is annual
        interest_amount = float(self) * (float(self.interest_rate) / 100) * (float(number_of_days) / 365)
        return interest_amount

    # creating method using __str__ to display the balance and interest rate
    def __str__(self):
        return f'Balance: {self}\nInterest rate: {self.interest_rate}'


def test_function():
    # creating an instance of the class and accepting information from user to fill in the info
    name = input('Please enter your name: ')
    account_number = input('Please enter your bank account number: ')
    amount = float(input('Please enter your bank account balance: '))
    interest_rate = float(input('Please enter your interest rate: '))
    account = BankAcct(amount, 'USD', name, account_number, interest_rate)

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
    print(balance)


    # testing method to calculate interest
    days = input('Please enter the amount of days you will accumulate interest: ')
    interest = account.interest_calculator(days)
    print('Amount of interest for', days, f'days: {interest:.2f}')

# calling test function
test_function()
