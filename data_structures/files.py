myfile = open('myfile.txt') # opens the file

print(myfile.read()) # reads the file

myfile.seek(0) # resets the cursor to be read at the top of the file, 
# otherwise a second read call will be an empty string

print(myfile.readlines()) # creates a list where every line is an index

# /c//Users//thega//Desktop//LearningPython
# need to use double slashes so python doesnt treat \ as an escape character

myfile.close()

# wont have to worry about closing this way
# modes, r = read, w = write, a = append
with open('myfile.txt', mode='r') as my_new_file: 
  contents = my_new_file.read()

with open('myfile.txt', mode= 'a') as f: 
  f.write('\nFOUR ON FOURTH')

with open('myfile.txt', mode='r') as f: 
  print(f.read())

# will overwrite file, or create if file does not exist
with open('adfadfadf.txt', mode = 'w') as f: 
  f.write('IM ON MY WAY')

with open('adfadfadf.txt', mode = 'r') as f: 
  print(f.read())