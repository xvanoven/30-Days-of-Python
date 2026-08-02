x = input('What is your name?\n') # takes input from user and stores it in a variable

print('\nHello, ' + x + '!') # prints the input string

print('The Characters in your name including spaces is ' + str(len(x))) # prints the length of the input string
print('The data type of your name is ' + str(type(x))) # prints the data type of the input string
print('Your name spelled backwards is ' + x[::-1].upper()) # prints the input string in reverse order
print('The third character of your name is ' + x[2].upper()) # prints the third character of the input string