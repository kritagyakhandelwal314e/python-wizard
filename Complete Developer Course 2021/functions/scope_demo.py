
a = 10

def confusion():
  a = 5
  return a


print(a) # 1
print(confusion()) # 5
print(a) # 1

# 1: start with local scope
# 2: parent 
# 3: Global
# 4: built in python functions


# global keyword

total = 2
def count():
  # global total
  # total += 1
  return total

print(count())
print(count())
print(count())

# nonlocal keyword

def outer():
  x = 'local'
  def inner():
    nonlocal x
    x = "nonlocal"
    print("inner: ", x)
  inner()
  print("outer:", x)
outer()


