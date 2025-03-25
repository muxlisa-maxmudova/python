# string = []
# def main():
#     add = input('CamelCase: ')
#     for let in add:
#         if let.isupper():
#           string.append(add[0:add.index(let)])
#           string.append(add[add.index(let):].lower())
#     snake_case = '_'.join(string)
#     print(snake_case)
# main()
def main():
    add = input("CamelCase: ")
    snake_case = []  # Use a list for efficiency

    for i, let in enumerate(add):
        if let.isupper() and i != 0:  # Avoid adding "_" at the start
            snake_case.append("_")
        snake_case.append(let.lower())  # Convert to lowercase and append

    print("".join(snake_case))  # Join list elements into a string

main()

