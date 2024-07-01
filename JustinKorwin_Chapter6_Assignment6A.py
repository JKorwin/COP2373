# This code will validate phone numbers, social security numbers and zip codes via the use of regular expressions
# importing regular expressions
import re

# defining function for validating phone numbers
def phone_number_validate(phone_number):
    # using return bool to give a true or false with re.match to determine if the pattern matches
    return bool(re.match(r'\d\d\d-\d\d\d-\d\d\d\d$', phone_number))

# defining function for validating a social security number in the same way I did for phone numbers
def social_security_validate(social_security_number):
    return bool(re.match(r'\d\d\d-\d\d-\d\d\d\d$', social_security_number))

# defining function for validating zipcodes in the same way
def zipcode_validate(zipcode):
    return bool(re.match(r'\d\d\d\d\d$', zipcode))

# defining main function that asks for inputs then calls on other functions
def main():
    # asking user for inputs with the correct format
    phone_number = input("Please enter a phone number in the format xxx-xxx-xxxx : ")
    social_security_number = input ("Please enter a social security number in the format xxx-xx-xxxx : ")
    zipcode = input("Please enter a zipcode in the format xxxxx : ")

    # setting up if else statements using the boolean values returned
    if phone_number_validate(phone_number) == True :
        print("The phone number is valid.")
    else:
        print("The phone number is invalid.")

    if social_security_validate(social_security_number) == True :
        print("The social security number is valid.")
    else:
        print("The social security number is invalid.")

    if zipcode_validate(zipcode) == True :
        print("The zipcode is valid.")
    else:
        print("The zipcode is invalid.")

# calling main function
main()