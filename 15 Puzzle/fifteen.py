''' DO NOT FORGET TO ADD COMMENTS '''
# author: Justin Jiang
# date: March 16, 2023
# file: fifteen.py a Python program that implements the game of Fifteen Puzzle
# input: user selects numbers they want to move to
# output: the board is updated and the user is notified if they have won
from graph import Graph
import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.size = size
        self.adj = [[self.tiles[1], self.tiles[4]],[self.tiles[0], self.tiles[2], self.tiles[5]],[self.tiles[1], self.tiles[3], self.tiles[6]],[self.tiles[2], self.tiles[7]],
                    [self.tiles[0], self.tiles[5], self.tiles[8]],[self.tiles[1], self.tiles[4], self.tiles[6], self.tiles[9]],[self.tiles[2], self.tiles[5], self.tiles[7], self.tiles[10]],[self.tiles[3], self.tiles[6], self.tiles[11]],
                    [self.tiles[4], self.tiles[9], self.tiles[12]],[self.tiles[5], self.tiles[8], self.tiles[10], self.tiles[13]],[self.tiles[6], self.tiles[9], self.tiles[11], self.tiles[14]],[self.tiles[7], self.tiles[10], self.tiles[15]],
                    [self.tiles[8], self.tiles[13]],[self.tiles[9], self.tiles[12], self.tiles[14]],[self.tiles[10], self.tiles[13], self.tiles[15]],[self.tiles[11], self.tiles[14]]]
            
    #swaps the values of the two tiles and updates the adjacency list
    def update(self, move):
        for i in range(len(self.tiles)):
            if self.tiles[i] == 0:
                zero = i
            if self.tiles[i] == move:
                move_index = i
        if self.is_valid_move(move):
            self.transpose(zero, move_index)
            
        else:
            print("Invalid move")

        
    #switches the values of i tile and j tile
    def transpose(self, i, j):
        
        zero, move= self.tiles[i], self.tiles[j]
       
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]
        
        for n in range(len(self.adj)):
            for k in range(len(self.adj[n])):
                if self.adj[n][k] == zero:
                    self.adj[n][k] = move
                elif self.adj[n][k] == move:
                    self.adj[n][k] = zero
     
           
        

    #shuffles the numbers
    def shuffle(self, steps=30):
        for i in range(len(self.tiles)):
            if self.tiles[i] == 0:
                start = i
        #randomly chooses a valid move from the adj list
        for n in range(steps):
            move = choice(self.adj[start])
            for k in range(len(self.tiles)):
                if move == self.tiles[k]:
                    moveid = k
        
            self.transpose(start, moveid)
            start = moveid
            
            
                

           

            
        
    #checks if the the tile is adjacent to the empty tile
    def is_valid_move(self, move):

        for i in range(len(self.tiles)):
            if self.tiles[i] == 0:
                zero = i
       
        if move in self.adj[zero]:
            return True
        return False
                

    #checks if the board is equal to the solved board
    def is_solved(self):
        return np.array_equal(self.tiles, np.array([i for i in range(1,len(self.tiles))] + [0]))
    
    #prints the board
    def draw(self):
        l = list(self.tiles)
        for i in range(len(l)):
            if l[i] == 0:
                l[i] = '  '
            else:
                l[i] = str(l[i]).rjust(2)
        print("+----+----+----+----+")
        print("| {} | {} | {} | {} |". format(l[0], l[1], l[2], l[3]))
        print("+----+----+----+----+")
        print("| {} | {} | {} | {} |". format(l[4], l[5], l[6], l[7]))
        print("+----+----+----+----+")
        print("| {} | {} | {} | {} |". format(l[8], l[9], l[10], l[11]))
        print("+----+----+----+----+")
        print("| {} | {} | {} | {} |". format(l[12], l[13], l[14], l[15]))
        print("+----+----+----+----+")
        
    #formats the str when printed
    def __str__(self):
        count = 0
        output = ""
        for i in self.tiles:
            count += 1
            if i == 0:
                i = ''
            if count % 4 == 0:
                output += '{:>2} \n'.format(i)
            else:
                output += '{:>2} '.format(i)
        
        return output
        

# 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n
# 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n
          


if __name__ == '__main__':
    
    game = Fifteen()
   
    
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    print('All tests passed!')
    
    '''You should be able to play the game if you uncomment the code below'''
  
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')

    
    
        
