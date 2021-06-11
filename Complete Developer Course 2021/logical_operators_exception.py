print(True == 1)
print(True == 123)
print(False == 0)
print([] == 1)
print(10 == 10.0)
print(.1+.1+.1 == .3)
print([1, 2, 3] == [1, 2, 3])


# checks if both points to same ?
print(True is 1)
print(True is 123)
print(False is 0)
print([] is 1)
print(10 is 10.0)
print(.1+.1+.1 is .3)
print([1, 2, 3] is [1, 2, 3])

# true case
l = [1, 2, 3, 4]
d = l
print(l is d)