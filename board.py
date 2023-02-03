class Board:
       def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
       def get_size(self): 
            return self.size * self.size
       def get_winner(self):
            # return the winner's sign O or X (an instance winner)  
            return self.winner
       def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # you can use a tuple ("A1", "B1",...) to obtain indexes 
            # this implementation is up to you 
            cell_values = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

            index_value = cell_values.index(cell)
            self.board[index_value] = sign


       def isempty(self, cell):
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # return True if the cell is empty (not marked with X or O)
            cell_values = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            index_value = cell_values.index(cell)
            if self.board[index_value] == ' ':
                return True
            else:
                return False

       def isdone(self):
            
            done = False
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X

            #vertical
            if self.board[0] != " " and self.board[1] == self.board[0] and self.board[2] == self.board[0]:
                self.winner = self.board[0]
                done = True
            elif self.board[3] != " " and self.board[4] == self.board[3] and self.board[5] == self.board[3]:
                done = True
                self.winner = self.board[3]
            elif self.board[6] != " " and self.board[7] == self.board[6] and self.board[8] == self.board[6]:
                done = True
                self.winner = self.board[6]
            #diagonal
            elif self.board[0] != " " and self.board[4] == self.board[0] and self.board[8] == self.board[0]:
                done = True
                self.winner = self.board[0]
            elif self.board[6] != " " and self.board[4] == self.board[6] and self.board[2] == self.board[6]:
                done = True
                self.winner = self.board[6]
            #horizontal
            elif self.board[0] != " " and self.board[3] == self.board[0] and self.board[6] == self.board[0]:
                done = True
                self.winner = self.board[0]
            elif self.board[1] != " " and self.board[4] == self.board[1] and self.board[7] == self.board[1]:
                done = True
                self.winner = self.board[1]
            elif self.board[2] != " " and self.board[5] == self.board[2] and self.board[8] == self.board[2]:
                done = True
                self.winner = self.board[2]
            elif(' ' not in self.board):
                self.winner = ''
                done = True
            return done
       def show(self):
            # draw the board
            print()
            print("   A   B   C")
            print(" +---+---+---+")
            print(f'1| {self.board[0]} | {self.board[3]} | {self.board[6]} |')
            print(" +---+---+---+")
            print(f'2| {self.board[1]} | {self.board[4]} | {self.board[7]} |')
            print(" +---+---+---+")
            print(f'3| {self.board[2]} | {self.board[5]} | {self.board[8]} |')
            print(" +---+---+---+")
