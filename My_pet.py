import tkinter as tk
from tkinter import Canvas

import random
from itertools import cycle


def life_param():
    global happiness_level, energy_level, fullness_level, root, is_fat
    if is_awake:
        if fullness_level <= 200 and is_fat:
            print(fullness_level, is_fat)
            is_fat = False
            c.coords(body, 35, 20, 365, 350)
            c.update()
        c.coords(energy_line, 450,100,450 + energy_level,100)
        energy_label.configure(text='Энергия'+str(energy_level//2)+'%')


        c.coords(happiness_line, 450, 150, 450 + happiness_level, 150)
        happiness_label.configure(text='Счастье' + str(happiness_level // 2) + '%')

        c.coords(fullness_line, 450, 200, 450 + fullness_level, 200)
        fullness_label.configure(text='Сытость' + str(fullness_level // 2) + '%')
        happiness_level -= 4
        energy_level -= 4
        fullness_level -= 4

    else:
        if fullness_level <= 200 and is_fat:
            print(fullness_level, is_fat)
            is_fat = False
            c.coords(body, 35, 20, 365, 350)
            c.update()
        c.coords(energy_line, 450, 100, 450 + energy_level, 100)
        energy_label.configure(text='Энергия' + str(energy_level // 2) + '%')

        c.coords(happiness_line, 450, 150, 450 + happiness_level, 150)
        happiness_label.configure(text='Счастье' + str(happiness_level // 2) + '%')

        c.coords(fullness_line, 450, 200, 450 + fullness_level, 200)
        fullness_label.configure(text='Сытость' + str(fullness_level // 2) + '%')

        if energy_level <= 196:
            energy_level += 8
        fullness_level -= 4


    root.after(5000, life_param)


def blink():
    if is_awake:
        eyes_switch()
        root.after(250, eyes_switch)
        root.after(3500, blink)


def eyes_switch():
    current_state = c.itemcget(eyeball_left, 'state')
    if current_state == tk.NORMAL:
        new_state = tk.HIDDEN
        delta = 10
    else:
        new_state = tk.NORMAL
        delta = -10
    c.itemconfigure(eyeball_left, state=new_state)
    c.itemconfigure(eyeball_right, state=new_state)
    c.itemconfigure(eye_left, state=new_state)
    c.itemconfigure(eye_right, state=new_state)
    c.coords(ear_left,75, 90, 75+delta, 10, 165, 80)
    c.coords(ear_right, 230, 80, 320-delta, 10, 320, 90)


def show_happiness(event):
    global happiness_level
    if is_awake and (20 <= event.x <= 350):
        c.itemconfigure(cheek_left, state=tk.NORMAL)
        c.itemconfigure(cheek_right, state=tk.NORMAL)
        c.itemconfigure(mouth_happy, state=tk.NORMAL)
        c.itemconfigure(mouth_normal, state=tk.HIDDEN)
        if happiness_level <= 198:
            happiness_level += 2

def hide_happiness(event):
    if is_awake:
        c.itemconfigure(cheek_left, state=tk.HIDDEN)
        c.itemconfigure(cheek_right, state= tk.HIDDEN)
        c.itemconfigure(mouth_normal, state=tk.NORMAL)
        c.itemconfigure(mouth_happy, state=tk.HIDDEN)


def feeding(event):
    if is_awake:
        global food, food_colors, happiness_level, energy_level, fullness_level, is_fat
        c.itemconfigure(mouth_happy, state=tk.HIDDEN)
        c.itemconfigure(mouth_normal, state=tk.HIDDEN)
        c.itemconfigure(mouth_eating, state=tk.NORMAL)
        if 470 < event.x < 500 and 350 < event.y < 380:
            food = food_fly(event.x, event.y, food)


        c.itemconfigure(mouth_happy, state=tk.NORMAL)
        c.itemconfigure(mouth_eating, state=tk.HIDDEN)
        c.itemconfigure(cheek_left, state=tk.NORMAL)
        c.itemconfigure(cheek_right, state=tk.NORMAL)
        if happiness_level <= 196:
            happiness_level += 4
        if energy_level <= 196:
            energy_level += 4
        if fullness_level <= 192:
            fullness_level += 8
        else:
            fullness_level += 8

        if 220 <= fullness_level <= 240 and not is_fat:
            c.coords(body,15,10,390,375)
            is_fat = True


def food_fly(x, y, food):
    root.after(320, c.move(food, -20, -40))
    c.update()
    root.after(320, c.move(food, -50, -20))
    c.update()
    root.after(320, c.move(food, -60, -20))
    c.update()
    root.after(320, c.move(food, -60, -20))
    c.update()
    root.after(450, c.delete(food))
    c.update()
    fd_color = next(food_colors)
    food_label['bg']=fd_color
    return c.create_oval(470, 350, 500, 380, outline=next(food_colors),
                             fill=fd_color)


def sleep_rise():
    global is_awake
    if is_awake:
        is_awake = False
        cmd_sleep['text'] = 'Разбудить'
        eyes_switch()

    else:
        is_awake = True
        cmd_sleep['text'] = 'Здоровый сон'
        eyes_switch()
        blink()


is_awake = True
is_fat = False

energy_level = 200
happiness_level = 200
fullness_level = 200


root = tk.Tk()
root.geometry('700x400')
root.title("Мой питомец")

c = tk.Canvas(width=700, height=400, bg = 'darkblue')

BODY_COLOR = 'SkyBlue1'
body = c.create_oval(35, 20, 365, 350, outline=BODY_COLOR, fill=BODY_COLOR)
ear_left = c.create_polygon(75, 90, 75, 10, 165, 80, outline=BODY_COLOR, fill=BODY_COLOR)
ear_right = c.create_polygon(230, 80, 320, 10, 320, 90, outline=BODY_COLOR, fill=BODY_COLOR)
foot_left = c.create_oval(55, 320, 145, 370, outline=BODY_COLOR, fill=BODY_COLOR)
foot_rigth = c.create_oval(250, 320, 340, 370, outline=BODY_COLOR, fill=BODY_COLOR)

eye_left_closed = c.create_line(130,145,145,170,160,145, smooth=1,width=2)
eye_left_closed = c.create_line(230,145,245,170,260,145, smooth=1,width=2)
eye_left = c.create_oval(130, 110, 160, 170, outline="black", fill="white", state=tk.NORMAL)
eye_right = c.create_oval(230, 110, 260, 170, outline="black", fill="white", state=tk.NORMAL)
eyeball_left = c.create_oval(140, 145, 150, 155, outline="black", fill="black", state=tk.NORMAL)
eyeball_right = c.create_oval(240, 145, 250, 155, outline="black", fill="black", state=tk.NORMAL)

cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=tk.HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=tk.HIDDEN)


mouth_normal = c.create_line(170, 250, 200, 265, 230, 250, smooth=1, width=2, state=tk.NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=tk.HIDDEN)
mouth_eating = c.create_oval(185, 240, 215, 270, width=2, state=tk.HIDDEN)

food_colors = cycle(['red','green','yellow','white','purple','brown','grey',
               'dark sea green', 'sea green', 'medium sea green','forest green', 'olive drab'])
food_color = next(food_colors)
food_label = tk.Label(root, text = 'МОЯ ЕДА ->', bg=food_color)
food_label.place(x=370, y=355)
food = c.create_oval(470,350,500,380, outline = next(food_colors),
                     fill=food_color, tag = 'food1')
energy_line = c.create_line(450,100,450 + energy_level,100, fill = 'yellow',
                            width = 5)
energy_label = tk.Label(root, text = 'Энергия'+str(energy_level//2)+'%', bg = 'darkblue',
                        fg = 'yellow')
energy_label.place(x = 450, y = 75)

happiness_line = c.create_line(450,150,450 + happiness_level,150, fill = 'green',
                            width = 5)
happiness_label = tk.Label(root, text = 'Энергия'+str(energy_level//2)+'%', bg = 'darkblue',
                        fg = 'green')
happiness_label.place(x=450, y=125)

fullness_line = c.create_line(450,200,450 + energy_level,200, fill = 'brown',
                            width = 5)
fullness_label = tk.Label(root, text = 'Сытость'+str(fullness_level//2)+'%', bg = 'darkblue',
                        fg = 'brown')
fullness_label.place(x=450, y=175)

cmd_sleep = tk.Button(root, text='Здоровый сон', width = 14, bg = 'aquamarine', command=sleep_rise)
cmd_sleep.place(x=550, y=352)

c.focus_set()
c.pack()

c.bind('<Motion>', show_happiness)
c.bind('<Leave>', hide_happiness)
c.bind('<Double-Button-1>', feeding)

root.after(1000, blink)
root.after(300, life_param)

root.mainloop()