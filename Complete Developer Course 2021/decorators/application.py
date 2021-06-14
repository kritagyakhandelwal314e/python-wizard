from time import time

def performance(func):
  def wrapper(*args, **kwargs):
    start_time = time()
    result = func(*args, **kwargs)
    end_time = time()
    print(f'time took: {(end_time - start_time) * 1000} ms')
    return result
  return wrapper


@performance
def long_time():
  for i in range(10000):
    i*5

long_time()
