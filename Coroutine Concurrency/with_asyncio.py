'''
Mechanically refactor our coop code
to asyncio code:

1. def async_foo  --> async def foo

2. import asyncio

3. async_sleep(x) --> asyncio.sleep(x)

4. remove async_sleep(x) --> (X)

5. yield from foo --> await foo

'''

import asyncio

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


# A cooperative linear search
# returns generator object
async def search(iterable, predicate):
  for item in iterable:
    res = await predicate(item)
    if res:
      return item
    await asyncio.sleep(0)
  raise ValueError("Not Found")


from math import sqrt

# non-blocking function -> calling returns a generator object
async def is_prime(x):
  if x < 2:
    return False
  for i in range(2, int(sqrt(x)) + 1):
    if x % i == 0:
      return False
    await asyncio.sleep(0)
  return True


async def print_matches(iterable, predicate):
  for item in iterable:
    matches = await predicate(item)
    if matches:
      print("Found :", item)
    await asyncio.sleep(0)

# print a message at intervals
async def repetitive_message(message, interval_seconds):
  while True:
    print(str(time()) + ': ' + message)
    await asyncio.sleep(interval_seconds)

# scheduler = asyncio.get_event_loop()
# scheduler.create_task(repetitive_message("Unattended baggage will be destroyed", 2.5))
# scheduler.create_task(print_matches(lucas(), is_prime))
# scheduler.run_forever()

async def thirteen_digit_prime(x):
  return (await is_prime(x)) and len(str(x)) == 13

async def monitored_search(iterable, predicate, future):
  try:
    found_item = await search(iterable, predicate)
  except ValueError as not_found:
    future.set_exception(not_found)
  else: # no exception
    future.set_result(found_item)

async def monitor_future(future, interval_seconds):
  while not future.done():
    print('Waiting...')
    await asyncio.sleep(interval_seconds)
  print("Done!")

loop = asyncio.get_event_loop()
future = loop.create_future()
co_obj = monitored_search(lucas(), thirteen_digit_prime, future)
loop.create_task(co_obj)
loop.create_task(monitor_future(future, 1.0))
loop.run_until_complete(future)
print(future.result())
loop.close()