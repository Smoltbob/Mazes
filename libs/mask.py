#!/usr/bin/env python3

class Mask():
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.bits = [[ True for x in range(rows)] for y in range(cols)]
