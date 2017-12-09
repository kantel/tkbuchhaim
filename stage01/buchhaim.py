# Buchhaim Stage 1
# Basic Roguelike

import tkinter as tk
from gameworld import GameWorld

def main():
    root = tk.Tk()
    root.title("In den Labyrinthen von Buchhaim")
    gameworld = GameWorld(root)
    gameworld.mainloop()

if __name__ == "__main__":
    main()
    