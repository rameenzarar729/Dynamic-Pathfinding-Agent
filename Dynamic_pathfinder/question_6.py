import tkinter as tk
from tkinter import simpledialog, messagebox
import heapq
import random
import time


COLOR_FRONTIER = "yellow"  
COLOR_VISITED = "red"    
COLOR_PATH = "green"      
COLOR_OBSTACLE = "black"

class DynamicAgent:
    def __init__(self, root, rows, cols, density):
        self.root = root
        self.rows, self.cols = rows, cols
        self.density = density / 100
        self.cell_size = 25
        
        self.start, self.goal = (0, 0), (rows-1, cols-1)
        self.obstacles = set()
        self.agent_pos = self.start
        self.is_moving = False
        
        self.setup_ui()
        self.generate_random_map()

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=self.cols*self.cell_size, height=self.rows*self.cell_size)
        self.canvas.pack()
     
        self.canvas.bind("<Button-1>", self.toggle_wall)
        
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()
        tk.Button(btn_frame, text="Start Navigation", command=self.start_sim).pack(side=tk.LEFT)
        self.status = tk.Label(self.root, text="Click cells to add/remove walls manually")
        self.status.pack()

    def generate_random_map(self):
    
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in [self.start, self.goal] and random.random() < self.density:
                    self.obstacles.add((r, c))
        self.draw_all()

    def toggle_wall(self, event):

        c, r = event.x // self.cell_size, event.y // self.cell_size
        node = (r, c)
        if node not in [self.start, self.goal]:
            if node in self.obstacles: self.obstacles.remove(node)
            else: self.obstacles.add(node)
            self.draw_all()

    def get_h(self, n):
   
        return abs(n[0] - self.goal[0]) + abs(n[1] - self.goal[1])

    def a_star(self, start_node):

        frontier = []
        heapq.heappush(frontier, (0, start_node))
        came_from = {start_node: None}
        g_score = {start_node: 0}
        expanded_count = 0

        while frontier:
            curr = heapq.heappop(frontier)[1]
            expanded_count += 1
            if curr == self.goal: break

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nb = (curr[0]+dr, curr[1]+dc)
                if 0 <= nb[0] < self.rows and 0 <= nb[1] < self.cols and nb not in self.obstacles:
                    new_g = g_score[curr] + 1
                    if nb not in g_score or new_g < g_score[nb]:
                        g_score[nb] = new_g
                        f = new_g + self.get_h(nb)
                        heapq.heappush(frontier, (f, nb))
                        came_from[nb] = curr
                        self.paint_node(nb, COLOR_FRONTIER)
        
        path = []
        temp = self.goal
        while temp in came_from and temp != start_node:
            path.append(temp)
            temp = came_from[temp]
        return path[::-1], expanded_count

    def start_sim(self):
        self.is_moving = True
        self.move_loop()

    def move_loop(self):
        if not self.is_moving or self.agent_pos == self.goal:
            return


        path, visited = self.a_star(self.agent_pos)
        if not path:
            messagebox.showinfo("Error", "No Path Found!")
            return

      
        next_step = path[0]
        
   
        if random.random() < 0.1: 
            obs = (random.randint(0, self.rows-1), random.randint(0, self.cols-1))
            if obs not in [next_step, self.goal, self.agent_pos]:
                self.obstacles.add(obs)
                self.paint_node(obs, COLOR_OBSTACLE)
                
              
                if obs in path:
                    self.status.config(text="Obstacle detected on path! Re-planning...")
                    self.root.after(200, self.move_loop)
                    return

        self.agent_pos = next_step
        self.paint_node(next_step, COLOR_PATH)
        self.status.config(text=f"Moving... Path Cost: {len(path)}")
        self.root.after(100, self.move_loop)

    def draw_all(self):
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                color = "white"
                if (r,c) in self.obstacles: color = COLOR_OBSTACLE
                elif (r,c) == self.start: color = "blue"
                elif (r,c) == self.goal: color = "purple"
                self.paint_node((r,c), color)

    def paint_node(self, node, color):
        r, c = node
        self.canvas.create_rectangle(c*self.cell_size, r*self.cell_size, (c+1)*self.cell_size, (r+1)*self.cell_size, fill=color)

root = tk.Tk()
root.withdraw()
R = simpledialog.askinteger("Input", "Grid Rows:", initialvalue=20)
C = simpledialog.askinteger("Input", "Grid Columns:", initialvalue=20)
D = simpledialog.askinteger("Input", "Wall Density %:", initialvalue=25)

if R and C:
    root.deiconify()
    app = DynamicAgent(root, R, C, D)
    root.mainloop()