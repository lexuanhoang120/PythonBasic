from tkinter import *

from PIL import Image, ImageTk
from googletrans import Translator

# create the window
# set the frame of the window
window = Tk()
window.title("Google Translate")
window.geometry("500x630")
window.iconbitmap("logo.ico")

# set the background
image = Image.open("background.png")
render = ImageTk.PhotoImage(image)
img = Label(window, image=render)
img.place(x=0, y=0)

# create the label TRANSLATOR
name = Label(window, text="TRANSLATOR", fg="#ffffff", bd=0, bg="#031520")
# set the arrangement the widget
name.pack(side=TOP)
name.config(font=("Transformers Movie", 30))
# the distance from frame to the Label
name.pack(pady=10)

# create the box
box = Text(window, width=28, height=8, font=("Arial", 16))
# the distance from box to the label above
box.pack(pady=20)

# create the frame to contain the Button
button_frame = Frame(window).pack(side=BOTTOM)


def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)


def translate():
    box1.delete(1.0, END)
    inp = box.get(1.0, END)
    print(inp)
    t = Translator()
    a = t.translate(inp, src="vi", dest="en")
    b = a.text
    box1.insert(END, b)


# create the Button on the frame which is created previously. command is pointed to function above
clear_button = Button(button_frame, text="Clear text", font=("Arial", 10, "bold"), bg="#303030", fg="#ffffff",
                      command=clear)
clear_button.place(x=150, y=310)

trans_button = Button(button_frame, text="Translate", font=("Arial", 10, "bold"), bg="#303030", fg="#ffffff",
                      command=translate)
trans_button.place(x=290, y=310)

# create the box
box1 = Text(window, width=28, height=8, font=("Arial", 16))
# the distance from box to the label above
box1.pack(pady=50)
# keeping the window
window.mainloop()
