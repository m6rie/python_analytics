# Write a function that calculates a number's factorial


def factorial(num):
    # get user to input a number
    num = int(
        input(
            "Which number would you like to get the factorial of (positive number only)? "
        ))
    # check that the input number is an integer
    # if it is not an int or if it is less than 0, return None
    if type(num) is not int:
        return None
    if num < 0:
        return None
    # if it is 0, return 1
    if num == 0:
        return 1

    # creates variables to help loop through the numbers
    i = 0  # let's start with the int 0
    j = 1  # and it's factorial 1

    # loop through the numbers in the range num to 0
    # for each number
    for number in range(num):
        i = i + 1  # increment the int by 1
        j = j * i  # reasign j with the product of the previous j and incremented i

    # once we've looped through all the numbers in the range num to 0, return the value of j
    return j


print(factorial(6))
