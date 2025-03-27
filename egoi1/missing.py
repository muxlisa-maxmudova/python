# this below is mine it works for only 1-9 numbers
new =[]
actually =[]
def find():
    count = int(input(''))
    show = list(map(int, input().split())) # worked
    for number in show:
        number = int(number)
        new.append(number)
    for i in range(count+1):
       if i != 0:
           actually.append(i)
    print(*(set(actually)-set(new)))
find()
# this is with specific formula:
# def find():
#     n = int(input())  # Read n
#     numbers = list(map(int, input().split()))  # Read the n-1 numbers
#
#     expected_sum = n * (n + 1) // 2  # Sum of first n numbers (Gauss formula)
#     actual_sum = sum(numbers)  # Sum of given numbers
#
#     missing_number = expected_sum - actual_sum  # Find missing number
#     print(missing_number)
#
#
# find()
