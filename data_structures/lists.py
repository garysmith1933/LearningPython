my_list = [1,2,3]

another_list = ['four', 'five']

new_list = my_list + another_list

new_list[0] = '0NE ALL CAPS'
new_list.append('six') # equivalent to push in javascript
print(new_list)


print(new_list.pop()) # pop is the same as javascript
print(new_list.pop(0))
print(new_list)


new_list = ['a','d','x','t','v','c']

#neither sort/reverse can be store to variable, is done in place
new_list.sort()
sorted = new_list
print(sorted)

sorted.reverse()
reversed = sorted
print(reversed)