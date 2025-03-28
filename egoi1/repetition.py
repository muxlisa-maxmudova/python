# from collections import Counter
# #dna = ['a', 't', 't', 'c', 'g', 'g', 'g', 'a']
# #a = (dict(Counter(dna)))
# #values = list(a.values())
# def maximum():
#     dna = input('DNA: ')
#     a = (dict(Counter(list(dna))))
#     values = list(a.values())
#     big = values[0]
#     for i in values:
#        if i > big:
#           big = i
#     print(big)
# maximum()
def maximum():
    dna = input("DNA: ")
    max_len = 0
    current_len = 1

    for i in range(1, len(dna)):
        if dna[i] == dna[i - 1]:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1  # Reset count for new character

    max_len = max(max_len, current_len)  # Ensure the last sequence is considered
    print(max_len)


maximum()
