class PlayerCharacter:
  def __init__(self, name, age):
    self._name = name # private attributes convention
    self._age = age

  def speak(self):
    print(f'my name is {self._name}, and I am {self._age} years old')

player1 = PlayerCharacter('kritagya', 22)
print(player1._name)
print(player1._age)

player1.speak() # abstraction

player1._name = '!!!!!!'
player1.speak = 'BOOOO'

print(player1._name)
print(player1.speak)