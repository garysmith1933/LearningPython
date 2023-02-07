import time 

# # Current time
# start_time = time.time()
# # run code
# result = func_one(100000)
# # Current time after 
# end_time = time.time()

# elapsed = end_time - start_time
# print(elapsed)

import timeit

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
  return [str(num) for num in range(n)]
'''

test = timeit.timeit(stmt, setup, number=1000000)
print(test)


stmt = '''
func_two(100)
'''

setup = '''
def func_two(n):
  return list(map(str,range(n)))
'''

test2 = timeit.timeit(stmt, setup, number=1000000)
print(test2)
