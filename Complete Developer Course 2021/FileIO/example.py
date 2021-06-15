my_file = open('test.txt')

# READ OPs

print('------------------------------------')
print(my_file.read())
print('------------------------------------')
print(my_file.read())
print('------------------------------------')
print(my_file.read())
print('------------------------------------')
my_file.seek(0)
print(my_file.read())
print('------------------------------------')

my_file.seek(0)

print(my_file.readline())

my_file.seek(0)
print(my_file.readlines())

my_file.close()

# READ WRITE APPEND OPs
# READ
print()
print('#########################################')
print('READ: ')
print()
with open('test.txt') as my_file:
  print(my_file.readlines())


# READ & WRITE
print()
print('#########################################')
print('READ & WRITE: ')
print()
with open('test.txt', mode='r+') as my_file:
  text = my_file.write('hey it\s  me')
  print(text)

# APPEND
print()
print('#########################################')
print('APPEND: ')
print()
with open('test.txt', mode='a') as my_file:
  text = my_file.write('hey it\s  me')
  print(text)

# WRITE
print()
print('#########################################')
print('WRITE: ')
print()
with open('test.txt', mode='w') as my_file:
  text = my_file.write('hey it\s  me')
  print(text)


