---
title: Applications of Cellular Automata - Visualising Forest Fires
author:
- Simon Fish
- Jack Barradell-Johns
- Martin Kabyamela
---

# Abstract

The paper follows the creation of a model for the representation of forest fires on a given area of land. Forest fires can happen regularly in certain conditions and areas of land, and are known to cause significant damage. Therefore, it is important to be able to visualise their impact in order to be able to counteract potential damage. Our commissioners have means of mitigating further damage that this simulation could represent.

The simulation uses Conway's Game of Life, a cellular automata structure in which neighbouring cells' states  can change based on how many are 'alive' or 'dead', and adapts it for several states. These represent types of ground, and how the cell is affected by fire. Other factors such as wind speed, flammability and burn time are determined for each type of ground.

Using the simulation we were able to predict and select solutions to several problems. The start points used were those of a proposed incinerator and a power plant. Problems ranged from determining the relative time for fires to reach the town based on the wind direction, and how to protect against this either by using aerial drops of water or extending the dense forest area.

# Introduction and Background (Literature Review)

# Materials and Methods

We were provided with the engine for Conway's Game of Life in [capyle](https://github.com/pjworsley/capyle), an open source program designed for the representation of celllular automata. We were able to extend this in various ways, initially increasing the number of states in the system. Conway's Game of Life determines whether cells are born, killed, or survive based on the number of living neighbours that surround them. Our simulation of the fire spread works on a similar basis, but clearly needed to take many more factors into account to become a useful model. For this, as mentioned in the abstract, we created states for each type of land represented in the specification - 

| Land type         | Flammability  | Fuel            |
| ----------------- |:-------------:|:---------------:|
| Chaparral         | High          | Several days    |
| Dense forest      | Mild          | Up to one month |
| Lake              | Assumed none  | Assumed none    |
| Canyon/scrubland  | Very high     | Several hours   |

Table: Parameters for each type of land, based on what was provided in the specification. All assumptions above are as provided to us in the assignment brief, and have a slight element of randomness applied in practice.

We also needed to modify the basic algorithm of Conway's Game of Life to better reflect the spread of fire. The first stage in the process was to add some sort of persistence. This required us to allocate a certain amount of fuel to each starting cell based on the type of land - this takes place on a secondary grid that is not rendered, a calculation layer. The fuel allocated to each cell is depleted once per cycle (equivalent to a couple of days) at a constant rate, and represents how long the land is assumed to burn for.

Flammabiility was then represented by a threshold, which was based on the number of ignited neighbouring cells in all cardinal directions. Land that ignites easily may only need one or two neighbouring ignited cells to catch fire, but other land types could need more of that type to ignite.

Wind was the last aspect to be implemented. This added another calculation layer that used another of our assumptions - the chance of a cell catching fire is weighted based on the wind direction and and proportionally to the square root of its speed. It was most important to ensure that simulations were accurate for the prevailing wind direction (south), but that the calculations could also be accurately applicable to any wind direction. In the code, the directions are represented as follows:

------- ------- ------- 
   0       1       2
   3               4
   5       6       7
------- ------- ------- 

Table: the cardinal directions mapped to the range 0 to 7 inclusive.

The `WIND_SPEED` in km/h and `WIND_DIRECTION` are defined as constants before the simulation is run. 

# Results

**NB:** Outlier results in which a fire starts at either location but does not spread have been omitted.

## Scenario 1

### From the power plant

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 49          | 16.33        |
| 2         | 49          | 16.33        |
| 3         | 50          | 16.67        |
| 4         | 48          | 16           |
| 5         | 49          | 16.33        |

Average time taken: **16.33 hrs**

### From the incinerator

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 61          | 20.33        |
| 2         | 63          | 21           |
| 3         | 56          | 18.67        |
| 4         | 59          | 19.67        |
| 5         | 62          | 20.67        |

Average time taken: **20.07 hrs**

## Scenario 4

### North

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 69          | 23           |
| 2         | 68          | 22.67        |
| 3         | 68          | 22.67        |
| 4         | 67          | 22.33        |
| 5         | 66          | 22           |

Average time taken: **22.53 hrs**

### West

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 69          | 23           |
| 2         | 66          | 22           |
| 3         | 68          | 22.67        |
| 4         | 64          | 21.33        |
| 5         | 65          | 21.67        |

Average time taken: **22.13 hrs**

# Discussion

## Scenario 1

The construction of the proposed incinerator should pose no further risk to the town than already exists, at least in terms of the time taken for a fire to reach it. On average, fires at the incinerator take around four (up to five) hours longer to reach the town than those at the power plant. In the event that the incinerator could go on to replace the power plant as the town's power source, those additional four hours could buy rescue services vital time to concert a rescue effort.

## Scenario 4

There is little variety no matter the choice - in the given trials, fire seems to spread at similar rates, though it appears to spread marginally more quickly when the forest area is extended towards the west. While the difference between the two options is of minimal significance, the recommendation seems to be to extend the forest towards the north.

# Conclusions

The conclusions for each scenario have been addressed in the discussion section of the report, but a short summary is as follows:

1. The construction of the proposed incinerator should pose no further risk to the town than already exists, at least in terms of the time taken for a fire to reach it.
2. \<TODO>
3. \<TODO>
4. The recommendation seems to be to extend the forest towards the north, though neither option carries much benefit, only buying rescue services around two hours on average.


# References
