#py -3.7 -m pip install pygame

from PIL import ImageTk,Image
import tkinter as tk
import random
import pygame


r = tk.Tk()
r.geometry('700x700')
r.title('Roll Dice')

c = tk.Canvas(r, width=700, height=700)
c.pack()

i = ''


def roll_dice():
    global img,i,bttn_clicks
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d = {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}
    die1 = random.choice(dice)
    die2 = random.choice(dice)
    ldice.configure(text=f'{die1} {die2}')
    c.create_window(350, 250, window=ldice)
    res = d[die1]+d[die2]
    label2.configure(text="You got  "+str(res))
    bttn_clicks += 1
    label1['text'] = "Dice rolled: " + str(bttn_clicks) + " times"
    if (bttn_clicks == 10 and res != 10):
        rollbutton.configure(state='disabled')
        img = ImageTk.PhotoImage(Image.open("game-over2.jpg").resize((700, 200)))
        label4 = tk.Label(r, image=img)
        i = c.create_window(350, 430, window=label4)
        pygame.mixer.init()
        pygame.mixer.music.load('ooh.wav')
        pygame.mixer.music.play()
    elif (res == 10):
        rollbutton.configure(state='disabled')
        img = ImageTk.PhotoImage(Image.open("youwon.jfif").resize((700, 200)))
        label4 = tk.Label(r, image=img)
        i = c.create_window(350, 430, window=label4)
        pygame.mixer.init()
        pygame.mixer.music.load('applause.wav')
        pygame.mixer.music.play()


def restart():
    global bttn_clicks
    global i
    bttn_clicks= 0
    label1.configure(text="")
    label2.configure(text="Not rolled yet")
    pygame.mixer.init()
    pygame.mixer.music.stop()
    if i:
        c.delete(i)
    rollbutton.configure(state='normal')


ldice = tk.Label(r, text='', font=('Times', 120),fg='green')
rollbutton = tk.Button(r, text='Roll the dice', font=('times', 20,"bold"),state="disabled",background="brown",foreground='yellow',height=1, width=15, command=roll_dice)
c.create_window(350, 120, window=rollbutton)
button1 = tk.Button(r, text='Start/Restart game', font=('times', 20,"bold"),background="blue",foreground='white',height=1, width=15, command=restart)
c.create_window(350, 50, window=button1)
label1 = tk.Label(r, text='', font=('Times',20,'bold'),fg='brown')
c.create_window(180, 550, window=label1)
label2 = tk.Label(r, text='Not rolled yet', font=('Times',20,'bold'),bg='purple',fg='yellow',width=12)
c.create_window(480, 550, window=label2)
label3 = tk.Label(r, text='Winning rule: The player wins if he/she gets a sum of 10 on rolling 2 dice,within 10 chances', font=('Times',13,'bold'),fg='white',bg="black")
c.create_window(350, 620, window=label3)

# call the mainloop of Tk
r.mainloop()