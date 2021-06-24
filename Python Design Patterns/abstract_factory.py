class Shape2DInterface: # interface class
  def draw(self): pass

class Shape3DInterface: # interface class
  def build(self): pass

# === concrete shape classes ===
class Circle(Shape2DInterface):
  def draw(self):
    print("Circle.draw")

class Square(Shape2DInterface):
  def draw(self):
    print("Square.draw")

class Sphere(Shape3DInterface):
  def draw(self):
    print("Sphere.build")

class Cube(Shape3DInterface):
  def draw(self):
    print("Cube.build")

# === Abstract Shape Factory ===
class ShapeFactory:
  @staticmethod
  def getShape(type):
    if type == 'Circle':
      return Circle()
    if type == 'Square':
      return Square()
    assert 0, "Couldn't find that shape"
