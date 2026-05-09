#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#0:susceptible; 1:infected ; 2:recovered
    #make array of all susceptible population
population = np.zeros((100,100))

    #set up the initial parameters and infected rates
N = 10000 #total population
I_count = 1
S_count = N-I_count
R_count = 0
time_points = 100
beta= 0.3
gamma= 0.05
# --- Move this OUTSIDE the time loop ---
# randomly choose ONE initial outbreak point for the whole simulation
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
# ---------------------------------------

time = input("The time point (1-101): ")

for t in range(int(time)):
    
    # find infected points
    infectedIndex = np.where(population == 1)
    
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        
        # infect neighbours
        for xNeighbour in range(x-1, x+2):
            for yNeighbour in range(y-1, y+2):
                if (xNeighbour, yNeighbour) != (x, y):
                    if 0 <= xNeighbour < 100 and 0 <= yNeighbour < 100:
                        if population[xNeighbour, yNeighbour] == 0:
                            if np.random.rand() < beta:
                                population[xNeighbour, yNeighbour] = 1
        
        # The currently infected person recovers with probability gamma
        if np.random.rand() < gamma:
            population[x, y] = 2

# Plotting
plt.figure(figsize=(6,4), dpi=150)
# 'viridis' defaults to: 0=Purple, 1=Teal/Green, 2=Yellow. Perfect for this.
plt.imshow(population, cmap="viridis", interpolation="nearest")
plt.show()
