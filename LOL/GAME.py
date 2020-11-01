from tkinter import *
window = Tk()

def roll():
    global ball_x
    global ball_y
    global dx
    global dy
    ball_x = ball_x + dx
    ball_y = ball_y + dy
    if ball_x> 710 or ball_x < -50:
        dx=-dx
    if ball_y>=360 or ball_y < 0:
        dy=-dy
    pad_one_c = canvas.coords(pad_one)
    pad_two_c = canvas.coords(pad_two)

    if ball_y > pad_one_c[1] and ball_y + 30 < pad_one_c[3] and ball_x < 50:
        dx = -dx

    if ball_y > pad_two_c[1] and ball_y + 30 < pad_two_c[3] and ball_x > 625:
        dx = -dx

    canvas.coords(ball, ball_x, ball_y, ball_x + 30, ball_y + 30)
    window.after(40, roll)

def update_score():
    global score_one_player, score_two_player
    if ball_x >= 700:
        score_one_player += 1
        window.itemconfig(player_one_text, text=score_one_player)
    elif ball_x <= -10:
        score_two_player += 1
        window.itemconfig(player_two_text, text=score_two_player)
    window.after(0, roll)

def pad_move(event):
    pad_one_c = canvas.coords(pad_one)
    pad_two_c = canvas.coords(pad_two)
    if event.keysym == 'Down':
       if pad_one_c[1] > 0 and pad_one_c[3] <= 380:
           canvas.move(pad_one, 0, 25)
       else:
           canvas.move (pad_one, 0, -25)

    if event.keysym == 'Up':
       if pad_one_c[1] > 0 and pad_one_c[3] <=380:
            canvas.move(pad_one, 0, -25)
       else:
            canvas.move (pad_one, 0, 25)

    if event.keysym == 'Left':
        if pad_two_c[1] > 0 and pad_two_c[3] <= 380:
            canvas.move(pad_two, 0, 25)
        else:
            canvas.move(pad_two, 0, -25)

    if event.keysym == 'Right':
        if pad_two_c[1] > 0 and pad_two_c[3] <= 380:
            canvas.move(pad_two, 0, -25)
        else:
            canvas.move(pad_two, 0, 25)

canvas = Canvas(window, width=700, height=400, bg="black")
canvas.pack()


dx = 13
dy = 13

ball_x = 325
ball_y = 175

pad_one_x = 20
pad_two_x = 660

pad_one_y = 20
pad_two_y = 20

window.geometry('700x400+0+0')
window.resizable(False, False)


ball = canvas.create_oval(ball_x, ball_y, ball_x + 30, ball_y + 30, fill="white")
pad_one = canvas.create_rectangle(pad_one_x, pad_one_y, pad_one_x + 20, 100, fill="white")
pad_two = canvas.create_rectangle(pad_two_x, pad_two_y, pad_two_x + 20, 100, fill="white")
canvas.create_line(330, 0, 330, 400, dash=(4, 2), fill="white")

score_one_player = 0
player_one_text = canvas.create_text(300, 50, text=score_one_player, font="Arial 20", fill="white")

score_two_player = 0
player_two_text = canvas.create_text(360, 50, text=score_two_player, font="Arial 20", fill="white")



window.bind("<Down>", pad_move)
window.bind("<Up>", pad_move)
window.bind("<Left>", pad_move)
window.bind("<Right>", pad_move)
window.after(0, roll)
window.mainloop()