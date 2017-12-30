#!/usr/bin/env python3
from grid import *

class Masked_grid(Grid):

    def __init(self, rows, columns):
       Grid.__init__(self, rows, columns)  
    
    def __getitem__(self, key):
        row, col = key
        if row < 0 or row > self.rows - 1:
            return None
        else:
            col = col % self.columns
            return self.grid[row][col]

