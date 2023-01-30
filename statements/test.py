st = 'Print only the words that start with s in this sentence'

s = st.split()
print(s)

for word in s:
  if word[0].lower() == 's':
    print(word)

evens = list(range(0,11,2))
print(evens)

mod3 = [x for x in range(0,51) if x % 3 == 0]
print(mod3)

for char in s:
  if len(char) % 2 == 0:
    print(char, 'even')
  else: print(char, 'odd')

first_letter = [word[0] for word in st.split()] 
print(first_letter) #['P', 'o', 't', 'w', 't', 's', 'w', 's', 'i', 't', 's']