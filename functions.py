x = input('What is your name?\n') # takes input from user and stores it in a variable

print('\nHello, ' + x + '!') # prints the input string

print('The Characters in your name including spaces is ' + str(len(x))) # prints the length of the input string
print('The data type of your name is ' + str(type(x))) # prints the data type of the input string
print('Your name spelled backwards is ' + x[::-1].upper()) # prints the input string in reverse order
print('The third character of your name is ' + x[2].upper()) # prints the third character of the input string

# --------------------------------------------------------------------- #

first_name = 'Xander'
last_name = 'Vanoven'
country = 'United States'
city = 'Houston'
age = 45

# Printing types
print(type(first_name))                 # str
print(type(last_name))                  # str
print(type(country))                    # str
print(type(city))                       # str
print(type(age))                        # int

print(type(10))                         # int
print(type(3.14))                       # float
print(type(1 + 3j))                     # complex
print(type('xvanoven'))                 # string
print(type(True))                       # boolean
print(type([1, 2, 3]))                  # list
print(type({'name':'xvanoven'}))        # dictionary
print(type((1,2)))                      # tuple
print(type(zip([1, 2, 3], [4, 5, 6])))  # zip

# int to float
num_int = 10
print('num_int',num_int)
num_float = float(num_int)
print('num_float:', num_float)

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Xander'
print(first_name)               # 'Xander'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['X', 'a', 'n', 'd', 'e', 'r']