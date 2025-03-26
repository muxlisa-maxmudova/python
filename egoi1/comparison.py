def compare():
    a = int(input(''))
    b = int(input(''))
    if a < 2*10**9 and b < 2*10**9:
      if a > b:
        print('>')
      elif b>a:
        print('<')
      elif a == b:
        print('=')
    else:
        print('Oh! Too much!')
compare()