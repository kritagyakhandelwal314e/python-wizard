

class User():
  def sign_in(self):
    print('logged in')



class Wizard(User):

  def __init__(self, name, power):
    self.name = name
    self.power = power
  
  def attack(self):
    print(f'attacking with power of {self.power}')


class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows
  
  def attack(self):
    print(f'attacking with {self.num_arrows} arrows')


wizard1 = Wizard('kritagya', 100)
print(type(wizard1))
wizard1.sign_in()

wizard1.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
