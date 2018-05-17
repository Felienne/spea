# 
Here is the code that guesses a random number until it finds 7. Run the code to find out what it does.

To pass the test, simply print the secret number once.



secret_value = 7 #<-- the secret value (not so secret in this case of course)
guess = 1 #<-- the first guess we try
while secret_value != guess: #<-- while we have not correctly guessed the answer
    guess = random.randint(1,10) #<-- try a new guess between 1 and 10
    print('That was one guess')
print("The secret number is... ", guess)