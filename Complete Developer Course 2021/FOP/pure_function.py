# PURE FUNCTION
'''
pure functions
2 rules:
- with same input it should always return same output
- function should not produce any side effects
  - printing
  - reassigning a variable

'''

def mul2(li):
  return [item * 2 for item in li]

print(mul2([1, 2, 3]))