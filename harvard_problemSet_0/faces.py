text = input('Type smth: ')
def smiles():
    if text.find(':)'and':(')>-1:
        return text.replace(':)', '😊').replace(':(', '🙁')
    else:
        return text
print(smiles())