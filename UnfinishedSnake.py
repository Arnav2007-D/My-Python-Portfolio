from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "#8F00FF"
FOOD_COLOUR = "#FFFF00"
BACKGROUND_COLOUR = "000000"

class snake():
    pass

class Food():
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collsion():
    pass

def game_over():
    pass
window = Tk()
window.title("Arnav's Snake Game")
window.resizable(False, False)


score = 0
direction = 'down'

label = Label(window, text="score:{}".format(score), font=('Courier', 24))
label.pack()

canvas = Canvas(window, bg= BACKGROUND_COLOUR, height= GAME_HEIGHT, width= GAME_WIDTH)
canvas.pack()

window_update()

window_width = window.winfo_height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+

window.mainloop()
