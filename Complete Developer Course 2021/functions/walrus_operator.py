# walrus operator( := )

a = 'hellooooooooo'
if (n := len(a)) > 10:
    print(f'too long {n} length')

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]

print(a)