def main():
    total = 0
    while total < 50:
        (input(f'Amount Due:{50-total}'))
        coin_inserted = int(input('Insert coin: '))
        if coin_inserted == 5 or coin_inserted == 10 or coin_inserted == 25:
            total+=coin_inserted
        else:
            total+=0
    print(f'Total is: {total}')
    if total == 50:
        input('Amount Due: 0')
    elif total>50:
        input(f'Change owed: {total-50}')

main()