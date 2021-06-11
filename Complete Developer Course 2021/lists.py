# List
# ordered sequece of object

# li = [1, 2, 3, 4, 5]
# li2 = ['a', 'b', 'c']
# li3 = [1, 2, 'a', True, 'kritagya', [1, 2, 3]] # mixed typed data
# for ele in li3:
#     print(f'{ele} is of tyle: {type(ele)}')

# # list slicing
# print(li3[4])
# print(li3[:])
# print(li3[::-1])

# # lists are mutable
# li3[2] = 'replaced element'
# print(li3[:])

# # list gotcha
# print("List Gotcha")
# # assignment copy
# print("\nAssignment copy")
# copyList = li3  # copylist would just point to the same memory block
# print(li3)
# print(copyList)
# copyList[0] = 'item replaced in copy list'
# print(li3)
# print(copyList)

# #shallow copy
# print("\nShallow copy")
# shallowcopy = li3[:] # copylist2 would make shallow copy of original li3
# print(li3)
# print(shallowcopy)
# shallowcopy[1] = 'item replaced in copy list 2'
# print(li3)
# print(shallowcopy)
# # BUT
# shallowcopy[-1].append(4)
# print(li3)
# print(shallowcopy)

# # deep copy
# print("\nDeep copy")
# import copy
# deepcopyli3 = copy.deepcopy(li3)
# print(li3)
# print(deepcopyli3)
# deepcopyli3[-1].append('appended in deepcopy')
# print(li3)
# print(deepcopyli3)

# List Methods

#adding
basket = [1, 2, 3, 4, 5]
print(len(basket))
basket.append(6)
print(basket)
basket.insert(4, 100)
print(basket)
basket.extend([1001, 1002])
print(basket)

# removing
popped = basket.pop()
print("popped: ", popped)
print(basket)
popped = basket.pop(1)
print("popped: ", popped)
print(basket)
removed = basket.remove(1001)
print("removed: ", removed) # None
print(basket)
#basket.remove(100234) # throws error 100234 is not in list
index = basket.index(6) # serching the velue and provide the index of that element
print(index)
freq = basket.count(4)
print(freq)
basket.append(4)
freq = basket.count(4)
print(freq)
print(basket)
basket.reverse()
print(basket)
# sorted_basket = sorted(basket)
# print(sorted_basket)
print(basket)
basket.sort()
print(basket)
basket.clear()

# other functionalities
basket = [1, 2, 3, 4, 5]
ispresent = 5 in basket
print(ispresent)

rl = list(range(100))
print(rl)

words = ['Hi,', 'I', 'am', 'kritagya']
delimeter = ' '
sentance = delimeter.join(words)
print(sentance)

# List Unpacking
print("\nList Unpacking")
[a, b, c, *other, d] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)

#