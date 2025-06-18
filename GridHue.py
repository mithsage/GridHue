import tkinter as tk

# Configurations
GRID_SIZE = 25
CELL_SIZE = 25
COLORS = ["black", "red", "blue","orange", "green", "white","yellow","purple","pink"]
DEFAULT_COLOR = COLORS[0]

class GridHue:
    def __init__(self, root):
        self.root = root
        self.root.title("GridHue - Simple Drawing")

        
        self.current_color = DEFAULT_COLOR

       
        self.canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
        self.canvas.grid(row=0, column=0, columnspan=len(COLORS)+1)
        self.canvas.bind("<Button-1>", self.paint)

     
        self.cells = []
        for row in range(GRID_SIZE):
            row_cells = []
            for col in range(GRID_SIZE):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray")
                row_cells.append(cell)
            self.cells.append(row_cells)

        # Color buttons
        for i, color in enumerate(COLORS):
            btn = tk.Button(root, bg=color, width=4, command=lambda c=color: self.set_color(c))
            btn.grid(row=1, column=i)

        # Clear button
        clear_btn = tk.Button(root, text="Clear", command=self.clear)
        clear_btn.grid(row=1, column=len(COLORS))

    def set_color(self, color):
        self.current_color = color

    def paint(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            cell_id = self.cells[row][col]
            self.canvas.itemconfig(cell_id, fill=self.current_color)

    def clear(self):
        for row in self.cells:
            for cell in row:
                self.canvas.itemconfig(cell, fill="white")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = GridHue(root)
    root.mainloop()
