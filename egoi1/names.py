def main():
    length = int(input(''))
    letters = list(input(''))
    print(letters)
    i = 0
    max_beauty = -1
    best_name = ""
    while i < length:
        name = input('')
        names = list(name)
        i+=1
        beauty_score = sum(1 for letter in name if letter in letters)
        if beauty_score > max_beauty:
            best_name = name
            max_beauty = beauty_score
    print(best_name)
main()