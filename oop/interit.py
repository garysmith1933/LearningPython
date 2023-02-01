class Animal():

  def __init__(self):
    print("ANIMAL CREATED")

  def who_am_i(self):
    print("I am an animal")

  def eat(self):
    print("I am eating")

myanimal = Animal()

#Derive Class
class Dog(Animal):
  
  def __init__(self):
    Animal.__init__(self)
    print("Dog Created")
  
  def who_am_i(self):
    print("Im a dog")

  def bark(self):
    print("WOOF!")

mydog = Dog()
mydog.eat()
mydog.who_am_i() 
mydog.bark()

# the dog class now has all methods from the animal class
# these methods can be over written by initalizing a method with the same name on the derive class