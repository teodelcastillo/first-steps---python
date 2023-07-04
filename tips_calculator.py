### This is a tip calculator. User must indicate what porcentage of the bill is willing to give as a tip, and then, input the total bill. Program will do the rest.

def tip_calculator():

    while True:
        willing_percentage = input('What porcentage of the total bill are you willing to give as a tip? Only numbers. ')
        if not willing_percentage.isdigit() or float(willing_percentage) < 0 :
            print('Please, enter just numbers.')
        else:
            percentage = float(willing_percentage) / 100
            break

        print (percentage)
    
    while True:
        bill = input('Insert the total of the bill: ' )
        if not bill.isdigit() or float(bill) < 0:
            print('Please, enter a valid number.') 
        else:
            tip = float(bill) * percentage
            break

    return  print('A ',willing_percentage, '% tip for a $', bill,' is $',tip,'.')
    
tip_calculator()


