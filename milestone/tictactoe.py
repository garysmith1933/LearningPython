# 2 players should be able to play (both sitting at same computer)
# The board should be printed out everytime a player makes a move
# You should be able to accept input of the player position 
# and then place a symbol on the board

#create board


# choice X or O
def start_game():
  print("Welcome to Tic Tac Toe")

  player1 = ''
  while player1 not in ['X', 'O']:
    player1 = input("Player 1, Which will you choose: X or O? ").upper()

    if player1 not in ['X', 'O']:
      print("Sorry, That's not an option here.")

  return player1
  
player1 = start_game()
player2 = 'X' if player1 == 'O' else 'O'
print(f'player1: {player1} ', f'player2: {player2}')