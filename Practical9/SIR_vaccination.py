#// Initialize population constants
#Define N (total population)
#Define I_count, S_count, R_count (initial values)
#Define beta (infection rate constant)
#Define gamma (recovery rate)
#Define time_points = 1000
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.figure(figsize=(7,5),dpi=150)
plt.xlabel('Time')
plt.ylabel('Population number')
plt.title('SIR model with different vaccination rates')
# Define the vaccination rates that is gonna be tested
v_rate=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
# Define the variables
time_points = 1000
beta = 0.3
gamma = 0.05
#Outer loop: goes through every rate
for rate in v_rate:

    N = 10000
    I_count = 1
    V_count=int(N* rate)
    S_count = N-I_count-V_count

    #to avound geting negative S_count:
    if V_count +I_count > N:
        V_count = N - I_count
    S_count=N-V_count-I_count

    infected_history = []
    # create a list to store infected numbers over time

#Loop 1000 times (for t from 1 to time_points):
    for t in range (1,1001):   
    #// 1. Calculate probabilities
    #// Probability for a susceptible person to get infected:
    #// P(inf) = beta * (current_infected / total_population)
        P_infection = beta * (I_count / N)
        P_recovery = gamma

    #// 2. Determine who changes status
    #// For susceptibles: pick who becomes infected
    #// We choose from [0, 1] where 1 = infected, 0 = stay susceptible
    #// Number of trials = S_count
        new_infections = sum(np.random.choice([0, 1], S_count, p=[1 - P_infection, P_infection]))
        new_recoveries = sum(np.random.choice([0, 1], I_count, p=[1 - P_recovery, P_recovery]))

        S_count=S_count - new_infections 
        I_count = I_count + new_infections - new_recoveries
    #// 3. Calculate the number of vaccinated people
    #// We choose from [0, 1] where 1 = vaccinated, 0 = without vaccination
        infected_history.append(I_count)

    if rate == 0:
        label_text = 0
    else:
        label_text = f"{int (rate *100)}%"

    plt.plot(infected_history,label=label_text, color=cm.viridis(rate))

plt.legend (title="Vaccination rate")
plt.grid()
plt.savefig(r"C:\Users\User\OneDrive\Desktop\IBI1\IBI1_2025-26\Practical9\SIR_vaccination.png")
plt.show()

