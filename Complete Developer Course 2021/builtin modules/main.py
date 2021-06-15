import random

freq = [0]*100
print(freq)
for i in range(1000000):
  freq[random.randint(0, 99)] += 1

print(freq)

print(sys)

