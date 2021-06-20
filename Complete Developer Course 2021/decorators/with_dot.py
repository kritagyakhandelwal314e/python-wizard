class decClass():
  def __init__(self):
    print('all cool')

  def decorator_with_argument(num=2):
    def decorator(func):
      def wrapper_decorator(*args, **kwargs):
        for i in range(num):
          print('before')
          func(*args, **kwargs)
          print('after')
      return wrapper_decorator
    return decorator

@decClass.decorator_with_argument(num=1)
def hello():
  print('hello')


hello()