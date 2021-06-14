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