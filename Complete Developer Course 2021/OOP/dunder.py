class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
      'name': 'yoyo',
      'has_pets': False
    }

  def __str__(self):
    return f'{self.color} is the toys color'

  def __len__(self):
    return 5

  def __del__(self):
    print('deleted|')

  def __call__(self):
    return 'yess ??'

  def __getitem__(self, i):
    return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure)) # will invoke object.__str__()
print(len(action_figure))
print(action_figure())
print(action_figure['name'])

del action_figure
