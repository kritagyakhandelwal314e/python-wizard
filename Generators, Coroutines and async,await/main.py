from time import time

def performance(func):
  def wrapper(*args, **kwargs):
    start = time()
    result = func(*args, **kwargs)
    end = time()
    print(f'time took in {func.__name__}: {end - start}')
    return result
  return wrapper

class Counter:
  def __init__(self, limit = 1000000):
    self.count = 0
    self.limit = limit

  def __iter__(self):
    return self

  def __next__(self):
    if self.count == self.limit:
      raise StopIteration
    self.count += 1
    return self.count - 1

def counter(limit = 1000000):
  count = 0
  while count < limit:
    yield count
    count += 1

@performance
def fun1(limit):
  for i in Counter(limit):
    i*5

@performance
def fun2(limit):
  for i in counter(limit):
    i*5

fun1(10000000)
fun2(10000000)