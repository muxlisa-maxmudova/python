# name = input('Enter your full name: ')
phone_number = input('Enter your phone number: ')
# result=len(name)
# result = name.rfind("q")
# name = name.capitalize() # in js we used to use toUpperCase
# name = name.upper()
# name = name.lower()
# result = name.isdigit() # only returns true if only numbers
# result = name.isalpha() # true => only letters
# result = phone_number.count('-') # counts how many dashes are there
result = phone_number.replace('-', '')
print(result)