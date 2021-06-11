username = 'coder'
password = 'secret'
long_string = '''
WOW
0 0
---
'''
print(long_string)
print(type(long_string)) # str

first_name = 'kritagya'
last_name = 'khandelwal'
full_name = first_name + ' ' + last_name # string concatenation
print(full_name)

# print('Hello' + 5) will throw error

# type conversion
num = 100
print(num)
print(type(num)) 
num = str(num)
print(num)
print(type(num))

# Escape Sequence
weather = "It's \"kind of\" \t summy \nisn't it?"
print(weather)

# \ , \t ,  \n

# formatted strings
name = 'kritagya'
age = 22

print(f'Hi this is {name}, I am {age} years old') # introduced in python 3
print('Hi this is {}, I am {} years old'.format(name, age))
print('Hi this is {1}, I am {0} years old'.format(name, age))
print('Hi this is {name}, I am {age} years old'.format(name='yash', age=22))

# indexing
# string    k   r   i   t   a   g   y   a
# indexing  0   1   2   3   4   5   6   7
# reverse I -8  -7  -6  -5  -4  -3  -2  -1 
print(name[0]) # k
print(name[4]) # a
# reverse indexing 
print(name[-1]) # a
print(name[-3]) # g
# intervals and steps : slicing
# [start : stop : steps]
print(name[0:4]) # krit
print(name[4:7]) # agy
print(name[:5]) # krita
print(name[1::2]) # rtga
print(name[::2]) # kiay
print(name[-1::-1]) # aygatirk -- reversing the string
print(name[::-1]) # aygatirk -- reversing the string

# immutability
''' name[2] = '0' # throws error -- we cannot reassign to part of a string
                # all we can do is add more or assign new
print(name)
'''

# inbuilt functions

print(f'length of name is {len(name)}')

# string methods

#format
print('Hi this is {}, I am {} years old'.format(name, age))
print('Hi this is {1}, I am {0} years old'.format(name, age))
print('Hi this is {name}, I am {age} years old'.format(name='yash', age=22))

print(name.upper()) # KRITAGYA
print(name.capitalize()) # Kritagya
print(full_name.find('tag')) # 3 -- the index where it started
print(full_name.find('not')) # -1 -- doesnot exist
print(full_name.replace(' ', '_')) # kritagya_khandelwal

