import tkinter

class MyApp(tkinter.Frame):


    def __init__(self, master=None):
            tkinter.Frame.__init__(self, master)
            self.pack()
            entry = tkinter.Entry()
            entryVar = tkinter.StringVar()
            entryVar.set("Hallo Welt")
            entry["textvariable"] = entryVar
            entry.pack()
            #entry.["show"]="*"
            """
            show: Legt ein Zeichen fest, das bei einer Eingabe des Benutzers statt des tat- sächlich eingegebenen Textes ange- zeigt werden soll. Diese Option ist beispielsweise für Passworteingaben interessant.
            textvariable: Setzt eine Steuerelementvariable, über die auf den im Eingabefeld ange- zeigten Text lesend und schreibend zugegriffen werden kann.
            """


root = tkinter.Tk()
app = MyApp(master=root)
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass

