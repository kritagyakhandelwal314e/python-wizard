# lambda expressions
'''
used if only only to be used once
do not store it on the machine
'''
from functools import reduce
li = [1, 2, 3, 4, 5]
print(list(map(lambda item: item * 2, li)))
print(list(filter(lambda item: item % 2 == 0, li)))
print(reduce(lambda acc, item: acc + item, li))
