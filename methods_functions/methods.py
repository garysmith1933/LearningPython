def square(num):
  return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums): # similar to array.map()
  print(item)

def splicer(mystring):
  if(len(mystring) % 2 == 0):
    return 'Even'

  else:
    return mystring[0]
  
names = ['Andy', 'Eve', 'Sally']

res = list( map(splicer, names) ) 
print(res)

res = list(filter(lambda num: num%2 == 0, my_nums)) # similar to array.filter()
print(res)

#Lamda expression - a function you only intend to use one time
square = lambda num: num ** 2 

res = list( map(lambda num: num**2, my_nums) )
print(my_nums, res)

res = list(map(lambda name: name[0], names))
print(res)

# should only use lambda if you are able easily able to read it later