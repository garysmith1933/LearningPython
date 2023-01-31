# 2 players should be able to play (both sitting at same computer)
# The board should be printed out everytime a player makes a move
# You should be able to accept input of the player position 
# and then place a symbol on the board

#create board
def display_board():
  row1 = [7,8,9]
  row2 = [4,5,6]
  row3 = [1,2,3]

  print(str(row1[0]) + '|' + str(row1[1]) + '|' + str(row1[2]))
  print('------')
  print(str(row2[0]) + '|' + str(row2[1]) + '|' + str(row2[2]))
  print('------')
  print(str(row3[0]) + '|' + str(row3[1]) + '|' + str(row3[2]))

# choose X or O
def start_game():
  print("Welcome to Tic Tac Toe!")

  player1 = ''
  while player1 not in ['X', 'O']:
    player1 = input("Player 1, Which will you choose: X or O? ").upper()

    if player1 not in ['X', 'O']:
      print("Sorry, That's not an option here.")

  return player1
  
player1 = start_game()
player2 = 'X' if player1 == 'O' else 'O'
print(f'\nPlayer 1: {player1} ', f'Player 2: {player2}', '\n')

display_board()