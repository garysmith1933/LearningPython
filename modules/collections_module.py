# counter counts the # of times a value shows up in the list passed in
from collections import Counter

mylist = [1,1,1,1,2,2,2,2,3,3,3,3]
counted = Counter(mylist)
# print(counted)

#if you use a string it has to be split into an array
sentence = "How many times does each word show up in this phrase"
wordcount = Counter(sentence.split())
# print(wordcount)

letters = 'aaaabbbcccdddd'
c = Counter(letters)
print(c.most_common()) # returns list of tuples with the first value being the most common
print(list(c))

# in short, its an easy way to do a hashmap

from collections import defaultdict
 
d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])
print(d['wrong key']) # would normally give KeyError but instead sets the value to 0
print(d)

# acts as a guard incase key is not yet set with a default value

mytuple = (10,20,30)
mytuple[0]

# easier way to get data when youre not sure of index of value or alot of data in list
from collections import namedtuple

# parameters = type, list of attributes
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5, breed='husky', name='Sam')

print(type(sammy)) # <class '__main__.Dog'>
print(sammy)