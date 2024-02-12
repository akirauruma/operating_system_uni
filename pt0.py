from guizero import App, Text, TextBox, PushButton, Slider, Picture, Box
from tkinter import colorchooser
import random

app = App(title="TextBox")
panel = Box(app, layout="grid")
text_cox = Text(panel, text="Гуд ивнинг", size=60, font="Ubuntu", color="#9F70FD", grid=[0, 0])
textbox_cox = TextBox(panel, width=30, hide_text=False, grid=[0, 6])
textbox2 = TextBox(panel, width=30, hide_text=False, grid=[0, 7])
textbox3 = TextBox(panel, width=30, hide_text=False, grid=[1, 7])


def say_my_name():
    text_cox.value = textbox_cox.value


button = PushButton(panel, command=say_my_name, text="Do u like this?", grid=[0, 2])


def change_text_size(slider_value):
    text_cox.size = slider_value


slider = Slider(panel, command=change_text_size, start=10, end=100, grid=[0, 3])


def change_text_color():
    color = colorchooser.askcolor()[1]
    text_cox.text_color = color


def multiply_x2():
    try:
        number = float(textbox_cox.value)
        result = number ** 2 - 3 + number
        text_cox.value = str(result)
    except ValueError:
        text_cox.value = "Error: Enter number"


multiply_button = PushButton(panel, command=multiply_x2, width=100, text="x^2-3+x", grid=[0, 5])

color_button = PushButton(panel, command=change_text_color, text="Change", grid=[0, 4])

pic = Picture(panel, image="pt0.gif", grid=[0, 1])


def on_mouse_enter_textbox2(event):
    textbox2_enter()


def on_mouse_leave_textbox2(event):
    textbox2_leave()


def on_mouse_enter_textbox3(event):
    textbox3_enter()


def on_mouse_leave_textbox3(event):
    textbox3_leave()


def textbox2_enter():
    textbox2.value = "Пришёл"
    textbox3.value = "Ушёл"


def textbox2_leave():
    textbox2.value = ""
    textbox3.value = ""


def textbox3_enter():
    textbox3.value = "Пришел"
    textbox2.value = "Ушёл"


def textbox3_leave():
    textbox3.value = ""
    textbox2.value = ""


def change_background_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    app.bg = color


def on_mouse_move(event_data):
    change_background_color()


app.when_mouse_moved = on_mouse_move

textbox2.tk.bind("<Enter>", on_mouse_enter_textbox2)
textbox2.tk.bind("<Leave>", on_mouse_leave_textbox2)
textbox3.tk.bind("<Enter>", on_mouse_enter_textbox3)
textbox3.tk.bind("<Leave>", on_mouse_leave_textbox3)

app.display()
