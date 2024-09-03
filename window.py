from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas_widget = Canvas(self.root, bg="white", width=width, height=height)
        self.canvas_widget.pack(fill=BOTH, expand=1)
        self.running = False

    def rewdraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.rewdraw()
        print("window closed...")

    def close(self):
        self.running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self,canvas, lowestx, highestx, lowesty, highesty):
        self.wall_top = True
        self.wall_right = True
        self.wall_bottem = True
        self.wall_left = True
        self.most_left = lowestx
        self.most_right = highestx
        self.most_top = lowesty
        self.most_bottem = highesty
        self.win = False
        self.canvas = canvas

    def draw(self):
        point_NW= Point(self.most_right, self.most_top)
        point_NE= Point(self.most_left, self.most_top)
        point_SW= Point(self.most_right, self.most_bottem)
        point_SE= Point(self.most_left, self.most_bottem)
        if self.wall_top:
            top_wall = Line(point_NE, point_NW)
            top_wall.draw(self.canvas)
        if self.wall_left:
            left_wall = Line(point_NE, point_SE)
            left_wall.draw(self.canvas)
        if self.wall_right:
            right_wall = Line(point_NW, point_SW)
            right_wall.draw(self.canvas)
        if self.wall_bottem:
            bottem_wall = Line(point_SE, point_SW)
            bottem_wall.draw(self.canvas)

    def draw_move(self, to_cell, undo=False):
        x_point1 = self.most_left + ((self.most_right-self.most_left)/2)
        y_point1 = self.most_top +((self.most_bottem-self.most_top)/2)
        x_point2 = to_cell.most_left + ((to_cell.most_right-to_cell.most_left)/2)
        y_point2 = to_cell.most_top +((to_cell.most_bottem-to_cell.most_top)/2)
        color = "red"
        if undo != False:
            color = "grey"
        path = Line(Point(x_point1,y_point1), Point(x_point2,y_point2))
        path.draw(self.canvas, color)
    
