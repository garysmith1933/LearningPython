x = 6

while x < 5:
  print(f'The current value of x is {x}')
  x += 1

else: 
  print(f'{x} is not less than 5')

x = [1,2,3]

for item in x:
  pass # does nothing, but is used as a placeholder to prevent syntax error
  print('end of my script')

mystring = 'Sammy'

for letter in mystring:
  if letter == 'a':
   break
  print(letter)

  # continue is the same as javascript, skips to the next letter
  # break is the same as javascript, breaks out of the loop