#!/usr/bin/env python3
from grid import *
from random import choice, randint
"""
Basically a random walk
"""

class Aldous_broder():

    def __init__(self, grid):
        cell = grid.random_cell()
        unvisited = grid.size() - 1

        while unvisited > 0:
            # Pick randomly from neighbors
            neighbor = None
            while neighbor is None:
                neighbor = choice([cell.east, cell.north, cell.south, cell.west])

            if neighbor.links == {}:
                cell.link(neighbor)
                unvisited -= 1

            cell = neighbor
