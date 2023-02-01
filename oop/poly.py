
class Animal():

  def __init__(self, name) -> None:
    self.name = name

  def speak(self):
    raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):

  def __init__(self, name):
    self.name = name

  def speak(self):
    return self.name + " says woof!"


class Cat(Animal):

  def __init__(self, name):
    self.name = name

  def speak(self):
    return self.name + " says meow!"


niko = Dog("niko")
bojji = Cat("bojji")

for pet in [niko, bojji]:
  print(type(pet))
  # print(pet.speak())

def pet_speak(pet):
  print(pet.speak())

pet_speak(bojji)
pet_speak(niko)

fido = Dog("Fido")
isis = Cat("Isis")

print(isis.speak())
print(fido.speak())


# Seperate classes that have to share same method name allowing you to call those methods 
# without worrying about a specific class being passed in