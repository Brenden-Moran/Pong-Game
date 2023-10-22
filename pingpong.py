# Author: Brenden Moran
# Date 3/9/23

from tkinter import *


def move_right(move):
    canvas.move(racket_id_2, 15, 0)             # Moves user's racket right 15 pixels


def move_left(move):
    canvas.move(racket_id_2, -15, 0)            # Moves user's racket left by 15 pixels


def change_txt():
    global height
    global text_id
    global score_1
    global score_2
    x1, y1, x2, y2 = canvas.coords(ball)        # Coordinates of the balls location on the pixel map
    if test:
        score_1 = 0                             # Sets default scores to 0
        score_2 = 0
    if y2 > height:     # Updates score if ball's y coordinate hits top of screen
        canvas.delete(text_id)
        text_id = canvas.create_text(400, 470, text=f'Score {score_1 + 1}:{score_2}', font=('Times', 20))
        score_1 += 1

    elif y1 < 0:        # updates score if ball's y coordinates hits bottom of screen
        canvas.delete(text_id)
        text_id = canvas.create_text(400, 470, text=f'Score {score_1}:{score_2 + 1}', font=('Times', 20))
        score_2 += 1
    else:   # Displays default scores
        text_id = canvas.create_text(400, 470, text=f'Score {score_1}:{score_2}', font=('Times', 20))


def animation():
    global dx; global dy
    x1, y1, x2, y2 = canvas.coords(ball)
    racket2_x1, racket2_y1, racket2_x2, racket2_y2 = canvas.coords(racket_id_2)     # Gets racket's coordinates
    racket_x1, racket_y1, racket_x2, racket_y2 = canvas.coords(racket_id)
    if x2 > width or x1 < 0:        # Changes direction of ball's motion in the x-direction
        dx = - dx
    if racket_x1 <= x1:
        canvas.move(racket_id, 15, 0)
    if racket_x2 >= x2:
        canvas.move(racket_id, -15, 0)
    if y2 >= racket2_y1 and y2 <= racket2_y2:
        if x1 >= racket2_x1 and x2 <= racket2_x2:
            dy = - dy
    if y1 <= racket_y2 and y1 >= racket_y1:         # Checks if ball was hit by a racket
        if x1 >= racket_x1 and x2 <= racket_x2:     # if so then change direction of ball's motion in y-direction
            dy = - dy
    if y2 > height or y1 < 0:                       # if ball hits the top or bottom of the canvas
        change_txt()                                # then change the score and reset the ball
        canvas.coords(ball, 125, 225, 140, 240)

    canvas.move(ball, dx, dy)
    canvas.after(10, animation)                     # recursively calls on the animation function


gui = Tk()
canvas = Canvas(gui, height=500, width=500)                 # Creates the canvas
ball = canvas.create_oval(125, 225, 140, 240, fill="red")   # Creates the ball
canvas.pack()
width = int(canvas.cget('width'))
height = int(canvas.cget('height'))
dx, dy = 2, 2
racket_id = canvas.create_rectangle(0, 100, 100, 110, fill='black')     # Creates racket
racket_id_2 = canvas.create_rectangle(0, 400, 100, 410, fill='blue')    # Creates other racket
canvas.bind_all('<KeyPress-Left>', move_left)                           # based on user's input, move the racket
canvas.bind_all('<KeyPress-Right>', move_right)
test = True
change_txt()
test = False
animation()
mainloop()
