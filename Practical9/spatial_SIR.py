#spatial_SIR

import numpy as np
import matplotlib.pyplot as plt

#0:susceptible; 1:infected ; 2:recovered
#Make array of all susceptible population
population = np.zeros((100,100))

#Set up the initial parameters and infected rates
N = 10000 #total population
I_count = 1
S_count = N-I_count
R_count = 0
time_points = 100
beta= 0.3
gamma= 0.05

#Randomly choose one initial outbreak point for the whole simulation
#Pick a random X and Y coordinate between 0 and 99. Set that cell to 1 (Infected).
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

time = input("The time point (0-100): ")

for t in range(int(time)):
    
    #Find infected points
    infectedIndex = np.where(population == 1)
    
    #Locate all currently infected cells on the grid and store their X/Y indices.
    #Loop through all infected points
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        
        #Loop through the 3x3 grid centered on the infected cell (x, y)
        #To check its surrounding neighbours
        #Infect neighbours
        for xNeighbour in range(x-1, x+2):
            for yNeighbour in range(y-1, y+2):
                #Skip the center cell itself (an individual cannot infect themselves)
                if (xNeighbour, yNeighbour) != (x, y):
                    #Ensure the neighbor coordinates do not fall off the edge of the 100x100 grid
                    if 0 <= xNeighbour < 100 and 0 <= yNeighbour < 100:
                        #If the neighbor is Susceptible (state 0)...
                        if population[xNeighbour, yNeighbour] == 0:
                            #Roll a random chance against 'beta'. If successful, infect them (state 1).
                            if np.random.rand() < beta:
                                population[xNeighbour, yNeighbour] = 1
        
        #After attempting to infect neighbors, the current infected individual has a chance to recover.
        #Roll against 'gamma'. If successful, set to Recovered (state 2).
        #The currently infected person recovers with probability gamma
        if np.random.rand() < gamma:
            population[x, y] = 2

#Plot a graph
#Render the final population matrix as an image map where values (0,1,2) correspond to different colors.
plt.figure(figsize=(6,4), dpi=150)
plt.imshow(population, cmap="viridis", interpolation="nearest")
plt.show()
