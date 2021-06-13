# OOP

class PlayerCharacter:
  membership = True # Class Attribute
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def shout(self):
    print(f'my name is {self.name}')

  def return_self(self):
    return self

  @classmethod # decorator
  def adding_things(cls, num1, num2):
    return cls('teddy', num1 + num2)

  @staticmethod # decorator
  def adding_things2(num1, num2):
    return num1 + num2


player1 = PlayerCharacter('Kritagya', 22)
player2 = PlayerCharacter('Yash', 22)
player1.shout()
print(player1.adding_things(2, 3))
player3 = PlayerCharacter.adding_things(2, 3)
print(player3.shout())
print(type(player1))
print(player3.adding_things2(4, 5))
print(PlayerCharacter.adding_things2(3, 4))
print(player3.return_self())