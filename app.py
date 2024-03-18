from tkinter import Tk,BOTH,Canvas
import random,time

class Window:
    def __init__(self,width,height,title):
        self.height = height
        self.width = width
        self.title = title
        self.root = Tk()
        self.root.title(self.title)
        self.root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.root,width=self.width,height=self.height)
        self.canvas.pack(fill=BOTH,expand=True)
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
        print("Window is Closed!")

    def close(self):
        self.is_running = False

    def draw_line(self,line_obj,fill_color):
        line_obj.draw(self.canvas,fill_color)

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class line:
    def __init__(self,p1:point,p2:point):
        self.p1 = p1
        self.p2 = p2

    def draw(self,canvas,fill_color):
        x1,y1 = self.p1.x,self.p1.y
        x2,y2 = self.p2.x,self.p2.y
        canvas.create_line(x1,y1,x2,y2,fill=fill_color,width=2)
        canvas.pack(fill=BOTH,expand=1)

class cell:
    def __init__(self,win=None):
        self.has_lw = True
        self.has_rw = True
        self.has_tw = True
        self.has_bw = True
        self.x1 = None
        self.y2 = None
        self.x2 = None
        self.y2 = None
        self.visited = False
        self.win_obj = win

    def draw(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if(x1 == 0 and y1 == 0):
            self.has_tw = False

        if self.has_lw:
            lineobj = line(point(x1,y1),point(x1,y2))
            self.win_obj.draw_line(lineobj,"red")
        else:
            line_obj = line(point(x1, y1), point(x1, y2))
            self.win_obj.draw_line(line_obj, "white")

        if self.has_tw:
            lineobj = line(point(x1,y1),point(x2,y1))
            self.win_obj.draw_line(lineobj,"red")
        else:
            lineobj = line(point(x1,y1),point(x2,y1))
            self.win_obj.draw_line(lineobj,"white")

        if self.has_rw:
            lineobj = line(point(x2,y1),point(x2,y2))
            self.win_obj.draw_line(lineobj,"red")
        else:
            lineobj = line(point(x2,y1),point(x2,y2))
            self.win_obj.draw_line(lineobj,"white")

        if self.has_bw:
            lineobj = line(point(x1,y2),point(x2,y2))
            self.win_obj.draw_line(lineobj,"red")
        else:
            lineobj = line(point(x1,y2),point(x2,y2))
            self.win_obj.draw_line(lineobj,"white")
    
    def draw_move(self,to_cell,undo=False):
        if self.win_obj is None:
            return
        xmid = (self.x1+self.x2)/2
        ymid = (self.y1+self.y2)/2

        toxmid = (to_cell.x1+to_cell.x2)/2
        toymid = (to_cell.y1+to_cell.y2)/2

        fill_color = "red"
        if undo:
            fill_color = "gray"
        if self.x1 > to_cell.x1:
            l1 = line(point(xmid,ymid),point(self.x1,ymid))
            self.win_obj.draw_line(l1,fill_color)
            l2 = line(point(toxmid,toymid),point(self.x1,ymid))
            self.win_obj.draw_line(l2,fill_color)

        elif self.x1 < to_cell.x1:
            l1 = line(point(xmid,ymid),point(self.x2,ymid))
            self.win_obj.draw_line(l1,fill_color)
            l2 = line(point(toxmid,toymid),point(self.x2,ymid))
            self.win_obj.draw_line(l2,fill_color)

        elif self.y1 > to_cell.y1:
            l1 = line(point(xmid,ymid),point(xmid,self.y1))
            self.win_obj.draw_line(l1,fill_color)
            l2 = line(point(toxmid,toymid),point(xmid,self.y1))
            self.win_obj.draw_line(l2,fill_color)

        elif self.y1 < to_cell.y1:
            l1 = line(point(xmid,ymid),point(xmid,self.y2))
            self.win_obj.draw_line(l1,fill_color)
            l2 = line(point(toxmid,toymid),point(xmid,self.y2))
            self.win_obj.draw_line(l2,fill_color)

class MAZE:
    def __init__(self,
                x1,
                y1,
                num_rows,
                num_cols,
                cellsize_x,
                cellsize_y,
                win=None,
                seed=None
    ): 
        if seed != None:
            random.seed(seed)
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cellsize_x = cellsize_x
        self.cellsize_y = cellsize_y
        self.win_obj = win
        self.create_cells()
        self.break_entrance_and_exit()
        self.break_cells(0,0)
        self.reset_cells_visited(0,0)

    def create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(cell(self.win_obj))
            self._cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cells(i,j)

    def draw_cells(self,i,j):
        if self.win_obj is None:
            return
        x1 = self.x1+i*self.cellsize_x
        y1 = self.y1+j*self.cellsize_y

        x2 = x1+self.cellsize_x
        y2 = y1+self.cellsize_y

        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()

    def _animate(self):
        if self.win_obj is None:
            return
        self.win_obj.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        self._cells[0][0].has_tw = False
        self.draw_cells(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bw = False
        self.draw_cells(self.num_cols-1,self.num_rows-1)
    
    def break_cells(self,i,j):
        self._cells[i][j].visited = True
        while True:
            next_celllist = []

            if i > 0 and not self._cells[i-1][j].visited:
                next_celllist.append((i-1,j))
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                next_celllist.append((i+1,j))
            if j > 0 and not self._cells[i][j-1].visited:
                next_celllist.append((i,j-1))
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                next_celllist.append((i,j+1))
            
            if len(next_celllist) == 0:
                self.draw_cells(i,j)
                return
            
            direction_ = random.randrange(len(next_celllist))
            next_cell = next_celllist[direction_]

            if next_cell[0] == i+1:
                self._cells[i][j].has_rw = False
                self._cells[i+1][j].has_lw = False
            if next_cell[0] == i-1:
                self._cells[i][j].has_lw = False
                self._cells[i-1][j].has_rw = False
            if next_cell[1] == j+1:
                self._cells[i][j].has_bw = False
                self._cells[i][j+1].has_tw = False
            if next_cell[1] == j-1:
                self._cells[i][j].has_tw = False
                self._cells[i][j-1].has_bw = False
            self.break_cells(next_cell[0],next_cell[1])

    def reset_cells_visited(self,i,j):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
    
    def solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True

        if (i == self.num_cols - 1) and (j == self.num_rows - 1):
            return True

        if (i > 0) and (not self._cells[i-1][j].visited) and (not self._cells[i][j].has_lw):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self.solve_r(i-1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j],True)
        if (i < self.num_cols - 1) and (not self._cells[i+1][j].visited) and (not self._cells[i][j].has_rw):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self.solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j],True)

        if (j > 0) and (not self._cells[i][j-1].visited) and (not self._cells[i][j].has_tw):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self.solve_r(i,j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1],True)

        if (j < self.num_rows - 1) and (not self._cells[i][j+1].visited) and (not self._cells[i][j].has_bw):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self.solve_r(i,j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1],True)

    def solve(self):
        return self.solve_r(0,0)

def main():
    num_rows = 6
    num_cols = 8
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y,"MAZE SOLVER")
    maze = MAZE(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()
    win.wait_for_close()
main()

