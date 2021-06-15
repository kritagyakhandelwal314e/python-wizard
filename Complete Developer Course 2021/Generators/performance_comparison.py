from time import time
from array import array
limit = 10000000
def performance(func):
  def wrapper_func(*args, **kwargs):
    start_time = time()
    result = func(*args, **kwargs)
    end_time = time()
    print(f'took: {(end_time - start_time) * 1000} ms')
    return result
  return wrapper_func

@performance
def test_list(li):
  for i in li:
    i*5

@performance
def test_generator():
  for i in range(limit):
    i*5

@performance
def test_array(arr):
  for i in arr:
    i*5

li = [i for i in range(limit)]
arr = array('i', li)

test_array(arr)
test_generator()
test_list(li)


