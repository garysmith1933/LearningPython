#classes uses camelCasing as opposed to everything else that is snake_casing
class Dog():

  # CLASS OBJECT ATTRIBUTE
  # SAME FOR ANY INSTANCE OF A CLASS
  species = 'mammal'
  
  #this is basically the constructor. you need to pass in self, where you wouldnt do to this in javascript
  def __init__(self, mybreed, name):
    #this.breed = breed - javascript

    #Attributes
    self.breed = mybreed
    self.name = name
    
  #OPERATIONS /Actions --> Methods
  def bark(self, number):
    print(f'WOOF! My name is {self.name} and my number is {number}')


my_dog = Dog(mybreed='Huskie', name='Lucky')
my_dog.bark(2)

class Circle():
  
  #CLASS OBJECT ATTRIBUTE
  pi = 3.14

  def __init__(self,radius=1):
    self.radius = radius
    self.area = radius * radius * self.pi # could also be seen as Circle.pi

  # METHOD
  def get_circumfrence(self):
    return self.radius * self.pi * 2

my_circle = Circle(30)

print(my_circle.pi)
print(my_circle.get_circumfrence())
print(my_circle.area)