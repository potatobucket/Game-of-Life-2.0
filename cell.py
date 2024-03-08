import random as rndm

class Cell:
    def __init__(self):
        self.alive = rndm.choice([True, False])
        self.neighbors = 0
        if self.alive == False:
            self.visual = "▢"
        else:
            self.visual = "▣"
        self.x = 0
        self.y = 0
    
    @property
    def life_status(self):
        if self.alive == False:
            return "The cell is dead"
        else:
            return "The cell is alive! Run!"
    
    def __repr__(self):
        return f"{self.visual}"
    
    def __str__(self):
        return f"{self.visual}"
