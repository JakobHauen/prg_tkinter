import tkinter

class MyApp(tkinter.Frame):

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)

        self.menuBar = tkinter.Menu(master)
        master.config(menu=self.menuBar)
        self.fillMenuBar()

        self.pack()

    def fillMenuBar(self):
        self.menuFile = tkinter.Menu(self.menuBar, tearoff=False)
        self.menuFile.add_command(label="Öffnen", command=self.handler)
        self.menuFile.add_command(label="Speichern", command=self.handler)
        self.menuFile.add_command(label="Speichern unter", command=self.handler)
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Beenden", command=self.quit)
        self.menuBar.add_cascade(label="Datei", menu=self.menuFile)

    """
    add_cascade([cnf][, **kw])
    Fügt ein Untermenü hinzu. Die tkinter.Menu- Instanz des Untermenüs muss für den Schlüssel- wortparameter menu angegeben werden. Über den Schlüsselwortparameter label kann die Beschriftung des Untermenüs bestimmt werden.
    
    add_checkbutton([cnf][, **kw])
    Fügt einen Checkbutton als Menüeintrag hinzu. Optionen für den Checkbutton, insbesondere label und command, können als Schlüsselwort- parameter übergeben werden.

    add_command([cnf][, **kw])
    Fügt einen einfachen Menüeintrag hinzu. Wich- tig sind hier die Optionen label für die Beschrif- tung und command für die Handler-Funktion.
    
    add_radiobutton([cnf][, **kw])
    Fügt einen Radiobutton als Menüeintrag hinzu. Optionen für den Radiobutton, insbesondere label und command, können als Schlüsselwort- parameter übergeben werden.

    add_separator([cnf][, **kw])
    Fügt eine Trennlinie ins Menü ein.
    
    
    delete(index1[, index2])
    Löscht den Menüeintrag an der Stelle index1 bzw. alle Menüeinträge zwischen den Stellen index1 und index2. Die Menüeinträge sind beginnend bei 0 aufsteigend durchnummeriert.

    entrycget(index, option)
    Gibt den Wert der Option option des Menüein- trags an der Stelle index zurück.

    entryconfig(index[, cnf][,**kw])
    Ruft die configure-Methode des Menüeintrags an der Stelle index mit den übergebenen Schlüs- selwortparametern auf.

    post(x, y)
    Zeigt das Menü an der Position an, die durch x und y bestimmt wird. Auf diese Weise lässt sich zum Beispiel ein Kontextmenü realisieren.
    Die Koordinaten x und y verstehen sich relativ zur oberen linken Ecke des Bildschirms.

    unpost()
    Versteckt das Menü wieder.
    """


    def handler(self):
        print("Hallo Welt!")


root = tkinter.Tk()
app = MyApp(master=root)
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass
