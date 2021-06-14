from time import time
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
  for i in range(1000000):
    i*5

li = [i for i in range(1000000)]

test_list(li)
test_generator()


