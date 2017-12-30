#!/usr/bin/env python3

class Mask():
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.bits = [[ True for x in range(cols)] for y in range(rows)]

    def __getitem__(self, key):
        row, col = key
        if (row > 0 and row <= self.rows - 1) and (col > 0 and col <= self.columns - 1):
            return self.bits[row][col]
        else:
            return False

    def set(self, key, is_on):
        row, col = key
        self.bits[row][column] = is_on

    """
    Tells how many locations in the mask are enabled
    """
    def count(self):
        count = 0
        for _ in self.rows:
            for _ in self.cols:
                if self.bits[rows][cols] == True:
                    count += 1
        return count

    def random_location(self):
        row = randint(0, self.rows - 1)
        col = randint(0, self.cols - 1)
        while self.bits[row][col] == False:
            row = randint(0, self.rows - 1)
            col = randint(0, self.cols - 1)
        return (row, col)
