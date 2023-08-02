# intialise Answer var and assign value
intAnswer = 123
# intialise Guess var and assign value
intGuess = 1

# start WHILE loop
while intGuess != 0:

   # get the input from user to assign to variable
   intGuess = int(input("Enter your Guess or 0 to Exit:"))

   #compare variable and print outcome
   if intAnswer == intGuess:
    print("Your Guess", intGuess, "is CORRECT.")
   else:
    print("Your Guess", intGuess, "is WRONG.")
