"""
Der Place-Geometrie-Manager erlaubt das explizite Setzen der Position und der Größe eines Fenster, entweder in absoluten Werten oder relativ zu anderen Widgets. Der Place-Manager kann über die place-Methode benutzt werden. Er kann auf alle Standart-Widgets angewendet werden. 

Im folgenden Beispiel benutzen wir den Place-Geometrie-Manager. Wir spielen mit Farben in diesem Beispiel, d.h. wir ordnen jedem Label eine andere Farbe zu, die wir zufällig mit der randrange-Methode aus dem random-Modul erzeugen. Wir berechnen den Grauwert (die Helligkeit, brightness) von jeder Farbe. Falls die Helligkeit kleiner als 120 ist, setzen wir die Vordergrundfarbe (fg) des Labels auf weiß andernfalls auf schwarz. Dadurch lässt sich der Text leichter lesen.

"""
import tkinter as tk
import random
    
root = tk.Tk()
# width x height + x_offset + y_offset:
root.geometry("170x200+30+30") 
     
languages = ['Python','Perl','C++','Java','Tcl/Tk']
labels = range(5)
for i in range(5):
   ct = [random.randrange(256) for x in range(3)]
   brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
   ct_hex = "%02x%02x%02x" % tuple(ct)
   bg_colour = '#' + "".join(ct_hex)
   l = tk.Label(root, 
                text=languages[i], 
                fg='White' if brightness < 120 else 'Black', 
                bg=bg_colour)
   l.place(x = 20, y = 30 + i*30, width=120, height=25)
          
root.mainloop()
