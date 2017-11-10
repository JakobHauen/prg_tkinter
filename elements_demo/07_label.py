import tkinter

class MyApp(tkinter.Frame):


    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        label = tkinter.Label()
        label["text"] = "Hallo Welt"
        label.pack()



root = tkinter.Tk()
app = MyApp(master=root)
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass

