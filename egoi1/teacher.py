# import math
#
#
# def max_pleasure(n, p):
#     # The number of students is ceil(n / 2)
#     students = math.ceil(n / 2)
#
#     # dp[i] will store the maximum pleasure possible by considering up to the i-th desk
#     dp = [0] * (n + 1)
#
#     # Base case: If there is only one desk, the only option is to place the student there
#     dp[0] = 0
#
#     # Fill the dp array
#     for i in range(1, n + 1):
#         # Option 1: Don't place a student at desk i, just take the value from previous desk
#         dp[i] = dp[i - 1]
#
#         # Option 2: Place a student at desk i, add the pleasure of desk i to the value from desk i-2
#         if i > 1:
#             dp[i] = max(dp[i], dp[i - 2] + p[i - 1])
#
#     # Now, find the maximum pleasure with exactly `students` desks occupied
#     return dp[n]
#
#
# # Example usage:
# n = int(input())  # Read number of desks
# p = list(map(int, input().split()))  # Read pleasure values
#
# # Output the result
# print(max_pleasure(n, p))

def one_two():
    numbers = []
    count = 0
    for i in range(1000, 10000):
        numbers.append(str(i))
    for num in numbers:
       if num.find('21')>-1 or num.find('12')>-1:
           count+=1
    return f"Overall there are {len(numbers)-count} numbers, where number one and two don't come together"
print(one_two())