from tkinter import *


def clean():
    c.delete("all")

def save():
    file = open("drawing.jpeg", "w")
    file.write(c)
    file.close()
    c.delete("all")

def painter(event):
    paint = colors.get()
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y - 1)
    hello = c.create_line(x1, y1, x2, y2, width = sizes.get())
    c.itemconfig(hello, fill = paint)

root = Tk()
screen = root

#------Title of screen-----#
screen.title("Drawing board")
screen.geometry("700x500")
screen.iconbitmap('helo.jpg')

#-------Label for the buttons---------#
Label(screen, bg = "grey", height = "10", width = "700").place(x = 0, y = 0)

#----------Brush Size---------#
size_list = [
    "5", "10",
    "15", "20",
    "25", "30",
    "35", "40"
]
sizes = StringVar()
sizes.set(size_list[0])
brush_size = OptionMenu(screen, sizes, *size_list).place(x = 30, y = 20)

#-----------Eraser Button----------#
eraser_button = Button(text = "Eraser", bg = "grey", fg = "black", command = clean).place(x = 200, y = 20)

#----------Color Pallette-----------#
color_list = [
    "Red", "Blue",
    "Green", "Black",
    "Yellow", "Orange"
]
colors = StringVar()
colors.set(color_list[0])
color = OptionMenu(screen, colors, *color_list).place(x = 370, y = 20)

#------------Save Button-------------#
Button(screen, text = "Save", bg = "grey", fg = "black", command = save).place(x = 600, y = 20)

##---------Canvas Layout-----------------
c = Canvas(screen, width = "700", height = "450")
c.pack(side = BOTTOM)
c.bind("<B1-Motion>", painter)


screen.mainloop()


