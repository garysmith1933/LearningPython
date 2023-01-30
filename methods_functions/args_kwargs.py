# (*args) is the equivalent of ...args in javascript
# this is a set as a tuple of arguments 

# kwargs keyword args
# all arguments are put in a dictionary

def myfunc(**kwargs):
  if ('fruit' in kwargs):
    print('My fruit of choice is {}'.format(kwargs['fruit']))
  
  else: print('No fruit for me')

print(myfunc(fruit='apple', veggie='lettuce', cheese='cheddar'))

#can use both args, and kwargs together
def myfunc2(*args, **kwargs):
  print('I would like {} {}'.format(args[0], kwargs['food']))

myfunc2(10,20,30, fruit='orange', food='eggs', animal='dog')