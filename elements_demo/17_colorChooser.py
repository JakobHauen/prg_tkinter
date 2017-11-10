import tkinter, tkinter.colorchooser
master = tkinter.Tk()
cv = tkinter.Canvas(master, width=100, height=40)
cv.pack()
color = "#FF0000"
colorFrame = cv.create_rectangle(0, 0, 100, 40, fill=color, width=0)

def changeColor():
    global color, colorFrame
    res = tkinter.colorchooser.askcolor(color)
    if res[1]:
            color = res[1]
            cv.itemconfig(colorFrame, fill=color)


b = tkinter.Button(master, text="Farbe ändern",
                               command=changeColor)
b.pack()

master.mainloop()