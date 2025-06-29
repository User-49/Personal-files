while True:
  a = input('enter file adress: ')
  try:
    f = open(a,'r', encoding = 'UTF-8')
  except FileNotFoundError:
    print("invalid adress, try again\n",'='*61)
    continue
  while True:
    print('\nplease select the required info-\n')
    print('1. number of words')
    print('2. number of letters')
    print('3. number of lines')
    print('4. open another file')
    print('5. exit the program')
    try:
      choice = int(input('\nenter choice: '))   
    except ValueError:
      print('choice to be written in numbers')
      print('='*61)
      continue
    if choice == 1:
      f.seek(0)
      x = f.read()
      l = x.split()
      print('\nnumber of words: ', len(l))
      k = input()
    elif choice == 2:
      f.seek(0)
      x = f.read()
      n = 0
      for i in x:
        if i.isalpha():
          n += 1
      print('\nnumber of letters: ', n)
      k = input()
    elif choice == 3:
      f.seek(0)
      print('\nnumber of lines: ', len(f.readlines()))
      k = input()
    elif choice == 4:
      print('='*61)
      break
    elif choice == 5:
      print('program has been closed\n','*'*61)
      exit()
    else:
      print("invalid choice,try again")
    print('-'*61)
  f.close()
