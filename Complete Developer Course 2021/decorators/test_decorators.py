import time
import functools

def run_time(func):
  @functools.wraps(func) #for printing doc of func
  def wrapper(*args, **kwargs):
    '''
    This is a wrapper function
    '''
    t1 = time.time()
    result: str = func(*args, **kwargs)
    t2 = time.time()
    print(f"time took: {t2 - t1} ms")
    return result
  return wrapper

@run_time
def func1(a: str, b: int):
  '''
  This is func1 function
  '''
  print(f"{b} times {a} is {a*b}")
  return a*b

result = func1('kritagya', 5)
print(result)
print(func1.__doc__)