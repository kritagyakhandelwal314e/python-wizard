# demonstration of state management by decorators
# decorators manages states of different functions differently
def history(func):
  return_values = set()
  def wrapper(*args, **kwargs):
    return_value = func(*args, **kwargs)
    return_values.add(return_value)
    print(f'Return Values: {str(sorted(return_values))}')
    return return_value
  return wrapper

@history
def foo(x):
  return x + 2

@history
def bar(x):
  return x - 2

print(foo(2))
print(foo(4))
print(bar(2))
print(foo(2))
print(foo(25))
print(bar(4))
print(bar(2))
print(bar(25))