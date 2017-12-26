#!/usr/bin/env python3
from grid import *
from random import choice, randint

class Sidewinder():

    def __init__(self, grid):
        for row in grid.each_row():
            run = []
            for cell in row:
                run.append(cell)
                at_eastern_boundary = (cell.east == None)
                at_northern_boundary = (cell.north == None)

                should_close_out = at_eastern_boundary or (not at_northern_boundary and randint(0,1) == 0)
                
                if should_close_out:
                    member = choice(run)
                    if member.north:
                        member.link(member.north)
                    run = []
                else:
                    cell.link(cell.east)
