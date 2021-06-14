'''
Usefule Functions:
- map()
- filter()
- zip()
- reduce()
'''
from functools import reduce
def mul2(item):
  return item * 2

def is_even(item):
  return item % 2 == 0

def sum(acc, item):
  return acc + item

li = [1, 2, 3, 4, 5]
li2 = [6, 7, 8, 9, 10]
li3 = [11, 12, 13, 14, 15]
print(list(map(mul2, li))) # map
print(list(filter(is_even, li))) # filter
print(list(zip(li, li2, li3))) # zip
print(reduce(sum, li, )) # reduce (cool stuff)