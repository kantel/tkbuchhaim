import tkinter as tk
import os

class GameWorld(tk.Frame):
    
    def __init__(self, master):
        super(GameWorld, self).__init__(master)
        self.width = 640
        self.height = 480
        self.bg = "#2b3e50"
        self.canvas = tk.Canvas(self, bg = self.bg, width = self.width,
                                height = self.height)
        self.hero = Hero(self.canvas, self.width/2, self.height/2)
        self.maze = Maze(self.canvas)
        self.maze.setup_maze(self.maze.levels[1])
        self.hero.move()
        self.canvas.pack()
        self.pack()

class Sprite(object):
    
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
    
    def move(self):
        pass

class Hero(Sprite):
    
    def __init__(self, canvas, x, y):
        super(Hero, self).__init__(canvas, x, y)
        
        path = os.path.join(os.getcwd(), "images/hildegunst.gif")
        print(path)
        self.image = tk.PhotoImage(file = path)
    
    def move(self):
        self.canvas.create_image(self.x, self.y, anchor = "center", image = self.image)
        self.canvas.update()

class Maze(object):
    
    def __init__(self, canvas):
        self.canvas = canvas
        
        path = os.path.join(os.getcwd(), "images/wall.gif")
        print(path)
        self.image = tk.PhotoImage(file = path)
    
        self.levels = [""]
    
        level_1 = ["####################",
                   "#                  #",
                   "#                  #",
                   "#                  #",
                   "#                  #",
                   "#                  #",
                   "#                  #",
                   "#                  #",
                   "#                  #",
                   "#                  #",
                   "#                  #",
                   "#                  #",
                   "#                  #",
                   "#                  #",
                   "####################"
               ]
        
        self.levels.append(level_1)
    
    def setup_maze(self, level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                char = level[y][x]
                screen_x = x + (x*32)
                screen_y = y + (y*32)
                
                if char == "#":
                    self.canvas.create_image(screen_x + 16, screen_y + 16, image = self.image)
                    self.canvas.update()
        
    