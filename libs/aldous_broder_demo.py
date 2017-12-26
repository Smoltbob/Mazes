#!/usr/bin/env python3
from grid import *
from aldous_broder import *

grid = Grid(60,60)
Aldous_broder(grid)
print(grid)
grid.to_svg("aldous.svg")

