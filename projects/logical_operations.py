# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one cond must be True |
#                     and = both conditions must be True &
#                     not = inverts the condition (not False, not True)
# temp = 20
# is_raining = True
# if temp > 35 or is_raining or temp<0:
#     print(f'The outdoor event is cancelled!')
# else:
#     print('The outdoor event is still scheduled')
#
# temp = 0
# is_sunny = False
# if temp >=28 and is_sunny:
#     print('It is hot outside')
#     print('It is sunny')
# elif temp <=0 and is_sunny:
#     print('It is cold')
#     print('Though it is sunny')
# elif 28>temp>0 and is_sunny:
#     print('It is warm outside')
#     print('Still sunny')
# elif temp <=0 and not is_sunny:
#     print('It is cold and dull today(')
# total = 0
# for i in range(1000):
#     if str(i).find('3')>-1 and str(i).find('5')>-1:
#         print(i)
#         total+=1
# print(total)
def palindromes():
  count = []
  for i in range(1001):
       if str(i)==str(i)[::-1] and str(i).find('3')>-1:
          count.append(i)
  print(max(count))
palindromes()

