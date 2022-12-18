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
      
  