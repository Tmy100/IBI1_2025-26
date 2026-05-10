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

print('\n == ROW 1 UNTIL ROW 10 ==')
print(dalys_data.head(10))
#The year that got the maximum DALYs across the first ten years in Afghanistan: 1998


print('\n == DATA INFO ==')
dalys_data.info() #info command do no need to add print

print('\n == DESCRIBE DATA ==')
print(dalys_data.describe())

print("\n == AFGHANISTA DATA ==")
print(dalys_data.iloc[0:30,0:4])

print("\n == ZIMBABWE DATA ==")
#columns=[entity,code,year,DALYs]
my_columns=[True,False,True,True]
print(dalys_data.loc[dalys_data.Entity == "Zimbabwe",my_columns])
#These data were recorded from 1990 until 2019.

print("\n == LARGEST AND SMALLEST DALYS IN 2019 ==")
recent_data=dalys_data.loc[dalys_data.Year == 2019,["Entity","DALYs"]]
max=recent_data["DALYs"].max()
min=recent_data["DALYs"].min()
max_row=recent_data.loc[recent_data["DALYs"] == max]
min_row=recent_data.loc[recent_data["DALYs"] == min]
print("the largest DALYs country is \n",max_row)
print("the smallest DALYs country is \n",min_row)
#The largest DALYs country is Lesotho
#The smallest DALYs country is Singapore

print("\n == PLOT THE DATA ==")
sg= dalys_data.loc[dalys_data.Entity== "Singapore",["Year","DALYs"]]
plt.plot(sg.Year,sg.DALYs,"b+")
plt.xticks(sg.Year,rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in Singapore 1990-2019")
plt.show()

print ("\n == ASK A QUESTION ==")
#Q:What was the distribution of DALYs across all countries in 2019?
print("What was the distribution of DALYs across all countries in 2019? \n")
dalys_2019=dalys_data.loc[dalys_data.Year == 2019,["Entity","DALYs"]]
plt.figure(figsize=(12, 6)) 
plt.plot(dalys_2019.Entity, dalys_2019.DALYs, "b+")
plt.xticks([]) 
plt.xlabel("All Countries")
plt.ylabel("DALYs")
plt.title("DALYs distribution in whole world 2019")
plt.show()
