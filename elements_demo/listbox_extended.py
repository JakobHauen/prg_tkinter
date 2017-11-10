import tkinter

class MyApp(tkinter.Frame):
    def selectionChanged(self, event):
        self.label["text"] = "Wir fahren nach: " + ", ".join(
            (self.lb.get(i) for i in self.lb.curselection()))

    def __init__(self, master=None):

        tkinter.Frame.__init__(self, master)
        self.pack()
        self.eintraege = ["Berlin", "London", "Moskau", "Ottawa", "Paris", "Rom", "Tokio", "Washington DC"]

        self.lb = tkinter.Listbox(self)
        self.lb.pack(fill="both", expand="true")
        self.lb["selectmode"] = "extended"
        self.lb.insert("end", *self.eintraege)
        self.lb.bind("<<ListboxSelect>>", self.selectionChanged)
        self.lb.selection_set(0)
        self.label = tkinter.Label(self)
        self.label.pack()
        self.selectionChanged(None)

    def selectionChanged(self, event):
        self.label["text"] = "Wir fahren nach: " + ", ".join(
            (self.lb.get(i) for i in self.lb.curselection()))


root = tkinter.Tk()
app = MyApp(master=root)
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass
