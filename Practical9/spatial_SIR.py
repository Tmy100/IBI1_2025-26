#spatial_SIR

import numpy as np
import matplotlib.pyplot as plt

#1. Make an array of all susceptible populations
population = np.zeros((100,100))

#2. Set up the initial parameters and infection rates
N = 10000 #total population
I_count = 1 #infected population
S_count = N-I_count #susceptible population 
R_count = 0 #recovered population
beta= 0.3 #proportion infection rate 
gamma= 0.05 #recovery rate

#3. Randomly choose one initial outbreak point for the whole simulation
#(Pick a random X and Y coordinate between 0 and 99. Set that cell to 1 (Infected).)
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

#4. Input the time point that we wanted to investigate.
time = input("The time point (0-100): ")

#5. Loop through the time range:
for t in range(int(time)):
    
    #6. Find infected points
    infectedIndex = np.where(population == 1)
    
    #7. Loop through all infected points
    # locate all currently infected cells on the grid and store their X/Y indices.
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        
        #8. Loop through the 3x3 grid centered on the infected cell (x, y)
        #To check its surrounding neighbours
        for xNeighbour in range(x-1, x+2):
            for yNeighbour in range(y-1, y+2):
                #Skip the center cell itself (an individual cannot infect themselves)
                if (xNeighbour, yNeighbour) != (x, y):
                    #Ensure the neighbour coordinates do not fall off the edge of the 100x100 grid
                    if 0 <= xNeighbour < 100 and 0 <= yNeighbour < 100:
                        #If the neighbour is Susceptible (state 0)...
                        if population[xNeighbour, yNeighbour] == 0:
                            #Roll a random chance against 'beta'. If successful, infect them (state 1).
                            if np.random.rand() < beta:
                                population[xNeighbour, yNeighbour] = 1
        
        #9. After attempting to infect neighbours, the current infected individual has a chance to recover.
        #Roll against 'gamma'. If successful, set to Recovered (state 2).
        #The currently infected person recovers with probability gamma
        if np.random.rand() < gamma:
            population[x, y] = 2

#10. Plot a graph
#Render the final population matrix as an image map where values (0,1,2) correspond to different colours.
plt.figure(figsize=(6,4), dpi=150)
plt.imshow(population, cmap="viridis", interpolation="nearest")
plt.show()
