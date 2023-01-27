myList = [1,2,3,4,5,6,7,8,9,10]

#equivalent to for of loop in javascript
for num in myList:
  if num % 2 == 0: 
    print(num)
  else:
    # print(f'Odd Number {num}')
    print('Odd Number {}'.format(num))

list_sum = 0 

for num in myList:
  list_sum = list_sum + num
  print(list_sum)

mystring = 'Hello World'

for letter in mystring:
  print(letter)

tup = (1,2,3)

for item in tup:
  print(item)

mylist = [(1,2), (3,4), (5,6), (7,8)]

#tuple unpacking, you can take individual items from a tuple. similar to object destructring
for (a,b) in mylist: 
  print(a, b)

d = {'k1': 1,'k2': 2,'k3': 3}

for (key,value) in d.items():
  print(value)