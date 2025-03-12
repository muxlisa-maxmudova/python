text = input('Type smth: ')
def smiles():
    if text.find(':)')>-1:
        return text.replace(':)', '😊').replace(':(', '🙁')
    else:
        return text
print(smiles())