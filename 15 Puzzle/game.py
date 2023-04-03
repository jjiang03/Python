''' DO NOT FORGET TO ADD COMMENTS '''
# author: Justin Jiang
# date: March 16, 2023
# file: game.py a Python program that implements a GUI for the fifteen puzzle game
# input: user selects numbers they want to move to
# output: the board is updated and the user is notified if they have won
from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
          
#transpose and checks if it is solved
def clickButton(id):
    if textButtons[id].get() == " " or tiles.is_solved():
        return " "
   
    print("Button clicked: " + textButtons[id].get())

    print(f"Button index: {id}")
    
    move = textButtons[id].get() #saves the value of the button clicked
    tiles.update(int(move)) #updates the board with the value
    tiles.draw()

    #updates the numbers on the buttons
    for z in range(len(textButtons)):
        if tiles.tiles[z] == 0:
            textButtons[z].set(" ")
        
        else:
            #replaces the button with the 0 and the 0 tile with the number from the button clicked
            textButtons[z].set(str(tiles.tiles[z]))
    if tiles.is_solved():
        print("Solved!")
        for p in range(len(textButtons)):
            #replaces every single button with "You Win!"
            textButtons[p].set("Solved!")

    
#shuffles the buttons by changing their values
def puzzleShuffle():
    tiles.shuffle()
    for z in range(len(textButtons)):
        if tiles.tiles[z] == 0:
            textButtons[z].set(" ")
        else:
            textButtons[z].set(str(tiles.tiles[z]))
    print("Shuffled")
    
    




  



  
   
if __name__ == '__main__':    

    # make tiles
    tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')
    #shuffle
    tiles.shuffle()
    
    # make buttons
    b = []
    textButtons = []

    for i in range(len(tiles.tiles)):
        text = StringVar()
        text.set(str(tiles.tiles[i]))
        t = text.get()
        if tiles.tiles[i] == 0:
            text.set(" ")
        textButtons.append(text)
        new = Button(gui, textvariable=text, text = text,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda m = i: clickButton(m))
        
        #store button in list
        b.append(new)
   
    #shuffle
    s_button = Button(gui, text="shuffle", name = "shuffle",
                        bg='white', fg='black', font=font, height=1, width=5,
                        command = lambda : puzzleShuffle())
    s_button.grid(row=4, column=3, columnspan=1)

    # the key argument name is used to identify the button
  

    # add buttons to the window
    # use .grid() or .pack() methods
    
    for i in range(4):
        for j in range(4):
            b[i*4+j].grid(row=i, column=j)
    
    gui.update()
    # update the window
    gui.mainloop()
