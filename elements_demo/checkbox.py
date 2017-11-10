import tkinter

class MyApp(tkinter.Frame):


    def __init__(self, master=None):
            tkinter.Frame.__init__(self, master)
            self.pack()
            self.auswahl = ["Berlin", "London", "Moskau", "Ottawa",
                       "Paris", "Rom", "Tokio", "Washington DC"]
            self.var = tkinter.StringVar()
            self.var.set("Moskau")
            for a in self.auswahl:
                b = tkinter.Radiobutton(master, text=a, value=a, variable=self.var, command=self.show(a))
                b.pack(anchor="w")

    def show(self,value):
        print(value)


root = tkinter.Tk()
app = MyApp(master=root)
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass

