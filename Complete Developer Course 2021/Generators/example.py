

def generator_function(num):
  for i in range(num):
    yield i*2

li = [item for item in generator_function(10)]
print(li)

g = generator_function(100)

print(g)
print(next(g))
print(next(g))