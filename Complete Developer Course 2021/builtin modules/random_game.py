import sys
import random

args = sys.argv
start = args[1]
end = args[2]
try:
  start = int(start)
  end = int(end)
except:
  print('arguments should be int please provide valid arguments')
  exit()

print(f'guess a number between {start} and {end}: ')
while True:
  num = random.randint(start, end)
  try:
    guessed_num = int(input())
    if num == guessed_num:
      print('Hoorray, you guessed it right')
      break
    else:
      print('oops, guess again: ')
  except (TypeError, ValueError):
    print('please guess an INTEGER')
  except:
    print('Unexpected error occured')

