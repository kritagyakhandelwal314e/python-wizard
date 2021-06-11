# Fundamental Datatypes

# int and float
print(type(2)) # int
print(type(2.0)) # float
print(type(2+2.0)) # float
print(type(2+2)) # int
print(type(2/2)) # float
print(type(2*2.0)) # float
print(type(2**2)) # int
print(type(2**2.0)) # float
print(type(9%2)) # int

# complex
# only used with very very complicated maths

# math functions
print(round(2.2)) # 2
print(round(2.6)) # 3
print(type(round(2.3))) # int

# operator precedence
print(20 + 3 *  4) # 20 + 3 * 4 -> 20 + 12 -> 32
print(20 / 10 * 5)
# order of execution
# ()
# **
# * ,  /
# + , -

# binary representation
print(bin(5))
print(int('101', 2))
print(int('0b101', 2))


# str (string)

print('hi hello there')
print(type('hi hello there')) # str


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

# booleans: bool
name = "Kritagya"
is_cool = False
is_cool = True

print(bool(0)) # False
print(bool(123)) # True
print(bool(-23423)) # True
print(bool(1)) # True

# List
# ordered sequece of object

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True, 'kritagya', [1, 2, 3]] # mixed typed data
for ele in li3:
    print(f'{ele} is of tyle: {type(ele)}')

# list slicing
print(li3[4])
print(li3[:])
print(li3[::-1])

# lists are mutable
li3[2] = 'replaced element'
print(li3[:])

# list gotcha
print("List Gotcha")
# assignment copy
print("\nAssignment copy")
copyList = li3  # copylist would just point to the same memory block
print(li3)
print(copyList)
copyList[0] = 'item replaced in copy list'
print(li3)
print(copyList)

#shallow copy
print("\nShallow copy")
shallowcopy = li3[:] # copylist2 would make shallow copy of original li3
print(li3)
print(shallowcopy)
shallowcopy[1] = 'item replaced in copy list 2'
print(li3)
print(shallowcopy)
# BUT
shallowcopy[-1].append(4)
print(li3)
print(shallowcopy)

# testing list.copy
print("\nusing list.copy (shallow copy)")
import copy
using_copy = li3.copy()
print(li3)
print(using_copy)
using_copy[1] = 4
using_copy[-1].append('appended in deepcopy')
print(li3)
print(using_copy)

# deep copy
print("\nDeep copy")
import copy
deepcopyli3 = copy.deepcopy(li3)
print(li3)
print(deepcopyli3)
deepcopyli3[-1].append('appended in deepcopy')
print(li3)
print(deepcopyli3)

# None Datatype
print("\nNone Datatype")
weapons = None
print(weapons)

# Dictionary
print("\nDictionary")
# dict
d = {
    'a': [1, 2, 3],
    'b': 'kritagya',
    'x': True
}
print(type(d))
print(d)
print(d['a'])

# hybrid
my_list = [{
        'name': 'kritagya',
        'roll': '17145',
        'year': '2021'
    }, {
        'name': 'yash',
        'roll': '54171',
        'year': '1202'
    }
]
print(type(my_list))
print(my_list)
print(my_list[0]['name'])

# key duplicationn
d = {
    'a': [1, 2, 3],
    'b': 'kritagya',
    'x': True,
    'b': 'yash'
}
print(d['b']) # key value override

print(d.get('a'))
print(d.get('c'))
print(d.get('c', 'default value if not a key'))

#another way to create dictionary
user = dict(
    name='kritagya',
    roll=17145
)
print(user)
print('name' in user)
print('kritagya' in user)
print('kritagya' in user.values()) # True
print(user.items())

user['dob'] = 1998
print(user)

# tuple
# -- immutable
# -- usually faster than list
t = (1, 2, 3, 4, 5)
print(type(t))
print(t)
print(t[0])
print(5 in t)
print(t.count(5))
print(t.index(5))

# tuple can be a key in dictionary
user[(1, 2, 3, 4)] = [1, 2, 3, 4]
print(user)
nt = t[1:4]
print(nt)
print(t)
x, y, z, *other = t
print(x)
print(y)
print(z)
print(other)

# set
# unordered collections of unique objects
s = {1, 2, 3, 4, 5, 6, 7, 7}
print(s)
s.add(100)
s.add(2)
print(s)
sl = set([34, 45, 3213, 345])
print(sl)

# print(s[0]) # throughs error
print(1 in s)
print(34 in s)
print(list(s))
# s.add([1, 2, 3]) # throughs error
ns = s.copy()
ns.add(199)
ns = ns.union({45, 46, 47})
print(s)
print(ns)
print(s & ns)
ns.discard(45)
print(ns.difference(s))
print(ns.intersection(s))
print(ns.isdisjoint(s))
print(ns.issubset(s))
print(ns.issuperset(s))
ns.difference_update(s)
print(ns)
print(s | ns) # union



# misc.
# print([1, 2, 3, 4].__str__())





