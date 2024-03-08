import cell
import numpy as np
import os
from time import sleep as slp

class Grid:
    def __init__(self):
        self.rows = int(input("How many rows?\n"))
        self.columns = int(input("How many columns?\n"))
        self.generations = int(input("How many generations would you like to simulate?\n"))
        self.cellArray = np.full(shape = (self.rows, self.columns), fill_value = "").tolist()
        self.visualArray = np.full(shape = (self.rows, self.columns), fill_value = "").tolist()
    
    def populate_grid_with_cells(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cellArray[row][column] = cell.Cell()
    
    def get_visual_data(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.visualArray[row][column] = self.cellArray[row][column].visual
