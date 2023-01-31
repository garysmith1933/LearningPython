# def display(row1, row2, row3):
#   print(row1)
#   print(row2)
#   print(row3)

# row1 = [' ', ' ', ' ']
# row2= [' ', ' ', ' ']
# row3 = [' ', ' ', ' ']

# row2[1] = 'X'

# display(row1, row2, row3)

def user_choice():
  acceptable_range = range(0,10)
  within_range = False
  choice = 'N/A'

  while ( choice.isdigit() == False or within_range == False ):
    choice = input("Please enter a number (0,10): ")

    #DIGIT CHECK
    if choice.isdigit() == False:
      print('Sorry that is not a digit')
    
    #RANGE CHECK
    if choice.isdigit() == True:
      if int(choice) in acceptable_range:
       within_range = True
      
      else:
        print('Sorry, you are out of range')
 
  return int(choice)

user_choice()

