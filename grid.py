import cell
import numpy as np
import os
from time import sleep as slp

class Grid:
    """
    The grid. Handles both the grid that's being worked on and the\n
    visual presentation of that data in sort of a double-buffered fashion.\n
    The intial grid is populated with empty cells (otherwise every cell ends up\n
    being the same cell).
    """
    def __init__(self):
        self.rows = int(input("How many rows?\n"))
        self.columns = int(input("How many columns?\n"))
        self.generations = int(input("How many generations would you like to simulate?\n"))
        self.cellArray = np.full(shape = (self.rows, self.columns), fill_value = "").tolist()
        self.visualArray = np.full(shape = (self.rows, self.columns), fill_value = "").tolist()
    
    def populate_grid_with_cells(self):
        """
        Iterates through the empty grid and randomly assigns each cell as "alive" or "dead."
        """
        for row in range(self.rows):
            for column in range(self.columns):
                self.cellArray[row][column] = cell.Cell()
    
    def get_visual_data(self):
        """
        Iterates through the grid and assigns each cell a visual signifier for whether it's alive (▣) or dead(▢).
        """
        for row in range(self.rows):
            for column in range(self.columns):
                self.visualArray[row][column] = self.cellArray[row][column].visual
    
    def neighbor_check(self):
        """
        Iterates through the grid and counts up how many neighboring cells are alive for each cell in the grid.
        """
        for checkRow in range(self.rows - 1):
            for checkColumn in range(self.columns - 1):
                self.cellArray[checkRow][checkColumn].neighbors = 0
                for adjacentRow in range(-1, 2):
                    for adjacentColumn in range(-1, 2):
                        if self.cellArray[checkRow + adjacentColumn][checkColumn + adjacentRow].alive == True and self.cellArray[checkRow + adjacentColumn][checkColumn + adjacentRow] != self.cellArray[checkRow][checkColumn]:
                            self.cellArray[checkRow][checkColumn].neighbors += 1
