def main():
  while True:
        n = int(input(''))
        p = int(input(''))
        if 1 <= n <= 10 ** 9 and 1 <= p <= 10**9:
         print(n*p)
         break
        else:
            print('Invalid values entered!')

main()
