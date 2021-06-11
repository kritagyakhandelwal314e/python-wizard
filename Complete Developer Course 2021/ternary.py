num = int(input())

# (num > 100 ? print("greater") : (num < 100 ? print("lesser") : print("equal")))


(print("greater") if num > 100 else (print("lesser") if num < 100 else print("equal")))