
while True:
  try:
    age = int(input('what is your age? '))
    print(10/age)
    # raise ValueError('hey cut it out')
  except ValueError as err:
    print(f'please enter a number: {err}')
  except ZeroDivisionError as err:
    print(f'please enter age higher than 0: {err}')
  else:
    print('Thank You')
    break
  finally:
    print("doesn't matter what happened")