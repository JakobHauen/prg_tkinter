import tkinter as tk
#from tkinter import ttk #just for MACs

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World (click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")



        """
        STEUERELEMENTVARIABLEN
        tkinter kennt folgende Steuerelementvariablen um einen Datenaustausch zwischen Programm und Oberfläche durchzuführen:
        
        tkinter.BooleanVar()
        tkinter.DoubleVar()
        tkinter.IntVar()
        tkinter.StringVar()
        
        diese Datentypen erben von der Basisklasse tkinter.Variable und sind wie folgt aufgebaut
        
        Variable([master[,value[,name]]])
        
        master = Hier wird das master-Widget angegeben, falls man mehrere parallel verwendet - optional
        value = Der Wert für die Variable, wobei die Datentypprüfung erst beim var.get() einen Fehler wirft - optional
        name = Der interne Name in Tcl - wird normal nicht manuell gesetzt und folgt dem Muster PY_VAR<n> 
        
        """
        self.myString = tk.StringVar(value="Blub")
        self.getText = tk.Button(self, text="Print Text", command=self.get_string)
        self.getText.pack(side="right")
        self.setText = tk.Button(self, text="set Text", command=self.set_string)
        self.setText.pack(side="right")


        """
<<<<<<< HEAD
        Der PACKER 
=======
        Der PACKER
>>>>>>> layout_demos
        Es ist wichtig die hirarchie zu kennen um zu verstehen wie die Elemente automatisch angeordnet werden:
        
                         --------
                        |   TK   |
                        |  root  |
                        |________|
                             |
                             |
                        -----------
                       |   Frame   |
                       |    app    |
                       |___________|
                            /|\
                            
                        /    |     \
                            
                     /       |            \
                           
                /            |                     \
         1----------         2----------         3----------
        |   Button  |       |   Button  |       |   Button  |
        | hi_there  |       |  getText  |       |  setText  |
        |___________|       |___________|       |___________|
        
<<<<<<< HEAD
        
        Der Branch "layout_demos" hat einige Beispiele für Layoutoptionen         
=======
                 
>>>>>>> layout_demos
        """

        #ttk.Style().configure('red.TButton', foreground='red') #just for MACs
        #self.quit = ttk.Button(self, text="QUIT", style='red.TButton',fg="red", command=root.destroy) #just for MACs

        self.quit = tk.Button(self, text="QUIT", highlightbackground='#aa3311', fg="red", command=root.destroy)

        self.quit.pack(side="bottom")

    def get_string(self):
        print(self.myString.get())

    def set_string(self):
        self.myString.set("Hallo Welt")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()