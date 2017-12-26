#!/usr/bin/env python3
from grid import *

def main():
    gride = Grid(4, 4)
    gride.prepare_grid()
    print(gride)
    for cell in gride.each_cell():
        print(cell)

main()
