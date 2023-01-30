from random import shuffle

def shuffle_list(mylist):
  shuffle(mylist)
  return mylist

def player_guess():
  guess = ''
  while guess not in ['0', '1', '2']:
    guess = input("Pick a number: 0, 1, or 2") # input always return a string
  
  return int(guess)

def check_guess(mylist, guess):
  if mylist[guess] == 'O':
    return f'Congrats you found the ball! {mylist}'

  else: 
    return f'Oops, its not that one! {mylist}'

    
mylist = [ ' ', 'O', ' ']
example = [1,2,3,4,5,6,7]
mixedup_list = shuffle_list(mylist)
user_guess = player_guess()
print(check_guess(mixedup_list, user_guess))