class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

player1 = PlayerCharacter('kritagya', 22)
print(player1.name)
print(player1.age)

player2 = {'name': 'yash', 'age': 23}
print(player2['name'])
print(player2['age'])
