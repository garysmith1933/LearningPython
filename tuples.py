t = ('a','a','b')
my_list = [1,2,3]

print(type(t))
print(t.count('a')) #returns count of parameter passed in 
print(t.index('b')) # returns index of parameter passed in

my_list[0] = 'HI'
print(my_list)

#t[0] = 'BYE' => tuple' object does not support item assignment

# The difference between tuples and arrays are that arrays are mutable, tuples are not.
