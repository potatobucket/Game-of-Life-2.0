import grid

newGrid = grid.Grid()

newGrid.populate_grid_with_cells()
newGrid.get_visual_data()

if __name__ == "__main__":
    newGrid.run_game_for(newGrid.generations, 15)
