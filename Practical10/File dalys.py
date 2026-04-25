import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as py


pathway= os.chdir('c:/Users/User/OneDrive/Desktop/IBI1/IBI1_2025-26/Practical10')
fileloc= os.getcwd()
filelist= os.listdir()

print('== FILE DIRECTORY ==')
print (fileloc)
print('\n == FILE LIST ==')
print (filelist)

#USE PANDAS TO REAS THE CSV
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(" ")
print('== ROW 1 UNTIL ROW 5 ==')
print(dalys_data.head(5))
print(" ")
print('== DATA INFO ==')
dalys_data.info() #info command do no need to add print
print(" ")
print('== DESCRIBE DATA ==')
print(dalys_data.describe())
print(" ")
print("== AFGHANISTA DATA ==")
print(dalys_data.iloc[0:30,0:4])
print(' ')
print("== ZIMBABWE DATA ==")
print(dalys_data.loc[dalys_data.Entity == "Zimbabwe",["Entity","Year","DALYs"]])
print(' ')
print("== LARGEST AND SMALLEST DALYS IN 2019 ==")
recent_data=dalys_data.loc[dalys_data.Year == 2019,["Entity","DALYs"]]
max=recent_data["DALYs"].max()
min=recent_data["DALYs"].min()
max_row=recent_data.loc[recent_data["DALYs"] == max]
min_row=recent_data.loc[recent_data["DALYs"] == min]
print("the largest DALYs country is \n",max_row)
print("the smallest DALYs country is \n",min_row)
print(' ')
print("== PLOT THE DATA ==")
mlys= dalys_data.loc[dalys_data.Entity== "Malaysia",["Year","DALYs"]]
plt.plot(mlys.Year,mlys.DALYs,"b+")
plt.xticks(mlys.Year,rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in Malaysia 1990-2019")
plt.show()

print ("== ASK A QUESTION ==")
#Q:What was the distribution of DALYs across all countries in 2019?
print("What was the distribution of DALYs across all countries in 2019? \n")
dalys_2019=dalys_data.loc[dalys_data.Year == 2019,["Entity","DALYs"]]
plt.plot(dalys_2019.Entity,dalys_2019.DALYs,"b+")
plt.xticks(dalys_2019.Entity,rotation=-90)
plt.xlabel("Entity")
plt.ylabel("DALYs")
plt.title("DALYs distribution in whole world 2019")
plt.show()