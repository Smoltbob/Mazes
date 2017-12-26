#!/usr/bin/env python3
from cell import *
from random import randint
import svgwrite

class Grid():

    """
    Initializes the grid and sets the correct neihbors for each cell.
    """
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.prepare_grid()
        self.configure_cells()

    """
    Returns a cell from the grid if the coordinates are valid.
    Avoids having to check within the algorithm.
    """
    def __getitem__(self, key):
        row, col = key
        if row < 0 or row > self.rows - 1:
            return None
        if col < 0 or col > self.columns - 1:
            return None
        return self.grid[row][col]

    """
    Prints the maze in ASCII.
    """
    def __str__(self):
        # Top row of the maze
        output = "+" + "---*" * self.columns + "\n"
        for row in self.each_row():
            top = "|"
            bottom = "+"

            for cell in row:
                if not cell:
                    cell = Cell(-1,-1)
                body = "   " # Three spaces
                east_boundary = " " if cell.islinked(cell.east) else "|"
                top += body + east_boundary
                south_boundary = "   " if cell.islinked(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner

            output += top + "\n"
            output += bottom + "\n" 
        return output

    def to_svg(self, cell_size = 30, name="maze.svg"):
        color = "black"
        img_width = cell_size * self.columns
        img_height = cell_size * self.rows
        
        img = svgwrite.Drawing(filename=name, debug=True)

        for cell in self.each_cell():
            x1 = cell.column * cell_size
            y1 = cell.row * cell_size
            x2 = (cell.column + 1) * cell_size
            y2 = (cell.row + 1) * cell_size

            if not cell.north:
                img.add(img.line(start=(x1,y1), end=(x2,y1), stroke=color))
            if not cell.west:
                img.add(img.line(start=(x1,y1), end=(x1,y2), stroke=color))

            if not cell.islinked(cell.east):
                img.add(img.line(start=(x2,y1), end=(x2,y2), stroke=color))
            if not cell.islinked(cell.south):
                img.add(img.line(start=(x1,y2), end=(x2,y2), stroke=color))
            img.save()

    """
    Creates the grid of initialized cells
    """
    def prepare_grid(self):
        # Inerser row et col ?
        self.grid = [[ None for x in range(0, self.rows)] for y in range(0, self.columns)]
        for r in range(0, self.rows):
            for c in range(0, self.columns):
                self.grid[r][c] = Cell(r, c)

    """
    Sets the neighbors of each cell
    """
    def configure_cells(self):
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                cell = self[i,j]
                row = cell.row
                column = cell.column
                cell.north = self[row - 1, column]
                cell.south = self[row + 1, column]
                cell.east = self[row, column + 1]
                cell.west = self[row, column - 1]

    """
    Returns a random cell from the grid
    """
    def random_cell(self):
        row = randint(0, self.rows)
        col = randint(0, self.columns)
        return self[row, col]

    """
    Returns the size of the maze
    """
    def size(self):
        return self.rows * self.columns

    """
    Iterates through rows of the grid
    """
    def each_row(self):
        for row in self.grid:
            yield row
    """
    Iterates through each cell of the grid
    """
    def each_cell(self):
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                yield self[i, j]
