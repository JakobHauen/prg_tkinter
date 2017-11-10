import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        s = tkinter.Spinbox()
        s["from"] = 0
        s["to"] = 100
        s.pack()

        s = tkinter.Spinbox(self.master)
        s["values"] = (2, 3, 5, 7, 11, 13, 19)
        s.pack()

        s = tkinter.Spinbox(self.master)
        s["values"] = ("A", "B", "C")
        s.pack()

        """
        format        "%pad1.pad2f"
        Legt die Formatierung der Ausgabe fest. Dabei bezeichnet pad1 die Anzahl der für den Vor- kommaanteil reservierten Ziffern und pad2 die Zahl der darzustellenden Nachkommastellen.
        
        from        float
        untere Grenze für den in der Spinbox darge- stellten Wert
        
        increment        float
        Legt den Wert fest, um den der Wert bei einem Klick auf die kleinen Buttons der Spin- box inkrementiert bzw. dekrementiert werden soll.
        
        to        float
        obere Grenze für den in der Spinbox darge- stellten Wert
        
        values        tuple, list
        Legt die möglichen Werte der Spinbox konkret fest.
        
        xscrollcommand
        Funktionsobjekt Möglichkeit zur Anbindung eine horizontalen Scrollbar. 
        
        """

root = tkinter.Tk()
app = MyApp(master=root)
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass
