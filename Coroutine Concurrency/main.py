# The Lucas Sequence
def lucas():
  a = 2
  b = 1
  yield a
  while True:
    yield b
    a, b = b, a + b

from itertools import islice

print(list(islice(lucas(), 10)))

from time import time

def async_sleep(interval_seconds):
  '''
    async_sleep always yields atleast once
    async_sleep(0) yields exactly once
    Occurrences of bare yield can be replaced with yield from async_sleep(0)
  '''
  start = time()
  expiry = start + interval_seconds
  while True:
    yield # Ensure coroutines always yield
          # at least once if they can't 
          # complete immediately
    now = time()
    if now >= expiry:
      break
    '''
    yield # Subtle bug!
          # If interval_seconds is very small
          # the coroutine will never yield
          # and will hog the system
    '''

# A linear Search
def search(iterable, predicate):
  for item in iterable:
    if predicate(item):
      return item
  raise ValueError("Not Found")

print(search(lucas(), lambda x: len(str(x)) >= 6))

# A cooperative linear search
# returns generator object
def async_search(iterable, predicate):
  for item in iterable:
    if predicate(item):
      return item
    yield from async_sleep(0)
  raise ValueError("Not Found")

g = async_search(lucas(), lambda x: x > 10)
print(type(g)) # generator

# simulation of concurrency
next(g)
next(g)
print('some other task in the middle')
next(g)
next(g)
next(g)
# next(g)



from collections import deque
# Task
# Aggregate a coroutine and an integer id
class Task:
  next_id = 0
  def __init__(self, routine):
    self.id = Task.next_id
    Task.next_id += 1
    self.routine = routine

class Scheduler:
  def __init__(self):
    self.runnable_tasks = deque()
    self.completed_tasks_results = {}
    self.failed_tasks_errors = {}

  def add(self, routine):
    task = Task(routine)
    self.runnable_tasks.append(task)
    return task.id

  def run_to_completion(self):
    while len(self.runnable_tasks) != 0:
      task = self.runnable_tasks.popleft()
      # print(f"Running task {task.id} ... ", end='')
      try:
        yielded = next(task.routine)
      except StopIteration as stopped:
        print(f"Completed with result: {stopped.value}")
        self.completed_tasks_results[task.id] = stopped.value
      except Exception as e:
        print(f"Failed with exception: {e}")
        self.failed_tasks_errors[task.id] = e
      else:
        assert yielded is None
        # print("now yielded")
        self.runnable_tasks.append(task)

scheduler = Scheduler()
scheduler.add(async_search(lucas(), lambda x: len(str(x)) >= 3))
scheduler.add(async_search(lucas(), lambda x: x >= 10))
scheduler.run_to_completion()

from math import sqrt

# blocking function -> calling returns a bool
def is_prime(x):
  if x < 2:
    return False
  for i in range(2, int(sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

# non-blocking function -> calling returns a generator object
def async_is_prime(x):
  if x < 2:
    return False
  for i in range(2, int(sqrt(x)) + 1):
    if x % i == 0:
      return False
    yield from async_sleep(0)
  return True

print(is_prime(2))
print(is_prime(97))
print(is_prime(1000000007))
print(is_prime(1000000008))

def async_print_matches(iterable, predicate):
  for item in iterable:
    if predicate(item):
      print("Found :", item, end=", ")
    yield from async_sleep(0)

def async_print_matches_with_async_predicate(iterable, predicate):
  for item in iterable:
    matches = yield from predicate(item)
    if matches:
      print("Found :", item)


# scheduler.add(async_print_matches(lucas(), is_prime))
# scheduler.run_to_completion()

# print a message at intervals

def repetitive_message(message, interval_seconds):
  while True:
    print(message)
    start = time()
    expiry = start + interval_seconds
    while True:
      now = time()
      if now >= expiry:
        break

def async_repetitive_message(message, interval_seconds):
  while True:
    print(str(time()) + ': ' + message)
    yield from async_sleep(interval_seconds)

scheduler = Scheduler()
scheduler.add(async_repetitive_message("Unattended baggage will be distroyed", 2.5))
scheduler.add(async_print_matches_with_async_predicate(lucas(), async_is_prime))
scheduler.run_to_completion()