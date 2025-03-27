#n = int(input('n: '))
def main(number):
    if 1 <= number <= 10**6:
        while number != 1:
            print(number, end=' ')
            if number%2 == 0:
                number //=2
            else:
                number = number*3+1

        print(1)
#main(n)

def main_two():
    n = int(input())
    if 1<=n<=10**6:
        while n != 1: # it will loop through numbers till n is not 1
            print(n, end=' ')   # in while lop we print the format first
            if n%3 == 0:
                n//=3
            elif n%2 == 0:
                n//=2
            else:
               n = n-1
        print(1)
main_two()



