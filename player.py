from random import choice
class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            # return an instance sign
            return self.sign
      def get_name(self):
            # return an instance name
            return self.name
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            cell_values = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

            while True:
                print()
                user_input = input(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ").upper()
                print()
                if user_input not in cell_values or board.isempty(user_input) == False:
                    print("You did not choose correctly. ")
               
                elif board.isempty(user_input) == True and user_input in cell_values:
                    board.set(user_input, self.sign)
                    break
                     


class AI(Player):
    def __init__(self, name, sign, board):
            super().__init__(name, sign)  # player's name
            
           

    def choose(self, board):
            cell_values = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            while True: 
                AI_choose = choice(cell_values)
                if board.isempty(AI_choose):
                    print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
                    print(AI_choose)
                    board.set(AI_choose, self.sign)
                    break
                


class MiniMax(AI):

    def __init__(self, name, sign, board):
            super().__init__(name,sign, board)  

    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)
    

    def minimax(self, board, self_player, start):
        # check the base conditions
        cell_values = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == "":
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1

        else:
            max = -float("inf")
            min = float("inf")
            
            for cell in cell_values:
                if board.isempty(cell):
                    if self_player:
                        board.set(cell, self.sign)
                    else:
                        if self.sign == "X":
                            board.set(cell, "O")
                        else:
                            board.set(cell,"X")
                        
                    score = MiniMax.minimax(self,board, not self_player, False)
                    board.set(cell, " ")
                    if self_player and max < score:
                        move = cell
                        max = score
                    elif not self_player and min > score: 
                        min = score

            if start:
                return move
            elif self_player:
                return max
            else:
                return min

        
class SmartAI(AI):
    pass

            
        
                
                








       