# Decorator

def my_decorator(func):
  def wrap_func():
    print('****************')
    func()
    print('****************')
  return wrap_func

@my_decorator
def hello():
  print('hello')


hello()

# similarly
def bye():
  print('see ya later')
my_decorator(bye)()

