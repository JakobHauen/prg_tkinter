import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
            tkinter.Frame.__init__(self, master)
            self.pack()
            group = tkinter.LabelFrame(master, text="Entenhausen")
            c1 = tkinter.Checkbutton(group, text="Donald Duck")
            c1.pack(anchor="w")
            c2 = tkinter.Checkbutton(group, text="Dagobert Duck")
            c2.pack(anchor="w")
            c3 = tkinter.Checkbutton(group, text="Gustav Gans")
            c3.pack(anchor="w")
            group.pack()


root = tkinter.Tk()
app = MyApp(master=root)
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass

