from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

li = [1, 2, 3, 4, 5, 6, 7, 7]
sentance = 'hi there, this is kritagya khandelwal, I am very cool'

print(Counter(li))
print(Counter(sentance))

dictionary = defaultdict(lambda : 'doesnot exist', {
  'a': 1,
  'b': 2
})

print(int())
print(dictionary['a'])
print(dictionary['c'])

d = {}
d['a'] = 1
d['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(d == d2)

# but
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d == d2)

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d == d2)


print(datetime.time(15, 30, 25))

arr = array('i', [1, 2, 3])
print(arr)