# if = Do some code only IF some cond is true
# in the other case do smth else
#
# age = int(input('Enter your age: '))
# if age>=100:
#     print('You are too old to sign up')
# elif  age >= 18 :
#     print('You are now signed up')
# elif age < 0:
#      print('You have not been born yet!')
# elif age<18:
#     print('You must be 18+ to sign up!')
#
# response = input('Would you like food? (Y/N): ')
# if response == 'Y':
#     print('Have some food')
# else:
#     print('no food for you')

# name = input('Enter your name: ')
# if name == "":
#     print('You did not type in your name')
# else:
#     print(f'Hello, {name}')
# for_sale = True
# if for_sale:
#     print('This item is for sale')
# else:
#     print('This item is not for sale!')

def main():
   difficulty = input('Difficult or casual?: ')
   if not (difficulty == 'Difficult' or difficulty == 'Casual'):
       print('Enter a valid difficulty')
       return
   players = input('Multiplayer or Single-player?: ')
   if not (players == 'Multiplayer' or difficulty == 'Single-player'):
       print('Enter valid number of players')
       return
   if difficulty == 'Difficult' and players == 'Multiplayer':
           print('Poker')
   elif difficulty == 'Difficult' and players == 'Single-player':
           print('Klondike')
   elif difficulty == 'Casual'  and  players == 'Multiplayer':
           print('Hearts')
   else:
       print('Clock')
main()