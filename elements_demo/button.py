import tkinter

class MyApp(tkinter.Frame):
    def helloWorld(self):
        print('Hallo Welt')

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        b = tkinter.Button(master)
        b["text"] = "Klick mich"
        b["command"] = self.helloWorld
        b.pack()

        """
        justify 	"left", "center", "right" 	
        Legt bei einem Button mit mehrzeili- ger Beschriftung die Ausrichtung der Textzeilen zueinander fest. 
		
        overrelief 	"raised", "sunken", "flat", "ridge", "solid", "groove" 	
        Legt die Darstellungsart des Buttons fest, wenn sich der Mauszeiger über ihm befindet. 
				
        padx 	int 	
        Legt das Padding in X-Richtung fest. 
		
        pady 	int 	
        Legt das Padding in Y-Richtung fest. 
		
        relief 	"raised", "sunken", "flat", "ridge", "solid", "groove" 	
        Legt die Darstellungsart des Buttons fest. 
				
        state 	"normal", "active", "enabled", "disabled" 	
        Setzt den Status des Buttons. Die Sta- tus enabled und normal sind synonym und bezeichnen den Normalzustand eines Buttons. Im disabled-Zustand ist der Button für den Benutzer nicht bedienbar. An der Benutzeroberfläche ist der Button dann grau hinterlegt. 
		
		
        takefocus 	bool 	
        Legt fest, ob der Button den Fokus bekommen soll, wenn der Benutzer mit der (ÿ)-Taste die Widgets des Dialogs durchschaltet. 
		
        text 	str 	
        Setzt die Beschriftung des Buttons. 
		
		
		
		
		
		
        Option 	Wertebereich 	Bedeutung 
		
        textvariable	StringVar 	Setzt eine Steuerelementvariable für die Beschriftung des Buttons. 
		Die Verwendung dieser Variablen funktioniert analog zum Entry-Widget, für das sie bereits im einführenden Bei- spielprogramm demonstriert wurde. 
        
        width 	int 	Legt die Breite des Buttons fest. Die Breite wird dabei in Zeichen angege- ben. 
		
        """

root = tkinter.Tk()
app = MyApp(master=root)
while True:
    try:
        app.mainloop()
        break
    except UnicodeDecodeError:
        pass
