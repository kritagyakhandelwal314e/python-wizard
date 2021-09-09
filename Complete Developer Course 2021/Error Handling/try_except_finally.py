def func1():
  try:
    print("execute toh hua")
    return 2
    print("execute yhaan bhi hua hua")
  finally:
    # return 3
    print("something")

def func2():
  try:
    return 1
    raise ValueError()
  except ValueError as e:
    print("execute toh hua")
    # return 2
    print("execute yhaan bhi hua hua")
  finally:
    # return 3
    print("something")

func1()

func2()
