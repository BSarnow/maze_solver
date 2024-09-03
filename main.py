from window import Window, Point, Line, Cell
import time
import random

win = Window(800, 600)

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=False):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.matrix = self.create_cells()

    def create_cells(self):
        matrix = []
        for row in range(0,self.num_rows):
            cols = []
            for col in range(0, self.num_cols):
                col = Cell(
                    win.canvas_widget,
                    self.x1+self.cell_size_x*col,self.x1+self.cell_size_x*col+self.cell_size_x ,
                    self.y1+self.cell_size_y*row, self.y1+self.cell_size_y*row+self.cell_size_y)
                cols.append(col)
            matrix.append(cols)
        return matrix
    
    def draw_maze(self):
        for row in self.matrix:
            for cell in row:
                cell.draw()
                self.animated()

    def animated(self):
        win.rewdraw()
        #time.sleep(0.01)

    def break_entrance_and_exit(self):
        self.matrix[0][0].wall_top=False
        self.matrix[-1][-1].wall_bottem=False

    def false_ways(self, visited):
        for row in range(0, len(self.matrix)):
            for cell in range(0, len(self.matrix[row])):
                if (row, cell) not in visited:
                    if cell != 0 and row != 0 and cell != len(self.matrix[row])-1 and row != len(self.matrix)-1: # Alles außer rand
                        bottem = random.randint(0,8)
                        right = random.randint(0,8)
                        top = random.randint(0,8)
                        left = random.randint(0,8)
                        if bottem == 1 or bottem == 2: # bottem
                            self.matrix[row][cell].wall_bottem=False
                            if row+1 <= len(self.matrix):
                                self.matrix[row+1][cell].wall_top=False
                        if right == 1 or right == 2:
                            self.matrix[row][cell].wall_right=False
                            if cell+1 <= len(self.matrix[row]):
                                self.matrix[row][cell+1].wall_left=False
                        if left == 1 or left == 2:
                            self.matrix[row][cell].wall_left=False
                            if cell-1 >= 0:
                                self.matrix[row][cell-1].wall_right=False
                        if top == 1 or top == 2:
                            self.matrix[row][cell].wall_top=False
                            if row-1 >= 0:
                                self.matrix[row-1][cell].wall_bottem=False
                    elif row == 0 and cell != 0 and cell != len(self.matrix[row])-1: # oberer Rand
                        bottem = random.randint(0,8)
                        right = random.randint(0,8)
                        left = random.randint(0,8)
                        if bottem == 1 or bottem == 2: #bottem
                            self.matrix[row][cell].wall_bottem=False
                            if row+1 <= len(self.matrix):
                                self.matrix[row+1][cell].wall_top=False
                        if right == 1 or right == 2:
                            self.matrix[row][cell].wall_right=False
                            if cell+1 <= len(self.matrix[row]):
                                self.matrix[row][cell+1].wall_left=False
                        if left == 1 or left == 2:
                            self.matrix[row][cell].wall_left=False
                            if cell-1 >= 0:
                                self.matrix[row][cell-1].wall_right=False
                    elif cell == 0 and row != 0 and row != len(self.matrix)-1: #linker Rand
                        bottem = random.randint(0,8)
                        right = random.randint(0,8)
                        top = random.randint(0,8)
                        if bottem == 1 or bottem == 2: # bottem
                            self.matrix[row][cell].wall_bottem=False
                            if row+1 <= len(self.matrix):
                                self.matrix[row+1][cell].wall_top=False
                        if right == 1 or right == 2:
                            self.matrix[row][cell].wall_right=False
                            if cell+1 <= len(self.matrix[row]):
                                self.matrix[row][cell+1].wall_left=False
                        if top == 1 or top == 2:
                            self.matrix[row][cell].wall_top=False
                            if row-1 >= 0:
                                self.matrix[row-1][cell].wall_bottem=False
                    elif cell != 0 and cell != len(self.matrix[row])-1 and row == len(self.matrix)-1: #unterer Rand
                        left = random.randint(0,8)
                        right = random.randint(0,8)
                        top = random.randint(0,8)
                        if left == 1 or left == 2:
                            self.matrix[row][cell].wall_left=False
                            if cell-1 >= 0:
                                self.matrix[row][cell-1].wall_right=False
                        if right == 1 or right == 2:
                            self.matrix[row][cell].wall_right=False
                            if cell+1 <= len(self.matrix[row]):
                                self.matrix[row][cell+1].wall_left=False
                        if top == 1 or top == 2:
                            self.matrix[row][cell].wall_top=False
                            if row-1 >= 0:
                                self.matrix[row-1][cell].wall_bottem=False
                    elif row != 0 and cell == len(self.matrix[row])-1 and row != len(self.matrix)-1: # rechter Rand
                        bottem = random.randint(0,8)
                        top = random.randint(0,8)
                        left = random.randint(0,8)
                        if bottem == 1 or bottem == 2: # bottem
                            self.matrix[row][cell].wall_bottem=False
                            if row+1 <= len(self.matrix):
                                self.matrix[row+1][cell].wall_top=False
                        if left == 1 or left == 2:
                            self.matrix[row][cell].wall_left=False
                            if cell-1 >= 0:
                                self.matrix[row][cell-1].wall_right=False
                        if top == 1 or top == 2:
                            self.matrix[row][cell].wall_top=False
                            if row-1 >= 0:
                                self.matrix[row-1][cell].wall_bottem=False

    def right_way(self):
        visited = []
        row = 0
        cell = 0
        safe_point = []
        count = 0
        current_cell = self.matrix[row][cell]
        while current_cell != self.matrix[-1][-1]:
            possible_ways = []
            if row-1 >= 0:
                if (row-1, cell) not in visited: #up
                    possible_ways.append(0)
            if cell+1 <= len(self.matrix[row])-1:
                if (row, cell+1) not in visited: #right
                    possible_ways.append(1)
            if row+1 <= len(self.matrix)-1:
                if (row+1, cell) not in visited: #down
                    possible_ways.append(2)
            if cell-1 >= 0:
                if (row, cell-1) not in visited: #left
                    possible_ways.append(3)
            if len(possible_ways) == 3:
                safe_point.clear()
                safe_point.append(row)
                safe_point.append(cell)
            if len(possible_ways) == 0:
                count += 1
                row = visited[-(count)][0]
                cell = visited[-(count)][1]
                current_cell = self.matrix[row][cell]
            else:
                go = possible_ways[random.randint(0,len(possible_ways)-1)]
                if go == 0:
                    current_cell.wall_top = False
                    self.matrix[row-1][cell].wall_bottem = False
                    row -= 1
                    count = 0
                    visited.append((row, cell))
                    current_cell = self.matrix[row][cell]
                if go == 1:
                    current_cell.wall_right = False
                    self.matrix[row][cell+1].wall_left = False
                    cell += 1
                    count = 0
                    visited.append((row, cell))
                    current_cell = self.matrix[row][cell]
                if go == 2:
                    current_cell.wall_bottem = False
                    self.matrix[row+1][cell].wall_top = False
                    row += 1
                    count = 0
                    visited.append((row, cell))
                    current_cell = self.matrix[row][cell]
                if go == 3:
                    current_cell.wall_left = False
                    self.matrix[row][cell-1].wall_right = False
                    cell -= 1
                    count = 0
                    visited.append((row, cell))
                    current_cell = self.matrix[row][cell]
        self.false_ways(visited)

    def solve(self):
        row = 0
        cell = 0
        visited = []
        dead_end = []
        wrong_way = 1
        while self.matrix[row][cell] != self.matrix[-1][-1]:
            if (row,cell) not in visited:
                visited.append((row,cell))
            way = self.solve_r(row,cell, visited)
            if way == False:
                wrong_way += 1
                start_point = Point(self.matrix[row][cell].most_left + (self.cell_size_x/2), self.matrix[row][cell].most_top + (self.cell_size_y/2))
                print(f"I´m at {row} {cell}")
                dead_end.append((row,cell))
                if (visited[-wrong_way][0],visited[-wrong_way][1]) in dead_end:
                    print(f"I can´t go to {(visited[-wrong_way][0],visited[-wrong_way][1])} it´s a dead end")
                else:
                    row = visited[-wrong_way][0]
                    cell = visited[-wrong_way][1]
                    print(f"I´m stucked. I´m want to go to {row} {cell}")
                    end_point = Point(self.matrix[row][cell].most_left + (self.cell_size_x/2), self.matrix[row][cell].most_top + (self.cell_size_y/2))
                    path_line = Line(start_point,end_point)
                    path_line.draw(win.canvas_widget, "grey")
            if way != False:
                row = way[0][0]
                cell = way[0][1]
                wrong_way=1
                path_line = Line(way[1], way[2])
                path_line.draw(win.canvas_widget, "red")
        print("I found the finish")    

    def solve_r(self, row, cell, visited=[]):
            possible_ways = []
            start_point = Point(self.matrix[row][cell].most_left+(self.cell_size_x/2), self.matrix[row][cell].most_top+(self.cell_size_y/2))
            if row-1 >=0:
                if self.matrix[row-1][cell].wall_bottem == False:
                    if (row-1, cell) not in visited:
                        possible_ways.append((row-1, cell))
            if cell+1 <= len(self.matrix[row])-1:
                if self.matrix[row][cell+1].wall_left == False:
                    if (row, cell+1) not in visited:
                        possible_ways.append((row, cell+1))
            if row+1 <= len(self.matrix)-1:
                if self.matrix[row+1][cell].wall_top == False:
                    if (row+1, cell) not in visited:
                        possible_ways.append((row+1, cell))
            if cell -1 >= 0:
                if self.matrix[row][cell-1].wall_right == False:
                    if (row, cell-1) not in visited:
                        possible_ways.append((row, cell-1))
            if len(possible_ways) == 0:
                return False
            if len(possible_ways) > 0:
                end_point = Point(self.matrix[possible_ways[0][0]][possible_ways[0][1]].most_left + (self.cell_size_x/2), self.matrix[possible_ways[0][0]][possible_ways[0][1]].most_top + (self.cell_size_y/2))
                return possible_ways[0], start_point, end_point
                

            
            

            

       
            
        
            


    
def main():
    test_maze = Maze(50,50,70,70,5,5)
    test_maze.break_entrance_and_exit()
    test_maze.right_way()
    test_maze.draw_maze()
    time.sleep(2)
    test_maze.solve()
    win.wait_for_close()

main()