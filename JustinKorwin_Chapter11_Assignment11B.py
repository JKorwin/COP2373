# this program will determine the length of a hypotenuse or a right triangle given the nearest angle and the length of the adjacent side
# importing math
import math

# creating main function that will do all the work
def main():
    # asking for the nearest angle and length of adjacent side from user
    angle = float(input("Please enter the nearest angle measured in degrees: "))
    length = float(input("Please enter the length of the adjacent side: "))

    # calculating the radians from the degrees given
    radians = math.radians(angle)

    # calculating the hypotenuse using cosine with the radians gotten
    hypotenuse = length / math.cos(radians)

    # displaying results with good format rounded to two decimal places
    print(f"The length of the hypotenuse is {hypotenuse:.2f}")

# calling main funciton
main()