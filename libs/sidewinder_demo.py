#!/usr/bin/env python3
from grid import *
from sidewinder import *

grid = Grid(40,40)
Sidewinder(grid)
print(grid)
grid.to_svg()
