# This program will pre-sell a limited number of cinema tickets
# After each buyer buys tickets the total of tickets left will be displayed
# Total number of buyers will be displayed at the end
# initial statement telling the user what the program is
#defining function
def main():
    print('Welcome. This is an application that allows you to buy cinema tickets.'         
          '\nThere are a total of 20 tickets and you can buy a maximum of 4.')

    # establish that there are 0 buyers and 20 tickets at the beginning
    number_of_buyers = 0
    number_of_tickets = 20

    # create a while loop to sell tickets
    while number_of_tickets > 0:

        # accept input from user for number of tickets they want to buy
        tickets_bought = int(input('Please enter the number of tickets you would like to buy:'))

        # creating if statements for if user is trying to buy more than 4 tickets
        # or if user is trying to buy more tickets than there are tickets left
        if tickets_bought > 4:
            print('You are only able to buy a maximum of 4 tickets. Try again.')
            continue
        if tickets_bought > number_of_tickets:
            print('You are attempting to buy more tickets than there are tickets available. Try again.')
            continue

        # subtracting tickets bought from number of tickets
        number_of_tickets -= tickets_bought

        # adding 1 to number of buyers
        number_of_buyers += 1

        # displaying tickets left
        print('There are',number_of_tickets, 'tickets left.')

    #displaying total number of buyers
    print('All tickets sold. Total number of buyers:',number_of_buyers)

#calling function
main()