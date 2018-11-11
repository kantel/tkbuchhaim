import tkinter as tk
import os



root = tk.Tk()
root.title("Rogue Stage 1")

cw, ch = 640, 480
canvas = tk.Canvas(root, width = cw, height = ch, bg = "royalblue")
canvas.grid(row = 0, column = 0)

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
# Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
# und os.path.join()
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

rogue = tk.PhotoImage(file = "../images/hildegunst.gif")
canvas.create_image(cw//2, ch//2, anchor = tk.NW, image = rogue)
canvas.update()

root.mainloop()

