import math

value = 4.35

print(math.floor(value)) # 4
print(math.ceil(value)) # 5
#Numpy 

import random 

print(random.randint(0, 100)) # prints random number

random.seed(101)
print(random.randint(0, 100))

mylist = list(range(0,20))
print(random.choice(mylist)) # picks from list

# Sample with replacement has a chance to pick numbers multiple times
print(random.choices(population=mylist, k = 10))

# without replacement will print not repeat picked numbers from a list
print(random.sample(population=mylist, k=10))

#rearranges index of numbers in list
random.shuffle(mylist)
print(mylist)