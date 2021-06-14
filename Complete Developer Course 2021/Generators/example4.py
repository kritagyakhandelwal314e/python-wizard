class MyGen():
  current = 0
  def __init__(self, first, last):
    self.current = first
    self.last = last
  
  def __iter__(self):
    return self

  def __next__(self):
    if self.current < self.last:
      num = self.current
      self.current += 1
      return num
    raise StopIteration

gen = MyGen(0, 10)
for i in gen:
  print(i)