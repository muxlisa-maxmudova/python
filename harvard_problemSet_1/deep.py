def main():
    answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything?: ')
    if answer.find('42' or 'forty-two' or 'forty two'):
        print('Yes')
    else:
        print('No')
main()