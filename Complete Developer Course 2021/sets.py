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
