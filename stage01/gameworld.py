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

        self.draw_grid()
        self.maze = Maze(self.canvas)
        self.maze.setup_maze(self.maze.levels[1])
        
        hero_x = 18
        hero_y = 1
        self.hero = Hero(self.canvas, hero_x, hero_y)
        self.hero.move(self.hero.x, self.hero.y)
        
        self.canvas.bind("<Left>", self.hero.move_left)
        
        self.canvas.pack()
        self.pack()
        
        self.game_loop()
        self.canvas.focus_set()
        
    
    def game_loop(self):
        self.after(50, self.game_loop)
        

    def draw_grid(self):
        for i in range(0, self.width, 32):
            self.canvas.create_line(i, 0, i, self.height)
        for i in range(0, self.height, 32):
            self.canvas.create_line(0, i, self.width, i)
        


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
    
    def move(self, x, y):
        self.canvas.create_image(self.x*32, self.y*32, anchor = "nw", image = self.image)
        self.canvas.update()
    
    def move_left(self, x):
        self.x =- 1
        self.move(self.x, self.y)

class Maze(object):
    
    def __init__(self, canvas):
        self.canvas = canvas
        
        path = os.path.join(os.getcwd(), "images/wall.gif")
        # print(path)
        self.image = tk.PhotoImage(file = path)
    
        self.levels = [""]
    
        level_1 = ["####################",
                   "#        #         #",
                   "#######  #  ########",
                   "#     #  #         #",
                   "#     #  #  #####  #",
                   "#        #  #      #",
                   "# #####  #  #      #",
                   "#     #     #      #",
                   "#     ##############",
                   "### ###  #   #     #",
                   "#        #   #  #  #",
                   "#######  #      #  #",
                   "#     #  ########  #",
                   "#                  #",
                   "####################"
               ]
        
        self.levels.append(level_1)
    
    def setup_maze(self, level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                char = level[y][x]
                screen_x = (x*32)
                screen_y = (y*32)
                
                if char == "#":
                    self.canvas.create_image(screen_x, screen_y, anchor = "nw", image = self.image)
                    # print(screen_x, screen_y)
                    self.canvas.update()
        
    