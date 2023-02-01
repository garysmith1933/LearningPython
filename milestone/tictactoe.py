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
  
def player_move(player, game_board, taken_spaces):
  choice = ''
  current_player = 'Player 1' if player == 'X' else 'Player 2'

  while choice not in game_board:
    choice = int(input(f"{current_player}, choose a position 1 to 9: "))

    if choice not in game_board:
      print('Invalid position: Please choose from 1 to 9: ')
    
  idx = game_board.index(choice)
  game_board[idx] = player
  taken_spaces.add(idx)

  display_board(game_board)
  return game_board

def three_in_a_row(position, player, game_board, count=0):
  # if the count is equal to 3, we have a winner, return true

  if count == 3: 
    return True

  print(position, count)
  if position - 1 not in range(0, len(game_board)):
    return False

  # is it a valid position, ex: X or O
  value = game_board[position - 1]
  print(f"The current value at {position - 1} is {value} ")
  
  # does it fall within range, does it match the player
  matches_player = value == player

  if not matches_player: 
    return False

  #Vertical Check
  vertical = three_in_a_row(position + 3, player, game_board, count + 1)

  #Horizontal Check
  horizontal = three_in_a_row(position + 1, player, game_board, count + 1)

  # Forward Diagonal
  diagonal = three_in_a_row(position + 4, player, game_board, count + 1)

  # Backwards Diagnonal - if and only if the position is 3
  if position == 3:
    backward_diagonal = three_in_a_row(position + 2, player, game_board, count + 1)
    if backward_diagonal == True:
      return True

  return vertical or horizontal or diagonal

def has_won(player, game_board):
  #iterating over, find the first value that has the player
  for pos, value in enumerate(game_board):
    if value == player:
      if three_in_a_row(pos + 1, player, game_board) == True:
        return True
  return False

player1 = start_game()
player2 = 'X' if player1 == 'O' else 'O'
print(f'\nPlayer 1: {player1} ', f'Player 2: {player2}', '\n')
winner = False

taken_spaces = set()

def game():
  while not winner or len(taken_spaces) == len(game_board):
    player_move(player1, game_board, taken_spaces)

    if has_won(player1, game_board) == True:
      print('Player 1 has won the game!')
      display_board(game_board)
      break
    
    player_move(player2, game_board, taken_spaces)

    if has_won(player2, game_board) == True:
      print('Player 2 has won the game!')
      display_board(game_board)
      break

  if len(taken_spaces) == len(game_board):
    print('Ladies and gentlemen...its a draw!')

game()


# board[1] == mark and board[2] == mark and board[3] == mark

#better way
# board[4] == board[5] == board[6] == mark