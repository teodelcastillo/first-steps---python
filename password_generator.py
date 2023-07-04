### This program generates random passwords. User must assign password length, and in case there are some forbiden characters, will be able to indicate it.

def password_generator ():

    import random
    import string
    
    characters = string.ascii_letters + string.digits + string.punctuation + string.hexdigits

    while True:
        psw_length = input('Enter the password length: ')
        if not psw_length.isdigit() or int(psw_length) < 1 :
            print('Invalid password length. Expected to be at least longer than 1.')
        else:
            psw_length = int(psw_length)
            break

    forbidden = input('Enter forbidden characters separating them with a comma (,), if there are none, just pass: ')
    forbidden_list = [character for character in forbidden.split(',')]
    password = ''.join(random.choice([c for c in characters if c not in forbidden_list]) for i in range(psw_length))

    return print(password)

password_generator()