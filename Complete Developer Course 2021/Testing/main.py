def do_stuff(num):
  try:
    if num or num == 0:
      return int(num) + 5
    else:
      return 'provide arg'
  except ValueError as err:
    return err