

# syntax is start, stop, step(ex: 2 will have numbers increment by 2)
for num in range(3,10):
  print(num)

print(list(range(0,11,2))) # prints [0,2,4,6,8,10]

#enumarate is a function that takes in a value, are returns an index counter, and the element at that index
word = 'abcde'
for index,letter in enumerate(word):
  print(index)
  print(letter)

mylist = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

# zip is used to pair 2 lists where the values at each index are paired into tuples
# it will zip as longest as the length of the shortest list
for a,b,c in zip(mylist, mylist2, mylist3):
  print(a,b,c)

newlist = list(zip(mylist, mylist2)) # creates an array of tuples
print(newlist)


print('x' in [1,2,3]) # in operator checks if a value in somethings
print(min(mylist)) # same as Math.min
print(max(mylist)) # same as Math.max

# shuffle takes a list and literally shuffles the values around to new indexs
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist) # shuffle is done in place, cannot be stored to a variable
print(mylist)

from random import randint
randint(0,100) # basically Math.random but easier, given a range returns a number within 
mynum = randint(0, 100) # can be store to a variable
print(mynum)

#input can be used for user input
result = input('Enter a number here:') # can be stored to a variable
print(f'did you know that {result} * 2 is equal to {int(result)*2}? YOU DO NOW!')