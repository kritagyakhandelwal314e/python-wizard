from time import time
def performance(func):
  def wrapper_func(*args, **kwargs):
    start_time = time()
    result = func(*args, **kwargs)
    end_time = time()
    print(f'took: {(end_time - start_time) * 1000} ms')
    return result
  return wrapper_func

class FibonacciGen():
  def __init__(self, n):
    self.prev = 0
    self.current = 1
    self.n = n
    self.till_now = 1

  def __iter__(self):
    return self

  def __next__(self):
    if self.till_now <= self.n:
      self.till_now += 1
      temp = self.prev + self.current
      self.prev = self.current
      self.current = temp
      return self.prev
    raise StopIteration

def fib(number):
  a = 0
  b = 1
  for i in range(number):
    yield a
    temp = a
    a = b
    b = temp + b

@performance
def testFibonacciGen():
  fibo = FibonacciGen(10)
  for i in fibo:
    print(i)

@performance
def testfib():
  fibo = fib(20)
  for i in fibo:
    print(i)

testFibonacciGen()
testfib()

