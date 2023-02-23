def create_cubes(n):
  for x in range(n):
    yield x ** 3
  
# print(list(create_cubes(10)))

def gen_fibon(n):
  a = 1 # 1 2 3 
  b = 1 # 2 3 5 8 13 21 34 55
  for i in range(n):
    yield a 
    a,b = b, a+b

for num in gen_fibon(10):
  print(num)

  #the goal here is to yield the data and use it as needed
  # as opposed to storing it and using extra memory

  # its remembering what the previous value was, and returning the next value given whatever
  # formula to follow

def simple_gen():
  for x in range(3):
    yield x

# for number in simple_gen():
#   print(number)

# g = simple_gen()
# print(next(g))
# print(next(g))
# print(next(g))


# s = 'hello'
# for letter in s:
#   print(letter)

# s_iter = iter(s)
# print(next(s_iter))