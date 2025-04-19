# Implement an 'eraser' on a canvas.
# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all  the rectangles it is in contact with to white.

import  tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root,  width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        self.cells = [] # Store cell rectangle IDs
        self.eraser = None

        self.create_grid()

        self.canvas.bind("<Button-1>", self.create_eraser)

    def create_grid(self):
        for row in range(0,CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                rect = self.canvas.create_rectangle(
                    col, row,
                    col + CELL_SIZE, row + CELL_SIZE,
                    fill="blue", outline="white"
                )
                self.cells.append(rect)


    def create_eraser(self, event):
        x, y = event.x, event.y
        self.eraser = self.canvas.create_rectangle(
            x, y,
            x + ERASER_SIZE, y + ERASER_SIZE,
            fill="pink", outline="black"

        )

        self.move_eraser()

    def move_eraser(self):
        def update():
            if self.eraser:
                x = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
                y = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()

                # Move eraser
                self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

                # Erase overlapping cells
                overlapping = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)

                for item in overlapping:
                    if item != self.eraser:
                        self.canvas.itemconfig(item, fill="white")

            self.root.after(50, update)
        update()

# Start the app
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Tkinter Eraser Canvas")
    app = EraserApp(root)
    root.mainloop()


