#.format() method
print('This is a string {}'.format('INSERTED'))

print('The {2} {1} {0} '.format('fox', 'brown', 'quick'))
#can use variables to make formatting easier
print('The {q} {b} {f} '.format(f= 'fox', b='brown', q='quick'))

#float formatting {value: width: precison}
result = 100/777
print('The result was {r:1.3f}'.format(r = result))

# string literal
name = "Bob"
print(f'Hello his name is {name}')

name = 'Sam'
age = 3
print(f'{name} is {age}')