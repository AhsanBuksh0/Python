# import random library
import random

# intialise Answer var and assign value
intAnswer = random.randint(1000, 9999)
# intialise Guess var and assign value
intGuess = 1

# start WHILE loop
while intGuess != 0:

   # get the input from user to assign to variable
   intGuess = int(input("Enter your Guess or 0 to Exit:"))

   #compare variable and print outcome
   if intGuess == 0:
       print("Goodbye")
       break
   elif intAnswer < intGuess:
    print("Your Guess", intGuess, "is TOO HIGH.")
   elif intAnswer > intGuess:
    print("Your Guess", intGuess, "is TOO LOW.")
   else:
    print("Your Guess", intGuess, "is CORRECT.")
    break
