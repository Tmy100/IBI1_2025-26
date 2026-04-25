#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#make array of all susceptible population
population = np.zeros((100,100))

#0:susceptible; 1:infected ; 2:recovered
initial_infected = 1
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1

plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population, cmap="viridis",interpolation="nearest")
plt.show()