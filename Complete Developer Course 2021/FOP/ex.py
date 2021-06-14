# squaring
li = [5, 4, 3]
print(list(map(lambda item: item*item, li)))

# sorting
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key = lambda item: item[1])
print(a)
a.sort()
