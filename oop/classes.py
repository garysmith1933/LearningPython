#classes uses camelCasing as opposed to everything else that is snake_casing
class Dog():
  
  #this is basically the constructor. you need to pass in self, where you wouldnt do to this in javascript
  def __init__(self, mybreed, name, spots):
    #this.breed = breed - javascript

    #Attributes
    #We take in the argument
    self.breed = mybreed
    self.name = name
    #boolean
    self.spots = spots
    

my_dog = Dog(mybreed='Huskie', name='Lucky', spots=False)

print(type(my_dog))

print(my_dog.spots)