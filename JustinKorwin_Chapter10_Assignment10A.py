# this program will use the inheritance approach to create a class definition of Money that will support addition, multiplication and subtraction

# using inheritance approach from section 10.12
from decimal import Decimal
class Money(Decimal):
    def __new__(cls, v, units='USD'):
        return super(Money, cls).__new__(cls, v)
    def __init__(self, v, units='USD'):
        self.units = units

    # creating method for addition
    def addition(self, add_value):
        return Money(super().__add__(Decimal(add_value)), self.units)
    # creating method for subtraction
    def subtraction(self, sub_value):
        return Money(super().__sub__(Decimal(sub_value)), self.units)
    # creating method for multiplication
    def multitply(self, mult_value):
        return Money(super().__mul__(Decimal(mult_value)), self.units)

# creating test function for all the methods above
def test():
    # creating two instances of Money to test with
    money1 = Money('1000.00', 'USD')
    money2 = Money('250.00', 'USD')

    # printing results of different methods to ensure they are correct
    result1 = money1.addition(money2)
    print(result1)

    result2 = money1.subtraction(money2)
    print(result2)

    result3 = money1.multitply(3)
    print(result3)

# running test function
test()

