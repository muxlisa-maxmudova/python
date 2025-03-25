# i = 0
# while i < 3:
#     print('meow')
#     i+=1 # 'i' will eventually reach 3
def main():
        moisture = float(input('Level: '))
        days = 0
        print(f'Day {days}: Moisture is {moisture}%')
        while moisture > 20:
            moisture = float(input('Level: '))
            days+=1
            print(f'Day {days}: Moisture is {moisture}%')
        print('Time to water!')
main()


