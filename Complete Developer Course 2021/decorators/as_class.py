import functools

class DecoratorClass():
  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwargs):
    print('before')
    self.func(*args, **kwargs)
    print('after')

@DecoratorClass
def hello():
  print("hello")

hello()