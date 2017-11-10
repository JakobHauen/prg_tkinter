"""
Schnittstelle 	Bedeutung

w.winfo_geometry()	Gibt die Position und die Dimension des Widgets w in Form eines Strings zurück. Beachten Sie, dass die Position relativ zum übergeordneten Widget zu sehen ist. Der zurückgege- bene String hat die Form "BxH+X+Y", wobei B die Breite, H die Höhe, X die X-Position und Y die Y-Position des Widgets ist.

w.winfo_height()	Gibt die Höhe des Widgets w in Pixel zurück.

w.winfo_pointerx()	Gibt die X-Koordinate des Mauszeigers relativ zur oberen linken Ecke des Bildschirms zurück.

w.winfo_pointerxy()	Gibt ein Tupel bestehend aus den X- und Y-Koordinaten des Mauszeigers zurück.

w.winfo_pointery()	Gibt die Y-Koordinate des Mauszeigers relativ zur oberen linken Ecke des Bildschirms zurück.

w.winfo_reqheight()	Gibt die für das Widget w angeforderte Höhe zurück. Diese Methode ist beispielsweise direkt nach dem Instantiieren eines Widgets sinnvoll, da das Widget zu diesem Zeitpunkt möglicherweise noch nicht gepackt wurde und somit keine realen Dimensionen hat.

w.winfo_reqwidth()	Gibt die für das Widget w angeforderte Breite zurück.

w.winfo_rootx()	Gibt die X-Position des Widgets w relativ zur oberen linken Ecke des Bildschirms zurück.

w.winfo_rooty()	Gibt die Y-Position des Widgets w relativ zur oberen linken Ecke des Bildschirms zurück.

w.winfo_screenheight()	Gibt die Höhe des Bildschirms in Pixel zurück.

w.winfo_screenwidth()	Gibt die Breite des Bildschirms in Pixel zurück.

w.winfo_width()	Gibt die Breite des Widgets w in Pixel zurück.

w.winfo_x() 	Gibt die X-Koordinate des Widgets w relativ zum überge- ordneten Widget zurück.

w.winfo_y() 	Gibt die Y-Koordinate des Widgets w relativ zum überge- ordneten Widget zurück.

w.bind(event, func[, add])	Events an ein Objekt binden

w.bind_all(event, func[, add])	Wie bind, mit dem Unterschied aber, dass das Event event in allen Widgets der Applikation mit der Handler-Funktion func verbunden wird.

w.unbind(event[, funcid])	Löst alle existierenden Bindungen an das Event event auf. Über den Parameter funcid kann eine bestimmte Verbindung gezielt aufgelöst werden. Jede mit einem Event verbundene Handler-Funk- tion bekommt dazu eine ID zugeteilt, die beim Aufruf der Methode bind zurückgegeben wird.

w.unbind_all(event)	wie unbind, jedoch stets für alle Verbindungen an das Event event und alle Widgets der Applikation

w.cget(key) 	Gibt den Wert der Option key von w zurück. Die für das Widget w gültigen Optionen lassen sich über die Methode keys herausfinden.

w.configure([cnf][, **kw])	Setzt eine oder mehrere Optionen des Widgets w. Die Optionen können dabei als Dictionary über den Parameter cnf oder in Form von Schlüssel- wortparametern übergeben werden. Näheres zu Optionen finden Sie im Laufe dieses Abschnitts.

w.destroy() 	Zerstört das Widget w und alle ihm untergeordne- ten Widgets.

w.focus_set()	Gibt w den Eingabefokus. Wenn der Eingabefokus gerade nicht bei der Applikation liegt, wird er an w gegeben, sobald die Applikation ihn bekommt.

w.info() 	Gibt ein Dictionary zurück, das die Ausrichtungs- anweisungen an den Packer für w enthält.

w.keys() 	Gibt eine Liste aller für w gültigen Optionen zurück.

w.mainloop()	Startet die Hauptschleife des Widgets w. Von nun an übernimmt das Tk-Toolkit den Programmfluss. Die Methode mainloop blockiert so lange, bis die Anwendung beendet wurde.

w.pack([cnf][, **kw])	Instruiert den Packer des übergeordneten Wid- gets, das Widget w zu pakken. Dabei können die eingangs erwähnten Layoutanweisungen sowohl als Schlüsselwortparameter als auch in Form eines Dictionarys für den Parameter cnf übergeben werden.

w.quit() 	Zerstört alle Widgets und beendet die Applika- tion.

w.slaves() 	Gibt ein iterierbares Objekt über alle w unterge- ordneten Widgets zurück.



"""