#SIR
import numpy as np
import matplotlib.pyplot as plt

#Initialize population constants
N = 10000 #total population
I_count = 1
S_count = N-I_count
R_count = 0
time_points = 1000
beta = 0.3 #infection rate constant
gamma = 0.05 #recovery rate

#Store the count to keep track of results
list_S = []
list_I = []
list_R = []

#force a new random seed every run
np.random.seed()

#Loop 1000 times (for t from 1 to time_points):
for t in range (1,1001):  

    #Calculate probabilities
    P_infection = beta * (I_count / N)
    P_recovery = gamma

    # For susceptibles: pick who becomes infected
    # np.random.binomial(number_of_trials, probability_of_success)
    new_infections = np.random.binomial(S_count, P_infection)

    # For infected: pick who recovers
    new_recoveries = np.random.binomial(I_count, P_recovery)
    
    #Update the population counts
    S_count = S_count - new_infections
    I_count = I_count + new_infections - new_recoveries
    R_count = R_count + new_recoveries

    #Record output
    #Append S_count, I_count, R_count to history lists
    list_S.append (S_count)
    list_I.append (I_count)
    list_R.append (R_count)

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

