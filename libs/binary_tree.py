#!/usr/bin/env python3
from grid import *
from random import choice

"""
Implementation of binary tree algorithm for maze generation.
For each cell, we randomly make one door on the east or north.
"""
class Binary_tree():
    
    """
    Creates the maze
    """
    def __init__(self, grid):
        """
        We can go through the cells in any order
        """
        for cell in grid.each_cell():
            """
            We build a list of neighbors and will pick randomly through them
            to build the nodes
            """
            neighbors = []
            if cell.north:
                neighbors.append(cell.north)
            if cell.east:
                neighbors.append(cell.east)

            if neighbors != []: 
                neighbor = choice(neighbors)
                cell.link(neighbor)
