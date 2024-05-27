# This code will search through a user inputted email message for words and phrases that
# are commonly found in spam emails and tell the user the spam score, likelihood of spam,
# and the spam words and phrases found

# defining the spam score function
def spam_score_function(email_message, spam_words):
    # initializing spam score variable and words found list
    spam_score = 0
    words_found = []

    # making the email message lowercase to avoid problems with case sensitivity
    lowercase_email = email_message.lower()

    # using a for loop to search for spam words and an accumulator to add up spam score
    # and then store the spam words found
    for word in spam_words:
        if word in lowercase_email:
            spam_score += 1
            words_found.append(word)

    # return the spam score and words found
    return spam_score, words_found


# defining function that rates the likelihood of spam and returns message stating the likelihood
# of spam
def likelihood_function(spam_score):
    if spam_score == 0:
        return 'Not spam.'
    elif spam_score <= 2:
        return 'Probably not spam.'
    elif spam_score <= 8:
        return 'Probably spam.'
    else:
        return 'High probability of spam.'

# defining main function that combines everything together
def main():
    # creating list of spam words
    spam_words = ['free', 'winner', 'urgent', '$', 'congratulations', 'guaranteed',
                  'all new', 'special promotion', 'gift', 'giving away', '#1', 'you have been selected',
                  'no strings attached', 'click below', 'click here', 'prize', 'sale', '50% off',
                  'cash bonus', 'best rates', 'lowest price', 'opportunity of a lifetime', 'cheap',
                  'unlimited', 'money', 'income', 'no obligation', 'sign up free today', 'certified',
                  'bonus', 'amazing']

    # getting email message from user
    email_message = input('Please enter the email message:')

    # adding up spam score and saving spam words and phrases found from spam score function
    spam_score, words_found = spam_score_function(email_message, spam_words)

    # rating the likelihood of spam with liklihood function
    spam_likelihood = likelihood_function(spam_score)

    # printing spam score and spam likelihood
    print('Spam score: ', spam_score)
    print('Spam likelihood: ', spam_likelihood)

    # printing spam words and phrases using comprehension because it was in the chapter
    print('Spam words and phrases found: ' if words_found else "So spam words or phrases found.")
    [print(word) for word in words_found]



# calling main function
main()
