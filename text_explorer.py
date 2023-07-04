# User input text
# Program counts words, letters, commas, and dots.

print()
print('Hello world! I\'m a text analizer.')
print('I count words, letters, and more!')
print()
print()

user_text = input('Copy your text here: ')

# Program
characters = (user_text)
words = user_text.split()   # It creates a lists with input info.
dots = user_text.split('.')
commas = user_text.split(',')

print()
print('Your text has: ', len(characters),'characters, ', len(words),' words, ', len(dots)-1,' dots, and ', len(commas)-1, 'commas.\n')
print('Total characters: ', len(characters))
print('Total words: ', len(words))
print('Total commas: ', len(commas)-1)
print('Total dots: ', len(dots)-1)