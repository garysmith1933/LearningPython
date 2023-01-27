mystring = 'hello'
mylist = []


mylist = [letter for letter in mystring] #easy way for adding splitting string indexs and putting them in an list
print(mylist) #prints ['h', 'e', 'l', 'l', 'o']

mylist = [num**2 for num in range(0,11)]
print(mylist)

mylist = [x**2 for x in range(0,11) if x % 2 == 0] #can add conditionals
print(mylist)

celcius = [0,10,20,34.5]

fahrenheit = [( (9/5)*temp +32 ) for temp in celcius]
print(fahrenheit)

# The code above is an easier way of doing the code below

fahrenheit = []

for temp in celcius:
  fahrenheit.append((9/5)*temp +32)
print(fahrenheit)

# example of if else statement..dont actually do this, it isnt clear to read..
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)


mylist = []

for x in [2,4,6]:
  for y in [1,10,1000]:
    mylist.append(x*y)
print(mylist)

# readablility sucks.
mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]