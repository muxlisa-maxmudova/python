string = input('Input: ')
def main(word):
    for letter in word:
        if letter=='a' or letter=='e'or letter=='i'or letter=='u' or letter=='o':
          word = word.replace(letter,'')
    return word
print(main(string))