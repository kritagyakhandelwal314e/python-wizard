i = 0
while i < 50:
    i += 1
    print(i, end=' ')
else:
    print()
    print('All work is done', end=' ')
print()

while True:
    response = input('say somthing: ')
    if response == 'bye':
        break