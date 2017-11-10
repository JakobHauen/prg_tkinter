import tkinter

class MyApp(tkinter.Frame):


    def __init__(self, master=None):
            tkinter.Frame.__init__(self, master)
            self.pack()
            text = tkinter.Text(self.master)
            text.pack()
            text.tag_config("o", foreground="orange")
            text.tag_config("u", underline=True)
            text.insert("end", "Hallo Welt\n")
            text.insert("end", "Dies ist ein langer, oranger Text\n", "o")
            text.insert("end", "Und unterstrichen ebenfalls", "u")


root = tkinter.Tk()
app = MyApp(master=root)
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass

