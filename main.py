from os import curdir
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import random
from rps_classes import RpsGame
import rps_constants as rpsc


# Tkinter initialization
root = Tk()
root.title(rpsc.WINDOW_TITLE)

# initialize the game
game = RpsGame(rpsc.DEFAULT_GAME)
game.load()

# functions
def load():
    """Loading function for the load-Button that will display a filedialog.
    If a file is picked, the game will be reloaded with the new configuration.
    """
    file = filedialog.askopenfilename(filetypes=[("JSON files", ".json")], initialdir=curdir)
    # reinitialize our game if a file was picked
    if file:
        game.filename = file
        try:
            game.load()
            # refresh GUI possibilities
            box.configure(values=game.elements)
        except Exception as err:
            messagebox.showerror(title=rpsc.GUI_ERROR_TITLE, message=err)

def fight():
    """Fighting function for the fight-Button that will evaluate the two chosen 
    RpsElements and display  the result within the GUI.
    """
    # player
    player_txt = box.get()
    player = next(e for e in game.elements if e.name == player_txt)
    opponent = random.choice(game.elements)
    # update opponent choice
    lbl_op_selection["text"] = opponent

    # get the result
    result = player.eval(opponent)

    # announce the result to the player
    if(result == rpsc.GAME_CONDITION_WIN):
        lbl_result["text"] = rpsc.GAME_TEXT_WIN
        lbl_result.configure(background="green")
    elif(result == rpsc.GAME_CONDITION_LOSE):
        lbl_result["text"] = rpsc.GAME_TEXT_LOSE
        lbl_result.configure(background="red")
    elif(result == rpsc.GAME_CONDITION_DRAW):
        lbl_result["text"] = rpsc.GAME_TEXT_DRAW
        lbl_result.configure(background="grey")


"""
TKinter Definition if the GUI.
"""

# row 0 Labels only
lbl_player = Label(root, text=rpsc.GUI_LABEL_PLAYER, width=rpsc.GUI_LABEL_WIDTH, foreground="black", background="green")
lbl_player.grid(row=0, column=0)

lbl_vs = Label(root, text=rpsc.GUI_LABEL_VERSUS, width=rpsc.GUI_LABEL_WIDTH, foreground="black")
lbl_vs.grid(row=0, column=1)

lbl_opponent = Label(root, text=rpsc.GUI_LABEL_OPPONENT, width=rpsc.GUI_LABEL_WIDTH, foreground="black", background="blue")
lbl_opponent.grid(row=0, column=2)

# row 1 Combobox and Fight Button
box = ttk.Combobox(root, values=game.elements, width=rpsc.GUI_COMBO_WIDTH, foreground="black", state="readonly")
box.grid(row=1, column=0)
box.current(0)

btn_fight = Button(root, command=fight, width=rpsc.GUI_BUTTON_WIDTH, text=rpsc.GUI_BUTTON_FIGHT, foreground="black")
btn_fight.grid(row=1, column=1)

lbl_op_selection = Label(root, text=rpsc.GUI_LABEL_OPPONENT_SELECTION, width=rpsc.GUI_LABEL_WIDTH, foreground="black")
lbl_op_selection.grid(row=1, column=2)

# row 2 result label
lbl_result = Label(root, text="", foreground="black")
lbl_result.grid(row=2, column=0, columnspan=3)

# row 3 open file
btn_load = Button(root, command=load, width=rpsc.GUI_BUTTON_WIDTH, text=rpsc.GUI_BUTTON_LOAD, foreground="black")
btn_load.grid(row=3, column=0)

btn_quit = Button(root, command=root.destroy, width=rpsc.GUI_BUTTON_WIDTH, text=rpsc.GUI_BUTTON_QUIT, foreground="black")
btn_quit.grid(row=3, column=2)

# Tkinter main loop
root.mainloop()