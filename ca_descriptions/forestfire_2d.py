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
from random import randint as rand

# Initialise fuel grid
grid_fuel = np.zeros((50,50))
grid_burn_chance = np.zeros((50,50))
BURN_THRESHOLD = 4
WIND_DIRECTION = 6
WIND_SPEED = 10
BASE_IGNITION_RATE = 1

def transition_func(grid, neighbourstates, neighbourcounts):
    # 0 (chaparral), 1 (dense forest), 2 (canyon), 3 (lake), 4 (burning), 5 (dead)
    # unpack state counts for state 0 and state 1
    #print(neighbourstates[1][1])
    chaparral_neighbours, dense_forest_neighbours, canyon_neighbours, lake_neighbours, burning_neighbours, dead_neighbours = neighbourcounts
    live_neighbours = chaparral_neighbours + dense_forest_neighbours + canyon_neighbours + lake_neighbours
    wind_speed(grid_burn_chance)
    burning = ((grid_burn_chance >= BURN_THRESHOLD) & (burning_neighbours >= ignition(grid)))
    ## Set cells to 4 where cell is burning
    grid[burning] = 4
    grid = fuel_use(grid)
    return grid

def wind_speed(grid_burn_chance):
    WIND_DIRECTION_INDICES = {
        0: [(-1,0), (-1,1), (0,1)],
        1: [(-1,1), (0,1), (1,1)],
        2: [(0,1), (1,1), (1,0)],
        3: [(-1,1), (-1,0), (-1,-1)],

        4: [(1,1), (1,0), (1,-1)],
        5: [(-1,0), (-1,-1), (0,-1)],
        6: [(-1,-1), (0,-1), (1,-1)],
        7: [(1,0), (1,-1), (0,-1)]
    }
    for row in range(len(grid_burn_chance)):
        for cell in range(row):
            for (x,y) in WIND_DIRECTION_INDICES[WIND_DIRECTION]:
                grid_burn_chance[y][x] += WIND_SPEED * BASE_IGNITION_RATE
                 


def ignition(grid):
    # Chaparral catches fire easily
    # Lake will not catch fire
    # Canyon ignites easily too
    # dense forest, doesn't ignite easily
    # 0 (chaparral), 1 (dense forest), 2 (canyon), 3 (lake), 4 (burning), 5 (dead)
    MIN_NEIGHBORS = {
           0: 1,
           1: 3, 
           2: 1,
           3: 9, # will not catch fire
           4: 0,
           5: 9  # will not catch fire
           }   
    return np.vectorize(MIN_NEIGHBORS.get)(grid)

def fuel_use(grid):
    global grid_fuel
    # if it is burning, reduce it by 1
    grid_fuel[(grid == 4)] -= 1
    # if it's burning and 0, it's dead
    grid[(grid == 4) & (grid_fuel == 0)] = 5
    # if it's burning and -1, it's burning and has 10
    grid_fuel[((grid == 4) & (grid_fuel == -1))] = 10
    return grid

def setup(args):
    config_path = args[0]
    config = utils.load(config_path)
    # ---THE CA MUST BE RELOADED IN THE GUI IF ANY OF THE BELOW ARE CHANGED---
    config.title = "Forest Fire Simulation"
    config.dimensions = 2
    # ------------------------------------------------------------------------

    # ---- Override the defaults below (these may be changed at anytime) ----

    # config.state_colors = [(0,0,0),(1,1,1)]
    config.states = (0,1,2,3,4,5)
    config.state_colors = [(0.6,0.6,0.4),(0.25,0.6,0.3),(0.5,0.5,0.5),(0.1,0.1,0.9),(0.75,0.4,0.3),(0,0,0)]
    #config.num_generations = 500
    config.grid_dims = (50,50)
    config.wrap = False    

    # 0 (chaparral), 1 (dense forest), 2 (canyon), 3 (lake), 4 (burning), 5 (dead)
    # Set all cells to 0 (chaparral)
    grid_terrain = np.zeros(config.grid_dims)
    grid_terrain[30:40, 15:25] = 1
    grid_terrain[5:35, 32:35] = 2
    grid_terrain[10:15, 5:15] = 3
    # Ignite ground at incinerator
    # grid_terrain[0, 49] = 4
    # Ignite ground at power plant
    grid_terrain[0, 0] = 4

    config.set_initial_grid(grid_terrain)
    d1, d2 = config.grid_dims
    FUEL_CONSUMPTION_RATES = {
            0: 96//3,
            1: 720//3, 
            2: 30//3,
            3: 0, # will not catch fire
            4: 0,
            5: 0  # will not catch fire
            }
    global grid_fuel
    grid_fuel = np.ceil(np.vectorize(FUEL_CONSUMPTION_RATES.get)(grid_terrain) * np.random.rand(d1,d2))
    # Initialise fuel grid 
    #grid_fuel = np.ceil(np.random.rand(d1, d2) * 10) 
    #grid_fuel = np.zeros(config.grid_dims)
    #grid_fuel[30:40, 15:25] = np.ceil(np.random.rand(10,10) * 100)
    # ----------------------------------------------------------------------

    FIRE_PROPAGATION_RATES = {
            0: rand(12,18),
            1: rand(6,10), 
            2: rand(14,20),
            3: 0, # will not catch fire
            4: rand(8,9),
            5: 0  # will not catch fire
            }
    global grid_burn_chance
    grid_burn_chance = np.ceil(np.vectorize(FIRE_PROPAGATION_RATES.get)(grid_terrain) * np.random.rand(d1,d2))

    if len(args) == 2:
        config.save()
        sys.exit()

    return config


def main():
    # Open the config object
    config = setup(sys.argv[1:])

    # Create grid object
    grid = Grid2D(config, transition_func)
    grid_fuel[(grid == 4)] = 10

    # Run the CA, save grid state every generation to timeline
    timeline = grid.run()

    # save updated config to file
    config.save()
    # save timeline to file
    utils.save(timeline, config.timeline_path)


if __name__ == "__main__":
    main()
