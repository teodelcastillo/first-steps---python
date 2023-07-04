# This is a simple calculator for everyone.

print('Hello world! I\'m a a math genius, just ask any operation with numbers and i\'ll solve it.')
print()

# Ask the user what kind of operation they want to do.

def let_user_pick(operation_options):
    print("Please choose what kind of operation you want: ")

    for idx, element in enumerate(operation_options):
        print("{}) {}".format(idx + 1, element))

    while True:
        i = input('Enter number from the list: ')
        try:
            if 0 < int(i) <= len(operation_options):
                return int(i) - 1
        except:
            pass
        print('Invalid input, please, start again.')


operation_options = ["Adition.", "Sustraction.", "Division.", 'Multiplication.']
chosen = let_user_pick(operation_options)+1


print('Chosen: ', chosen)

print()
print('Choose your numbers.')
x = float ( input('Enter the first number: '))
y = float ( input('Enter the second number: '))

result_adition = float(x + y)
result_division = float(x / y)
result_multiplication = float(x*y)
result_substraction = float(x-y)

if chosen == 1:
    print('Here is your operation: ', x, '+', y,'=', result_adition)

if  chosen == 2:
    print('Here is your operation: ', x, '-', y,'=',result_substraction)

if  chosen == 3:
    print('Here is your operation: ', x, '/', y,'=',result_division)

if  chosen == 4:
    print('Here is your operation: ', x, '*', y,'=',result_multiplication)

