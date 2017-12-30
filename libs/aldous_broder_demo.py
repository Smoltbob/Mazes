#!/usr/bin/env python3
from grid import *
from aldous_broder import *

grid = Grid(7,16)
Aldous_broder(grid)
print(grid)
grid.to_svg()
