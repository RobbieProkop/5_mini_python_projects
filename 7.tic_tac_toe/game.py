from player import HumanPlayer, RandomComputer
import time

class TicTacToe:
  def __init__(self):
    self.board = [' ' for _ in range(9)] #single list to represent 3x3 board
    self.current_winner = None # who is the current winner (if any)
    
  def print_board(self):
    # gets the rows
    for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
      print('| ' + ' | '.join(row) + ' |')
      
  @staticmethod
  def print_board_nums():
    # print num that corresponds to each spot
    number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] 
    for row in number_board:
      print('| ' + ' | '.join(row) + ' |')
      
  def available_moves(self):
    #  list comprehension way
    return [i for i, spot in enumerate(self.board) if spot == " "]
    # one way to write this (long way)
    # moves = []
    # for (i, spot) in enumerate(self.board):
    #   # ['x', 'x', 'o'] ---> [(0, 'x'), (1, 'x'), (2, 'o')]
    #   if spot == " ":
    #     moves.append(i)
    # return moves
    
  def empty_squares(self):
    return ' ' in self.board
  
  def num_empty_squares(self):
    return len(self.available_moves())
  
  def make_move( self, square, letter):
    #if invalid move, return false
    if self.board[square] == " ":
      self.board[square] = letter
      
      if self.winner(square, letter):
        self.current_winner = letter

      return True
    return False

  def winner(self,square,letter):
    # must check all posibilities of row column diagonal for 3 
    # check row
    row_index = square // 3
    row = self.board[row_index*3 : (row_index + 1)*3]
    if all([spot == letter for spot in row]):
      return True

    #check column
    col_index = square % 3
    column = [self.board[col_index*3 : (col_index+1)*3] for i in range(3)]
    if all([spot == letter for spot in column]):
      return True
    
    # check diagonal
    # diagonal checking works only on even numbers
    if square % 2 == 0:
      diag1 = [self.board[i] for i in [0, 4, 8]] # top left to bottom right
      if all([spot == letter for spot in diag1]):
        return True
      
      diag2 = [self.board[i] for i in [2, 4, 6]] # top right ot bottom left
      if all([spot == letter for spot in diag2]):
        return True
    
    # if no winner
    return False
      
    
    
def play(game, x_player, o_player, print_game=True):
  if print_game:
    game.print_board_nums()
    
  letter = 'x' #starting letter
  #iterate while game is incomplete
  
  while game.empty_squares():
    # get move from current player
    if letter == 'o':
      square = o_player.get_move(game)
    else:
      square = x_player.get_move(game)
    
    # make a move function
    if game.make_move(square, letter):
      if print_game:
        print(f'{letter} makes a move to square {square}')
        game.print_board()
        print()

      if game.current_winner:
        print(letter + ' wins!')
        return letter
      # alternate letter after move is made
      letter = 'o' if letter == 'x' else 'x'
      
    # slow down computer move for better UX
    time.sleep(0.8)
    
  if print_game:
    print("it's a tie")  
      
      
if __name__ == '__main__':
  x_player = HumanPlayer('x')
  o_player = RandomComputer('o')
  t = TicTacToe()
  play(t, x_player, o_player, print_game=True)