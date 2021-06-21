class Vehicle:

  number_of_wheels = 4

  def __init__(self, make, model, fuel="gas"):
    self.make = make
    self.model = model
    self.fuel = fuel
  
  def __str__(self):
    return f"I drive {self.make} {self.model} it runs on {self.fuel}."

  def __repr__(self):
    pass


class Car(Vehicle):

  number_of_wheels = 4


class Truck(Vehicle):

  number_of_wheels = 6

  def __init__(self, make, model, fuel="diesel"):
    super().__init__(make, model, fuel)






daily = Vehicle("Suburu", "Crosstreck")
daily.number_of_wheels = 3
print(daily)
print("Instance", daily.number_of_wheels)
print("Class", Vehicle.number_of_wheels)

