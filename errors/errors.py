def add(n1, n2):
  try:
    res = n1 + n2
  except: 
    print("Something is off")
  
  # if there is no error, do this
  else:
    print(f'Here is the result, {res}')

add(10, 10)

try:
  f = open('testfile', 'w')
  f.write("Write a test line")

#you can do stuff after looking for a specific error
except TypeError:
  print("There was a type error")

#catch in javascript
except:
  print("All other exceptions")

# will always run regardless of it working or error
finally:
  print("I always run")