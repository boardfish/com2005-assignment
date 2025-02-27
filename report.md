---
title: Applications of Cellular Automata - Visualising Forest Fires
author:
- Simon Fish
- Jack Barradell-Johns
- Martin Kabyemela
---

# Abstract

The paper follows the creation of a model for the representation of forest fires on a given area of land. Forest fires can happen regularly in certain conditions and areas of land, and are known to cause significant damage. Therefore, it is important to be able to visualise their impact in order to be able to counteract potential damage. Our commissioners have means of mitigating further damage that this simulation could represent.

The simulation uses Conway's Game of Life, a cellular automata structure in which neighbouring cells' states  can change based on how many are 'alive' or 'dead', and adapts it for several states. These represent types of ground, and how the cell is affected by fire. Other factors such as wind speed, flammability and burn time are determined for each type of ground.

Using the simulation we were able to predict and select solutions to several problems. The start points used were those of a proposed incinerator and a power plant. Problems ranged from determining the relative time for fires to reach the town based on the wind direction, and how to protect against this either by using aerial drops of water or extending the dense forest area.

# Introduction and Background (Literature Review)

In this investigation, we focus on the spread and speed of a forest fire. The USA recorded over 66,000 wildfires in the year 2017 [@national2018incident]. A sufficiently accurate model of potential forest fires can help us take preventative measures that prevent spread of these fires and help us find the most effective locations for short-term intervention.

Physical environments like forest/land terrain are often hard to simulate as they involve many inter-connecting variables. From the shape and size of forest to the terrain, temperature and weather, many things need to be measured, implemented and tracked. Fires themselves can also be very unpredictable and reactive to conditions, so any model we create would require intensive computation that still may not be sufficiently accurate.

A cellular automata consists of a cell space where each cell has a certain state. The state of a cell at any point in time is based of neighbouring cells governed by transition rules. CA (Cellular Automata) algorithms are exceptionally effective at modelling systems where local interactions are important.

![Cellular Automata](img/CellularAutomata.png)

This makes using a CA algorithm to model forest fire behaviour potentially attractive. It provides a simple model to a complex system which will not be correct, but will be useful in the properties it shares with the real problem.

CA-based models have been used before to model other real-world systems. The University of Exeter used CA-based models to simulate sewer system to better combat the effect of floods. In their journal article [@austin2014quick], they investigate CA-based systems' capacity to accurately model a sewer system when compared to traditional, more computationally intensive models. To model the sewer system, manholes were represented by states, each of which contained a certain number of figurative water blocks. Movement between manholes was dependent on relative depth and the current water level in the cell. Both this model and traditional models (SWMM5 and SIPSON) were used to simulate a sewer network in Keighley, Yorkshire. The CA-based model showed similar results to the SWMM5 and SIPSON models, being sufficiently accurate to model the sewer system. The CA-based model was significantly more efficient and faster than both of the traditional models, with the paper stating that the time saved in simulation time would be even more significant in larger network simulations.

A research team at Geoinformation and Land Management in Morocco attempted to model forest fires in Morocco, highlighting the challenges faced in their journal article. The journal [@jellouli2016forest], acknowledges that there are many parameters at play that affect the fire spread. This group decided that the transition rules would be based on these 5 parameters: vegetation, humidity, wind direction, wind power and altitude. This enabled them to simulate terrain in Morocco, Oued Laou, and identify areas of strong fire spread easily. The information from this research was sufficient to contribute to proposed approaches to combat forest fires in the region.

As shown, CA-based systems are very capable of simulating these complex real world systems.

# Materials and Methods

We were provided with the engine for Conway's Game of Life in [capyle](https://github.com/pjworsley/capyle), an open source program designed for the representation of cellular automata. We were able to extend this in various ways, initially increasing the number of states in the system. Conway's Game of Life determines whether cells are born, killed, or survive based on the number of living neighbours that surround them. Our simulation of the fire spread works on a similar basis, but clearly needed to take many more factors into account to become a useful model. For this, as mentioned in the abstract, we created states for each type of land represented in the specification -

| Land type         | Flammability  | Fuel            |
| ----------------- |:-------------:|:---------------:|
| Chaparral         | High          | Several days    |
| Dense forest      | Mild          | Up to one month |
| Lake              | Assumed none  | Assumed none    |
| Canyon/scrubland  | Very high     | Several hours   |

Table: Parameters for each type of land, based on what was provided in the specification. All assumptions above are as provided to us in the assignment brief, and have a slight element of randomness applied in practice.

We also needed to modify the basic algorithm of Conway's Game of Life to better reflect the spread of fire. The first stage in the process was to add some sort of persistence. This required us to allocate a certain amount of fuel to each starting cell based on the type of land - this takes place on a secondary grid that is not rendered, a calculation layer. The fuel allocated to each cell is depleted once per cycle (equivalent to a couple of days) at a constant rate, and represents how long the land is assumed to burn for.

Flammability was then represented by a threshold, which was based on the number of ignited neighbouring cells in all cardinal directions. Land that ignites easily may only need one or two neighbouring ignited cells to catch fire, but other land types could need more of that type to ignite.

Wind was the last aspect to be implemented. This added another calculation layer that used another of our assumptions - the chance of a cell catching fire is weighted based on the wind direction and proportionally to the square root of its speed. It was most important to ensure that simulations were accurate for the prevailing wind direction (south), but that the calculations could also be accurately applicable to any wind direction. In the code, the directions are represented as follows:

------- ------- -------
   0       1       2
   3               4
   5       6       7
------- ------- -------

Table: the cardinal directions mapped to the range 0 to 7 inclusive.

The `WIND_SPEED` in km/h and `WIND_DIRECTION` are defined as constants before the simulation is run.

# Results

**NB:** For this scenario, outlier results in which a fire starts at either location but does not spread have been omitted.

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

## Scenario 2

Wind speed used: 60
No Fire means the fire burnt out before reaching the town

### North-West

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 75          | 25           |
| 2         | 73          | 24.3         |
| 3         | 74          | 24.6         |
| 4         | 74          | 24.6         |
| 5         | 72          | 24           |

Average time taken: **24.5 hrs**

### North

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 246         | 82           |
| 2         | 223         | 74.3         |
| 3         | 236         | 78.6         |
| 4         | No Fire     | No Fire      |
| 5         | 235         | 78.3         |

Average time taken: **78.3 hrs**

### North-East

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | No Fire     | No Fire      |
| 2         | 303         | 101          |
| 3         | 294         | 98           |
| 4         | No Fire     | No Fire      |
| 5         | No Fire     | No Fire      |

Average time taken: **99.5 hrs**

### West

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 68          | 22.6         |
| 2         | 71          | 23.6         |
| 3         | 70          | 23.3         |
| 4         | 67          | 22.3         |
| 5         | 73          | 24.3         |

Average time taken: **23.2 hrs**

### East

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 249         | 83           |
| 2         | 247         | 82.3         |
| 3         | 253         | 84.3         |
| 4         | No Fire     | No Fire      |
| 5         | 231         | 77           |

Average time taken: **81.7 hrs**

### South-West

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 57          | 19           |
| 2         | 59          | 19.6         |
| 3         | 54          | 18           |
| 4         | 61          | 20.3         |
| 5         | 53          | 17.6         |

Average time taken: **18.9 hrs**

### South

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 61          | 20.3         |
| 2         | 63          | 21           |
| 3         | 59          | 19.6         |
| 4         | 61          | 20.3         |
| 5         | 60          | 20           |

Average time taken: **20.2 hrs**

### South-East

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 71          | 23.6         |
| 2         | 75          | 25           |
| 3         | 71          | 23.6         |
| 4         | 73          | 24.3         |
| 5         | 74          | 24.6         |

Average time taken: **24.2 hrs**

## Scenario 3

### Dropped over dense forest - (15, 20)

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 62          |20.67         |
| 2         | 60          |20.00         |
| 3         | 58          |19.33         |
| 4         | 59          |19.67         |
| 5         | 62          |20.67         |

Average time taken: **20.07 hrs**

### Dropped over top of canyon containing scrubland - (30, 45)

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 63          |21            |
| 2         | 60          |20            |
| 3         | 65          |21.67         |
| 4         | 64          |21.33         |
| 5         | 62          |20.67         |

Average time taken: **21.13 hrs**


### Close to the incinerator - (48, 48)

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 67          |22.33         |
| 2         | 68          |22.67         |
| 3         | 66          |22            |
| 4         | 67          |22.33         |
| 5         | 68          |22.67         |

Average time taken: **22.39 hrs**

### Close to town - (2, 39)

| Trial no. | Generations | Time (hours) |
|-----------|-------------|--------------|
| 1         | 65          |21.66         |
| 2         | No Fire     |No Fire       |
| 3         | 62          |20.67         |
| 4         | No Fire     |No Fire       |
| 5         | 65          |21.66         |

Average time taken: **21.33 hrs**
**With chance of fire never reaching the town**

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

## Scenario 2

The effect of wind direction on the spread time of a fire can be seen in the tables above. This is particularly distinct when the wind is moving directly towards the town from the incinerator and vice-versa. The delta between average time-to-burn on these two directions is 80.6 hours, with some samples not even reaching the town with the wind moving against the fire. Similar effects can be seen on other directions, for instance the slower burn on North and East, faster burns on South and West. However, the effect is most prominent on North-East vs South-West. These results support the observation that wind is a major factor in the speed of these fires, as there can be over 3 days' difference in how long the fire can take to reach the town from point of ignition.

## Scenario 3

Water dropped over the dense forest had no effect on time taken for the fire to spread to town and would therefore be ineffective. To reliably delay the fire from reaching the town, water should be dropped close to the incinerator. This would on average delay the fire by 2 hours. Water dropped close to the town had a 40% chance of preventing the fire reaching the town. However, if not prevented, it would only delay the fire on average by an hour. The best place to drop would depend on priorities. If the town is fully evacuated, dropping close to town may be the best option. Otherwise, an extra hour's evacuation time on average may be useful if lives are in danger.

## Scenario 4

There is little variety no matter the choice - in the given trials, fire seems to spread at similar rates, though it appears to spread marginally more quickly when the forest area is extended towards the west. While the difference between the two options is of minimal significance, the recommendation seems to be to extend the forest towards the north.

## How the model compares to existing journal articles on CA-Based models?

In the Cellular Automata, each cell represents a physical space with certain parameters the define it. Each cell has a fuel level, which differentiates this model from the Moroccan forest fire study. This fuel level enabled us to model the flammability of different terrains. This was significantly more important in this investigation as the flammability of terrain various widely.  The Moroccan forest fire study is similar in fact it takes wind direction and wind speed into account when determining if a certain cell will catch fire. But differs again in the fact that our investigation didn’t take humidity into account.
Like the University of Exeter sewer simulations, our investigation involved identifying the variables that had the most significant effect on state the environment. In the sewer simulation case, it was the depth of manhole and current level of water. Other factor such as temperature or acidity, were not implement here. Similarly, fuel, wind and burn rate were the most significant factors for this simulation. And therefore not all factors could implemented. This reduced the accuracy of the model but makes it sufficiently accurate to predict reasonable outcomes in real time.

# Model 

Further progress could be made on the model if funds became available, through the addition of features to simulate events and environment details which may affect the way a fire will spread, examples of the kinds of features which could be added, are things like weather, e.g. rain, which could be further improved by simulating "wetness" of potential fuel which will counter the chance of something igniting. Other features which could be added are the ideas of plant regrowth, the effect of seasons etc. 

# Conclusions

The conclusions for each scenario have been addressed in the discussion section of the report, but a short summary is as follows:

1. The construction of the proposed incinerator should pose no further risk to the town than already exists, at least in terms of the time taken for a fire to reach it.
2. Wind is a major factor in the speed of forest fires, as there can be over 3 days' difference in how long the fire can take to reach the town from point of ignition.
3. To reliably delay the fire from reaching the town, water should be dropped close to the incinerator, though a drop point should be chosen based on whether or not the town has been evacuated.
4. The recommendation seems to be to extend the forest towards the north, though neither option carries much benefit, only buying rescue services around two hours on average.

# References
