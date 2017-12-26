#!/usr/bin/env python3

class Cell():

    """
    Initialises the cell with x, y coordinates
    and a hash table of linked cells
    """
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.links = {}

    """
    Links self with another cell.
    Bidi is used to make the link bidirectional.
    """
    def link(self, cell, bidi = True):
        self.links[cell] = False
        if bidi:
            cell.link(self, False)

    """
    Unlinks self from another cell by deleting the cell from
    the hash table. 
    Bidi is used to make the link bidirectional.
    """
    def unlink(self, cell, bidi = True):
        self.links.pop(cell, None)
        if bidi:
            cell.unlink(self, False)

    """
    Returns the list of linked cells.
    """
    def links(self):
        return self.links.keys()

    """
    Says if self is linked with cell
    """
    def islinked(self, cell):
        return cell in self.links

    """
    Queries the list of neighbors of self.
    """
    def neighbors(self):
        res = []
        if self.north is not None:
            res.append(north)
        if self.south is not None:
            res.append(south)
        if self.east is not None:
            res.append(east)
        if self.west is not None:
            res.append(west)
        return res
