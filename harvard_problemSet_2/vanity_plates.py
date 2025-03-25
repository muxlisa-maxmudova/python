def main():
    plate = input("Plate: ")
    if (plate[0:2].isalpha() and
            2<len(plate)<=6 and
            plate[-2:].isdigit() and
            plate[-2]!='0'):
        print("Valid")
    elif plate.find(' 'or '.' or ','):
        print("Invalid")
main()