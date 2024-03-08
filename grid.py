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
