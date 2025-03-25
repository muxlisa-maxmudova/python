def main():
    history=[]
    while True:
        action = input('Action: ') # in js we use prompt
        if action == 'Undo':
          undone =  history.pop() # removes last element on the list
          print(f'Undone:{undone}')
        elif action == 'Restart':
           history.clear()
        else:
            history.append(action) # in js we use push method
        print(history)

main()
