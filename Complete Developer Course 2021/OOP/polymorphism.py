class User():
  def sign_in(self):
    print('logged in')

  def attack(self):
    print('do nothing')

class Wizard(User):

  def __init__(self, name, power):
    self.name = name
    self.power = power
  
  def attack(self):
    User.attack(self)
    print(f'attacking with power of {self.power}')


class Archer(User):

  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows
  
  def attack(self):
    # User.attack(self)
    print(f'attacking with {self.num_arrows} arrows')

def player_attack(char):
  char.attack()

wizard1 = Wizard('kritagya', 100)
print(type(wizard1))
wizard1.sign_in()

wizard1.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))

archer1 = Archer('yash', 22)
player_attack(wizard1)
player_attack(archer1)
