try:
  with open('test.txt', mode='r') as my_file:
    print(my_file.read())
except FileNotFoundError as err:
  print('file does not exist')
except IOError as err:
  print('IO  Error')
except:
  print('Unexpected Error occured')
