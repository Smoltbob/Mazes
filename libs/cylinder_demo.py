#!/usr/bin/env python3
from cylinder_grid import *
from aldous_broder import *

grid = Cylinder_grid(7,16)
Aldous_broder(grid)
print(grid)
grid.to_svg()
