# create the answer
intAnswer = 12345

# get the input from user to assign to variable
intGuess = int(input("Enter your Guess:"))

#print("Answer =", intAnswer)
#print("Guess =", intGuess)

if intAnswer == intGuess:
    print("Your Guess", intGuess, "is CORRECT.")
else:
    print("Your Guess", intGuess, "is WRONG.")
