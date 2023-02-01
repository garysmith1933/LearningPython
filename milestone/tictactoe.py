# 2 players should be able to play (both sitting at same computer)
# The board should be printed out everytime a player makes a move
# You should be able to accept input of the player position 
# and then place a symbol on the board

#create board
game_board = [
  1,2,3,
  4,5,6,
  7,8,9
]

def display_board(game_board):
  print('Here is the game board')
  print(str(game_board[0]) + '|' + str(game_board[1]) + '|' + str(game_board[2]))
  print('------')
  print(str(game_board[3]) + '|' + str(game_board[4]) + '|' + str(game_board[5]))
  print('------')
  print(str(game_board[6]) + '|' + str(game_board[7]) + '|' + str(game_board[8]))

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
display_board(game_board)
winner = False


def player_move(player, game_board):
  choice = ''
  current_player = 'Player 1' if player == 'X' else 'Player 2'

  while choice not in game_board:
    choice = int(input(f"{current_player}, choose a position 1 to 9: "))

    if choice not in game_board:
      print('Invalid position: Please choose from 1 to 9: ')

  idx = game_board.index(choice)
  game_board[idx] = player

  display_board(game_board)
  return game_board

def three_in_a_row(position, player, game_board, count=1):
  # if the count is equal to 3, we have a winner, return true
  if count == 3: 
    return True

  # is it a valid position, ex: X or O
  value = game_board[position]

  # does it fall within range, does it match the player
  is_valid = value != None and value == player

  if not is_valid: 
    return False

  #Vertical Check
  vertical = three_in_a_row(position + 3, player, game_board, count + 1)

  #Horizontal Check
  horizontal = three_in_a_row(position + 1, player, game_board, count + 1)

  # Forward Diagonal
  diagonal = three_in_a_row(position + 4, player, game_board, count + 1)

  # Backwards Diagnonal - if and only if the position is 3
  if position == 3 and count == 1:
    backward_diagonal = three_in_a_row(position + 2, player, game_board, count + 1)

  return vertical or horizontal or diagonal or vertical

def has_won(player, game_board):
  #iterating over, find the first value that has the player
  for pos, value in enumerate(game_board):
    if value == player:
      if three_in_a_row(pos + 1, player, game_board) == True:
        return True
  return False

player_move(player1, game_board)
player_move(player2, game_board)
#check if either player one
# check if there are still playable spaces using a set