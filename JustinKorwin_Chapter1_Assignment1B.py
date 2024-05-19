# This program will simulate a magic 8-ball fortune telling toy
# This program will repeat until the user is ready to quit

# importing random
import random

# defining function
def main():
    # adding all phrases as a list
    phrases = ['Yes, of course!', 'Without a doubt, yes.', 'You can count on it.', 'For sure!', 'Ask me later!',
           "I'm not sure.", "I can't tell you right now.", "I'll tell you after my nap.", 'No way!',
           "I don't think so.", 'Without a doubt, no.', 'The answer is clearly NO!']

    # opening a file in write mode and inputting all the phrases then closing file
    file = open('8ball_responses.txt', 'w')
    file.writelines(phrases)
    file.close()

    # opening file in read mode
    file = open('8ball_responses.txt', 'r')

    # creating loop that only continues as the user wants it to with lower command to avoid error because of
    # case sensitivity
    user_wants = 'yes'

    # user_question is used in the loop to ensure the phrase does not come before the user enters a question
    user_question = ''
    while user_wants.lower() == 'yes':

        # prompting user to ask a yes or no question
        while user_question == '':
            user_question = input('Please ask a yes or no question:')

        # setting user_question back to nothing incase user wants to ask another question
        user_question = ''

        # randomly choosing a phrase from the list
        phrase = random.choice(phrases)

        # displaying phrase
        print(phrase)

        # asking user if they want to continue
        user_wants = input('Would you like another fortune? yes/no')

    # closing file and telling the user thanks for using magic 8-ball python edition
    file.close()
    print('Thanks for using magic 8 ball fortune telling toy python edition. Have a great day!')

# calling on function
main()