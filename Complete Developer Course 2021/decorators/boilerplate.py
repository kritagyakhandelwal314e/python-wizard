import functools

def decorator(func):
  @functools.wraps(func)
  def wrapper_decorator(*args, **kwargs):
    # De something before
    result = func(*args, **kwargs)
    # Do something after
    return result
  return wrapper_decorator

