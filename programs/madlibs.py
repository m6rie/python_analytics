# Create a madlibs
# Get user input
# Handle error when the input has the wrong data type

word1 = input("Please enter the name of a room: ").upper()
word2 = input("Please enter an adjective: ").upper()
word3 = input("Please enter a liquid: ").upper()
word4 = input("Please enter a noun: ").upper()
word5 = input("Please enter an adjective: ").upper()
word6 = input("Please enter a plural noun: ").upper()
word7 = input("Please enter an adjective: ").upper()
word8 = input("Please enter an adjective: ").upper()
word9 = input("Please enter a non-decimal number: ")
try:
    num9 = int(word9)
except ValueError:
    print("Try again with a non-decimal number!")
    word9 = input("Please enter a non-decimal number: ")

word10 = input("Please enter another non-decimal number: ")
try:
    num10 = int(word10)
except ValueError:
    print("Try again with a non-decimal number!")
    word10 = input("Please enter a non-decimal number: ")

word11 = input("Please enter a liquid: ").upper()

print(
    f"I love my new couch it is located in my {word1} it’s nice and {word2}. "
    + "I like to sit and lay down on it while I do many activities such as " +
    f"read a book while drinking a nice cold cup of {word3}, playing on my {word4} or listening to a good song. "
    +
    f"I like the cushions on my couch they remind me of {word5} {word6} and they are very {word7} to sleep on, "
    +
    "but the armrests are the most comfortable they fit the shape of my arms perfectly and "
    +
    f"don’t forget they are {word8} but I can never forget about the cup holder as it can hold {word9} to {word10} cups of hot or cold {word11}."
)
