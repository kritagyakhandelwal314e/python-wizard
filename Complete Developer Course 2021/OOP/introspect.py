class User():
  def __init__(self, email):
    self.email = email
  def sign_in(self):
    print('logged in')

class Wizard(User):

  def __init__(self, name, power, email):
    User.__init__(self, email)
    self.name = name
    self.power = power
  
  def attack(self):
    print(f'attacking with power of {self.power}')


class Archer(User):

  def __init__(self, name, num_arrows, email):
    super().__init__(email) # with super we don't have to pass self
    self.name = name
    self.num_arrows = num_arrows
  
  def attack(self):
    # User.attack(self)
    print(f'attacking with {self.num_arrows} arrows')

def player_attack(char):
  char.attack()

wizard1 = Wizard('kritagya', 100, 'kk@gmail.com')

archer1 = Archer('yash', 22, 'tt@gmail.com')

for i in dir(wizard1):
  print(i)