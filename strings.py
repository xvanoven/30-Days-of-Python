# 1. Concatenate to Thirty Days of Python

str1 = "Thirty"
str2 = "Days"
str3 = 'Of'
str4 = 'Python'

print(str1 + " " + str2 + " " + str3 + " " + str4 + ".")

# 2. Concatenate to Coding For All

str1 = 'Coding'
str2 = 'For'
str3 = 'All'

print(str1 + " " + str2 + " " + str3 + ".")

# 3. Declare variable company, assign "Coding for All"

company = 'Coding for All'

# 4. Print variable company using print()

print(company)

# 5. Print the length of the company using len() and print()

print(len(company))

# 6. Change all the characters to uppercase letters

company = company.upper()

# 7. Do 6. with lower

company = company.lower()

# 8. Use capitalize(), title(), swapcase() method to format the value of the string Coding For All

print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All String

print(company[7:])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.

if 'Coding' in company:
    print('Substring "Coding" found in company!')

# 11. Replace the word coding in the string 'Coding For All' to Python.

print(company.replace('coding', 'python'))

# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.

str1 = 'Python for Everyone'.lower()
print(str1.replace('all', 'everyone'))

# 13. Split the string 'Coding For All' using space as the separator (split()) .

str1 = 'Coding For All'
print(str1.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

str1 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(str1.split(', '))

# 15. What is the character at index 0 in the string Coding For All.

str1 = 'Coding For All'
print(str1[0])

# 16. What is the last index of the string Coding For All.

print(str1[-1])

# 17. What character is at index 10 in "Coding For All" string.

car10 = str1[10]
if car10 is " ":
    print("The character at index 10 in str1 is a space.")
else:
    print(car10)

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.

str1 = 'Python for Everyone'
acronym = "".join([word[0].upper() for word in str1.split()])
print(acronym.lower())

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.

str1 = 'Coding For All'
acronym = "".join([word[0].upper() for word in str1.split()])
print(acronym.lower())

# 20. Use index to determine the position of the first occurrence of C in Coding For All.

print(str1.lower().index('c'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.

print(str1.lower().index('f'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.

str1 = 'Coding For All People'
print(str1.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

str1 = 'You cannot end a sentence with because because because is a conjunction'
print(str1.index('because'))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(str1.rindex('because'))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(str1.replace('because because because ', ""))

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(str1.index('because'))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(str1.replace('because because because ', ""))

# 28. Does 'Coding For All' start with a substring Coding?

str1 = 'Coding For All'
if 'Coding' in str1:
    print("Coding For All has Coding as a substring.")
else:
    print("Coding For All does not have Coding as a substring.")

# 29. Does 'Coding For All' end with a substring coding?

if str1.endswith('coding'):
    print("Yes!")
else:
    print("No.")

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.



# 31. Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython, thirty_days_of_python



# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.



# 33. Use the new line escape sequence to separate the following sentences.



# 34. Use a tab escape sequence to write the following lines: 



# 35. Use the string formatting method to display the following:



# 36. Make the following using string formatting methods: 



