# Name: Conway's game of life
# Dimensions: 2

# --- Set up executable path, do not edit ---
import sys
import inspect
this_file_loc = (inspect.stack()[0][1])
main_dir_loc = this_file_loc[:this_file_loc.index('ca_descriptions')]
sys.path.append(main_dir_loc)
sys.path.append(main_dir_loc + 'capyle')
sys.path.append(main_dir_loc + 'capyle/ca')
sys.path.append(main_dir_loc + 'capyle/guicomponents')
# ---

from capyle.ca import Grid2D, Neighbourhood, CAConfig, randomise2d
import capyle.utils as utils
import numpy as np

def transition_func(grid, neighbourstates, neighbourcounts):
    # dead = state == 0, live = state == 1
    # unpack state counts for state 0 and state 1
    dead_neighbours, live_neighbours = neighbourcounts
    # create boolean arrays for the birth & survival rules
    # if 3 live neighbours and is dead -> cell born
    birth = (live_neighbours == 3) & (grid == 0)
    # if 2 or 3 live neighbours and is alive -> survives
    survive = ((live_neighbours == 2) | (live_neighbours == 3)) & (grid == 1)
    # Set all cells to 0 (dead)
    grid[:, :] = 0
    # Set cells to 1 where either cell is born or survives
    grid[birth | survive] = 1
    return grid

def birth(grid, neighbourcounts):
    # unpack state counts for state 0 and state 1
    dead_neighbours, live_neighbours = neighbourcounts

def setup(args):
    config_path = args[0]
    config = utils.load(config_path)
    # ---THE CA MUST BE RELOADED IN THE GUI IF ANY OF THE BELOW ARE CHANGED---
    config.title = "Conway's game of life"
    config.dimensions = 2
    config.states = (0, 1)
    # ------------------------------------------------------------------------

    # ---- Override the defaults below (these may be changed at anytime) ----

    # config.state_colors = [(0,0,0),(1,1,1)]
    config.states = (0,1,2,3,4,5)
    config.state_colors = [(0.6,0.6,0.4),(0.25,0.6,0.3),(0.5,0.5,0.5),(0.1,0.1,0.9),(0.75,0.4,0.3),(0,0,0)]

    config.num_generations = 500
    config.grid_dims = (50,50)

    # 0 (chaparral), 1 (dense forest), 2 (canyon), 3 (lake), 4 (burning), 5 (dead)
    # Set all cells to 0 (chaparral)
    grid_terrain = np.zeros(config.grid_dims)
    grid_terrain[30:40, 15:25] = 1
    grid_terrain[5:35, 32:35] = 2
    grid_terrain[10:15, 5:15] = 3
    config.set_initial_grid(grid_terrain)
    # ----------------------------------------------------------------------

    if len(args) == 2:
        config.save()
        sys.exit()

    return config


def main():
    # Open the config object
    config = setup(sys.argv[1:])

    # Create grid object
    grid = Grid2D(config, transition_func)

    # Run the CA, save grid state every generation to timeline
    timeline = grid.run()

    # save updated config to file
    config.save()
    # save timeline to file
    utils.save(timeline, config.timeline_path)


if __name__ == "__main__":
    main()
