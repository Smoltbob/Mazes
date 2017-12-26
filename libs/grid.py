#!/usr/bin/env python3
from cell import *
from random import randint

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
