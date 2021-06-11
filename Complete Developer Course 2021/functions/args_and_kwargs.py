def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args) + sum(item for item in kwargs.values())

print(super_func(1, 2, 3, 4, 5, num1=5, num2=12))

## Rule: params, *args, default parameters, **kwargs