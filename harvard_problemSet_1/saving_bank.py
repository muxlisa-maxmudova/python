def bonus():
    greet = input('Greeting: ')
    if greet.find('Hello')>-1:
        print('$0')
    elif greet.find('H')>-1:
        print('$20')
    else:
        print('$100')
bonus()