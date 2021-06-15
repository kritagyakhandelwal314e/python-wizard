# debugging
# - practice
# - linting
# - ide/editor
# - read errors
# - pdb: built in module in python
import pdb

def add(num1, num2):
  pdb.set_trace()
  return num1 + num2

add(4, 7)