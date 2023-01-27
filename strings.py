# Strings

# use \n in prints to make a new line
# \t in prints make a tab
#print("Hi \nGary")
#print ("Good \t Day")

# len checks the length of a string. 
#print(len("I like food"))

#getting a specific index in a string is the same as javascript
mystring = "hello world"
#print(mystring[0])

newstr = 'abcdef'
#you can get every index including the second this way
print(newstr[2:])

#you can get indexes before but not including the 3rd this way
print(newstr[:3])

#will log from 1 to 4
print(newstr[1:4])

#will log the string in reverse
print(newstr[::-1])

#String concatentation
name = 'Sam'

last_letters = name[1:]

pam = 'P' + last_letters
print(pam)

letter = 'z'
print(letter * 10) #prints zzzzzzzzzz
 
x = 'Hello World'

x = x.upper() #toUpperCase()
x = x.lower() #toLowerCase()

x = 'Hi this is a string'
x = x.split() #transforms to list. works the same as javascript
