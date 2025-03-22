def main():
    w = int(input('w:'))
    if 1<=w<=100:
          if w>2 and w%2 == 0:
              print('YES')
          else:
            print('NO')
    else:
        print('Over the limits')
main()
