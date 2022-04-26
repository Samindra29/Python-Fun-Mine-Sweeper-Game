import sys
from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell:
    all = []
    cell_count_label_object = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None  # to make each cell button-able
        self.is_opened = False
        self.is_mine_candidate = False
        self.x = x
        self.y = y

        # appending the object to the Cell.all list
        Cell.all.append(self)

    # this will make a cell btn on calling from main.py file
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12, height=4,
        )
        # event listener in tkinter
        btn.bind('<Button-1>', self.left_clicked)  # left-click
        btn.bind('<Button-2>', self.right_clicked)  # right-click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells Left: {settings.CELL_COUNT}",
            width=12, height=4,
            bg='black', fg='white',
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl

    def left_clicked(self, event):
        if self.is_mine:
            self.show_mine()

        # if 0 mines surrounding, open up the surrounding cells
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
            self.show_cell()

    # to get the x y of the surrounding cells
    def get_cell_by_axis(self, x, y):
        # return cell obj x & y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property  # make it a read only attribute
    def surrounding_cells(self):
        # took a sample and formed a formula to figure the cells out
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    # counting the surrounding mines
    @property
    def surrounded_cells_mines_length(self):
        count = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                count += 1
        return count

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1  # reduces as a cell is clicked
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)  # printing no. of surrounding mines
            # updating new label counts
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f'Cells left : {Cell.cell_count}'
                )
        # to mark a cell was opened at the end of action show_cell
        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(highlightbackground="red")
        ctypes.windll.user32.MessageBox(0, "You clicked a mine", "Game Over", 0)
        sys.exit()

    def right_clicked(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(highlightbackground='orange')
            print("Right clicked")
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False


    @staticmethod
    def randomise_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)

        # randomly making some cells mines
        for picked_cells in picked_cells:
            picked_cells.is_mine = True

    # magic method to represent the cells
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
