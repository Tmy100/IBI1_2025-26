# Part1: List the number of patients
heart_rate= [72,60,126,85,90,59,76,131,88,121,64]
print  ("The number of pateints:", len(heart_rate))

# Part2: Calculate the mean heart rate of the patients
mean_rate= sum (heart_rate)/len (heart_rate)
print ("Mean heart rate:", mean_rate)

# Part3: Categorise heart rate into three levels.
Low=[]
Normal=[]
High=[]

for x  in heart_rate:


    if x < 60 :
        Low.append(x)
        
    elif x>=60 and x<=120:
        Normal.append(x)
        
    else:
        High.append(x)
       

# Part4: List the number of patients in each category.
print ("patients in low category:", len(Low))
print ("patients in norm category:", len(Normal))
print ("patients in high category:", len(High))

# Determine which category got the highest number of patients.
if len(Low) >( len(Normal) and len(High)):
    print ("The largest category:Low")
elif len(Normal)> ( len(Low)and len(High)):
    print ("The largest category:Normal")
else :
    print ("The largest category:High")

# Part5: Create a pie chart
import matplotlib.pyplot as plt
# Define the data and labels for the pie chart
chart_data = [len(Low),len(Normal),len(High)]
chart_labels = ['Low', 'Normal', 'High']
chart_colors = ['#66b3ff', '#99ff99', '#ff9999'] # Light blue, green, red

# List the components in the chart and format the chart
plt.pie(chart_data, labels=chart_labels, colors=chart_colors,startangle=140,autopct=lambda p: '{:.0f}'.format(p * sum(chart_data) / 100))

plt.title('Patient Heart Rate Categories')
plt.show()
