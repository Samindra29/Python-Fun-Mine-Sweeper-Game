from tkinter import *
import settings
import utils
from cell import Cell

# for the window screen
root = Tk()
# override widow settings
root.configure(bg="black")
root.geometry('1440x720')
root.title("Mine Sweeper Game")
root.resizable(False, False)

# dividing the window into sections/frames
top_frame = Frame(
    root,
    bg='black',  # change to red to test frame divisions
    width=settings.WIDTH,
    height=utils.height_percentage(25)
)
top_frame.place(x=0, y=0)  # need to specify the pixel values in x and y-axis
# sidebar
left_frame = Frame(
    root,
    bg='black',  # change to blue to test frame divisions
    width=utils.width_percentage(25),
    height=utils.height_percentage(75)
)
left_frame.place(x=0, y=180)

center_frame = Frame(
    root,
    bg='black',  # change to green to test frame divisions
    width=utils.width_percentage(75),
    height=utils.height_percentage(75)
)
center_frame.place(
    x=utils.width_percentage(25),
    y=utils.height_percentage(25)
)

# dynamically making the grid for the game layout
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# print(Cell.all)

# call label from the Cell class
Cell.create_cell_count_label(left_frame)   # we want the count stuff on the left column
Cell.cell_count_label_object.place(x=0, y=0)
Cell.randomise_mines()


# run the window
root.mainloop()
