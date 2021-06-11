for item in 'lol kol jol hol gol fol':
    print(item, end=' ')
print()

for item in [1, 2, 3, 4, 5, 6]:
    print(item, end=' ')
print()

for item in (1, 2, 3, 4, 5, 6):
    print(item, end=' ')
print()

for item in {1, 2, 3, 4, 5, 6}:
    print(item, end=' ')
print()

user = {
    'name': 'kritagya',
    'roll': 17145,
    'can_swim': False
}
for item in user:
    print(item)

for item in user.values():
    print(item)

for item in user.items():
    print(item)

for key, value in user.items():
    print(key, value, sep='\t')

my_list = [1123,2435,345,345,6346,745,74567,436]
sum = 0
for i in my_list:
    sum += i
print(sum)

sum = 0
for i in range(len(my_list)):
    sum += my_list[i]
print(sum)

# range

print(list(range(10)))
print(list(range(4, 10)))
print(list(range(4, 20, 2)))
print(list(range(20, 4, -2)))

# enumerate

for i, c in enumerate('Hello Kritagya'):
    print(i, c)

for i, value in enumerate([1, 2, 3, 4]):
    print(1, value)

for i, value in enumerate((1, 2, 3, 4)):
    print(1, value)



