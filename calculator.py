# Python calculator

operator = input("Enter an operator (+ / - *): ")

num1 = float(input('Enter the first number: ')) # if we do not add int() then we will result string concatenation

num2 = float(input('Enter the second number: '))

if operator=="+":
    result = (num1+num2)
    print(result)
elif operator=="-":
    result = (num1-num2)
    print(result)
elif operator=="*":
    result = (num1*num1)
    print(result)
elif operator=="/":
    result = (num1/num2)
    print(result)
else:
    print(f'{operator} is not valid')

