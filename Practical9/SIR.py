#// Initialize population constants
#Define N (total population)
#Define I_count, S_count, R_count (initial values)
#Define beta (infection rate constant)
#Define gamma (recovery rate)
#Define time_points = 1000
import numpy as np
import matplotlib.pyplot as plt

N = 10000
I_count = 1
S_count = N-I_count
R_count = 0
time_points = 1000
beta = 0.3
gamma = 0.05

#// Initialize data storage to keep track of results
#Create lists: list_S, list_I, list_R

list_S = []
list_I = []
list_R = []

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

    #// For infected: pick who recovers
    #// We choose from [0, 1] where 1 = recovered, 0 = stay infected
    #// Number of trials = I_count
    new_recoveries = sum(np.random.choice([0, 1], I_count, p=[1 - P_recovery, P_recovery]))

    #// 3. Update the population counts
    S_count = S_count - new_infections
    I_count = I_count + new_infections - new_recoveries
    R_count = R_count + new_recoveries

    #// 4. Record output
    #Append S_count, I_count, R_count to history lists
    list_S.append (S_count)
    list_I.append (I_count)
    list_R.append (R_count)


#create dictionary
SIR_dict = {"S":S_count, "I":I_count,"R":R_count}

health_status = list(SIR_dict.keys())
population_number = list(SIR_dict.values())

S = np.array(list_S)
I = np.array(list_I)
R = np.array(list_R)

plt.figure(figsize=(6,4),dpi=150)

plt.plot(S,c="#0099ff", label="susceptible")
plt.plot(I,c="#ff6600", label="infected")
plt.plot(R,c="#33cc33", label="recovered")
plt.legend (title="health status")
plt.xlabel('Time')
plt.ylabel('Population number')
plt.title('SIR model')

plt.grid()
plt.savefig(r"C:\Users\User\OneDrive\Desktop\IBI1\IBI1_2025-26\Practical9\SIR_model.png")
plt.show()

