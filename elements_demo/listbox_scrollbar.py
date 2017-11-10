import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        lb = tkinter.Listbox(master)
        lb.pack(side="left")
        sb = tkinter.Scrollbar(master)
        sb.pack(fill="y", side="left")
        lb.insert("end", *[i * i for i in range(200)])
        lb["yscrollcommand"] = sb.set
        sb["command"] = lb.yview


root = tkinter.Tk()
app = MyApp(master=root)
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass
