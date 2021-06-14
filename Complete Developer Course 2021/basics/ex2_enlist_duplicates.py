some_list = ['a', 'b', 'c', 'd', 'e', 'a', 'e', 'd', 'f', 'g', 'b']
dup_list = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in dup_list:
            dup_list.append(item)
print(dup_list)