#SIR_vaccination

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.figure(figsize=(7,5),dpi=150)
plt.xlabel('Time')
plt.ylabel('Population number')
plt.title('SIR model with different vaccination rates')
#Define the vaccination rates that is gonna be tested
v_rate=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
#Define the variables
time_points = 1000
beta = 0.3
gamma = 0.05
#Outer loop: goes through every rate
for rate in v_rate:

    N = 10000 #total population
    I_count = 1
    V_count=int(N* rate) #vaccinated population
    S_count = N-I_count-V_count

    #To avoid geting negative S_count:
    if V_count +I_count > N:
        V_count = N - I_count
    S_count=N-V_count-I_count

    infected_history = []
    #Create a list to store infected numbers over time

#Loop 1000 times (for t from 1 to time_points):
    for t in range (1,1001):   
   
    #Calculate probability for a susceptible person to get infected:
        P_infection = beta * (I_count / N)
        P_recovery = gamma

    #Determine who changes status
    #For susceptibles: pick who becomes infected
    #[0, 1] where 1 = infected, 0 = stay susceptible
    #For infected: pick who recovers
    #[0, 1] where 1 = recovered, 0 = stay infected
        new_infections = sum(np.random.choice([0, 1], S_count, p=[1 - P_infection, P_infection]))
        new_recoveries = sum(np.random.choice([0, 1], I_count, p=[1 - P_recovery, P_recovery]))

        S_count=S_count - new_infections 
        I_count = I_count + new_infections - new_recoveries

    #Store the total infected numnbers (including vaccinated people)
        infected_history.append(I_count)

    if rate == 0:
        label_text = 0
    else:
        label_text = f"{int (rate *100)}%"

    plt.plot(infected_history,label=label_text, color=cm.viridis(rate))

    plt.legend (title="Vaccination rate")
    plt.grid()
    plt.savefig(r'C:\Users\User\OneDrive\Desktop\IBI1\IBI1_2025-26\Practical9\SIR_vaccination.png')
plt.show()

