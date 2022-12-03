import numpy as np
import tkinter as tk
from interpolation import lagrange_interpolate

DRAG_MIN_RADIUS = 15

def distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class Canvas(tk.Canvas):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.focus_set()
        self.width = width
        self.height = height
        self.bind('<Button-1>', self.click)
        self.bind('<ButtonRelease-1>', self.stop_dragging)
        self.bind('<B1-Motion>', self.click)
        self.bind('<Button-3>', self.delete_point)
        self.bind('<Key>', self.key_press)
        self.points_x = []
        self.points_y = []
        self.point_ids = []
        self.point_radius = 5
        self.point_color = 'red'
        self.line_color = "blue"
        self.dragging = False
        self.dragging_point = None

    def add_point(self, x, y):
        self.points_x.append(x)
        self.points_y.append(y)
        self.point_ids.append(self.create_oval(x - self.point_radius, y - self.point_radius, x + self.point_radius, y + self.point_radius, fill=self.point_color))

    def move_point(self, x, y):
        self.points_x[self.dragging_point] = x
        self.points_y[self.dragging_point] = y
        self.coords(self.point_ids[self.dragging_point], x - self.point_radius, y - self.point_radius, x + self.point_radius, y + self.point_radius)
        self.update_interpolation()

    def click(self, event):
        x = event.x
        y = event.y
        
        if self.dragging:
            self.move_point(x, y)
            return
        
        for i, point_id in enumerate(self.point_ids):
            if point_id == self.find_closest(x, y)[0]:
                if distance(x, y, self.points_x[i], self.points_y[i]) < DRAG_MIN_RADIUS:
                    self.dragging = True
                    self.dragging_point = i
                    return
            
        self.add_point(x, y)
                
        self.update_interpolation()
    
    def stop_dragging(self, event):
        self.dragging = False
        self.dragging_point = None

    def delete_point(self, event):
        x = event.x
        y = event.y
        for i, point_id in enumerate(self.point_ids):
            if point_id == self.find_closest(x, y)[0]:
                self.points_x.pop(i)
                self.points_y.pop(i)
                self.delete(point_id)
                self.point_ids.pop(i)
                break
        self.update_interpolation()
    
    def key_press(self, event):
        if event.char == 'c':
            self.clear()
        elif event.char == 'q':
            self.quit()

    def clear(self):
        for point_id in self.point_ids:
            self.delete(point_id)
        self.points_x = []
        self.points_y = []
        self.point_ids = []
        self.update_interpolation()

    def update_interpolation(self):
        self.delete('interpolation')
        if len(self.points_x) > 1:
            P = lagrange_interpolate(self.points_x, self.points_y)
            x = np.linspace(0, self.width, 1000)
            y = P(x)
            for i in range(len(x) - 1):
                self.create_line(x[i], y[i], x[i + 1], y[i + 1], fill=self.line_color, tags='interpolation')
    

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Lagragian Polynomial Interpolation')
    canvas = Canvas(window, 800, 600)
    canvas.pack()
    window.mainloop()