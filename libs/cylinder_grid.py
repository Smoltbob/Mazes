#!/usr/bin/env python3
from grid import *

class Cylinder_grid(Grid):
    
    def __getitem__(self, key):
        row, col = key
        if not (row > 0 and row < self.rows - 1):
            col = col % self.columns
            return self.grid[row][col]
        else:
            return None
