# Decorator Pattern

def my_decorator(func):
  def wrap_func(*args, **kwargs):
    # before execution modifications
    print('****************')
    func(*args, **kwargs)
    # after execution modifications
    print('****************')
  return wrap_func

@my_decorator
def hello(greeting, emoji):
  print(greeting, emoji)


hello('Good Morning', ';p')
# my_decorator(hello)('Good Morning')


