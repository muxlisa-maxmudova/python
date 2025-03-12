# def converter(temp):
#  print(round((9*temp)/5 + 32, 1))
# converter(25)

def converter(temp, v):
    if v == 'C':
       return (temp * 9 / 5) + 32
    elif v == 'F':
       return (temp - 32) *5 / 9

print(converter(86, 'F'))
