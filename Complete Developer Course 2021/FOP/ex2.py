li = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({x for x in li if li.count(x) > 1})

print(duplicates)