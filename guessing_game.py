# This is a guessing game against your PC
# There are some extra lines so as to make it a little bit more interactive.

# Introduction for user
print('Hello world! This is a guessing game between you, and your PC.')
print('Don\'t worry about chances, for this time you can try as much as you want.')
print()
print('Rules: ')
print('''1. Computer will think a number between 1, and a 1000.
2. You must guess what number is.
3. If your number is lower the one the PC choose, it will tell you it\'s too low.
4. If your number is higher the one the PC choose, it will thell you it\'s too high. ''')
print()

print('Ready? Lets play!')
print()

# Just interactive prints as if PC is joking.
print('PC: \"Ha! you\'re never going to guess my number, Im just built different.')
print()

import  random

number = random.randrange (1,1000)                # This is a random number the PC will choose.
guess = int(input('Enter your first guess: '))    # Input for user to guess

while number != guess:  # Loop until reaching objective, or guessing.

    if  guess < number:
            print('Ha! Too low! \n')
            guess = int (input('Try again with a higher number: ')) # You must redefine the var, if not, it will allways be as first user input.

    elif guess > number:
          print('Of course not! Too high! xD \n')
          guess = int(input('Try again with some lower number: '))
    
    else:
          break

print()
print('THERES NO WAY! :\'(')
print('You did it! Hmm.. Are you a magician?')

