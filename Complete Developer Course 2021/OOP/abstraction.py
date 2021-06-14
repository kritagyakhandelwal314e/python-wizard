class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def speak(self):
    print(f'my name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('kritagya', 22)
print(player1.name)
print(player1.age)

player1.speak() # abstraction