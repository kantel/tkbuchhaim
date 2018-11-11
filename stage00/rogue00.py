import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
canvas = tk.Canvas(frame, width= 640, height = 480, bg = "#8d8741")
frame.pack()
canvas.pack()

root.title("Hello Rogue!")
root.mainloop()