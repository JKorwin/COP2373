# This program will ask the user for different expenses and then analyze and display the total, lowest, and highest
# expense
# importing functools to use reduce method
import functools

# creating a function that asks the user for a set of expenses and saves them as tuples
def expense_list():
    # initializing list
    list_of_expenses = []
    # getting number of expenses to know how many times to run the loop
    expense_number = int(input('Please enter the number of monthly expenses you would like to enter: '))

    # creating loop to get the list of expeses
    for x in range(0, expense_number):
        expense_name = input('Please enter the type of expense (rent, transportation, etc.): ')
        expense_amount = float(input(f'Please enter your {expense_name} expense: $'))
        expense = expense_name, expense_amount
        list_of_expenses.append(expense)
    return list_of_expenses


# creating a min max function that uses the return method to analyze the second element of the tuples and returns
# the tuples that have the minimum expense and maximum expense
def min_max(list_of_expenses):
    highest_expense = functools.reduce(lambda x, y: x if x[1] > y[1] else y, list_of_expenses)
    lowest_expense = functools.reduce(lambda x, y: x if x[1] < y[1] else y, list_of_expenses)
    return highest_expense, lowest_expense

# defining function finding sum using reduce method
def sum_expenses(list_of_expenses):
    return functools.reduce(lambda x, y: x+y[1], list_of_expenses, 0)

# defining main function that creates the list of expenses, gets the highest expense, sum of expenses, and
# lowest expense and then displays them to user
def main():
    # creating list of expenses
    list_of_expenses = expense_list()

    # getting highest and lowest expense
    highest_expense, lowest_expense = min_max(list_of_expenses)

    #getting sum of expenses
    expenses_sum = sum_expenses(list_of_expenses)

    # printing results with good format
    print(f'Total expenses: ${expenses_sum:.2f}')
    print(f'Your highest expense is {highest_expense[0]} expense for ${highest_expense[1]:.2f}.')
    print(f'Your lowest expense is {lowest_expense[0]} expense for ${lowest_expense[1]:.2f}.')

# calling main function
main()








