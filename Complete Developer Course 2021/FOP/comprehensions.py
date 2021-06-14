# list, set, dictionary

# list comprehensions
li = [ch for ch in 'hello']
li2 = [num for num in range(10)]
li3 = [num*2 for num in range(10)]
li4 = [num**2 for num in range(10) if num % 2 == 0]

print(li)
print(li2)
print(li3)
print(li4)

# set comprehensions
s = {ch for ch in 'hello'}
s2 = {num for num in range(10)}
s3 = {num*2 for num in range(10)}
s4 = {num**2 for num in range(10) if num % 2 == 0}

print(s)
print(s2)
print(s3)
print(s4)

# dict comprehensions
simple_dict = {
  'a': 1,
  'b': 2
}
d = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}
d2 = {item: item**2 for item in li2}
print(d)
print(d2)