#population growth rate
population_data = {
    'UK': {'pop2020': 66.7, 'pop2024': 69.2},
    'China': {'pop2020': 1426.0, 'pop2024': 1410.0},
    'Italy': {'pop2020': 59.4, 'pop2024': 58.9},
    'Brazil': {'pop2020': 208.6, 'pop2024': 212.0},
    'USA': {'pop2020': 331.6, 'pop2024': 340.1}
}

percent_changes = {}

for country, pops in population_data.items():
    pop2020 = pops['pop2020']
    pop2024 = pops['pop2024']
    
    # Formula: ((pop2024 - pop2020) / pop2020) * 100
    change = ((pop2024 - pop2020) / pop2020) * 100
    percent_changes[country] = change
    
    # .2f formats the number to 2 decimal places
    print(f"{country}: {change:.2f}%") 

# Print descending order and identify extremes
sorted_changes = sorted(percent_changes.items(), key=lambda item: item[1], reverse=True)

for country, change in sorted_changes:
    print(f"{country}: {change:.2f}%")


# The first item in the sorted list is the largest increase
largest_increase_country = sorted_changes[0][0]
largest_increase_value = sorted_changes[0][1]

# The last item in the sorted list is the largest decrease (most negative)
largest_decrease_country = sorted_changes[-1][0]
largest_decrease_value = sorted_changes[-1][1]

print(f"\nLargest Increase: {largest_increase_country} ({largest_increase_value:.2f}%)")
print(f"Largest Decrease: {largest_decrease_country} ({largest_decrease_value:.2f}%)")

countries = [item[0] for item in sorted_changes]
changes = [item[1] for item in sorted_changes]

#create a bar chart
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))

# Create the bars
bars = plt.bar(countries, changes)

# Add a horizontal line at 0 to clearly separate positive/negative growth
plt.axhline(0, color='black', linewidth=1)

# Formatting: Adding labels and a title
plt.title('Percentage Change in Population (2020 vs 2024)', fontsize=14)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Percentage Change (%)', fontsize=12)

# Optional visual improvement: Make positive bars green and negative bars red
for bar in bars:
    if bar.get_height() < 0:
        bar.set_color('salmon')
    else:
        bar.set_color('lightgreen')

# Optional visual improvement: Add the exact numbers on top/bottom of the bars
for bar in bars:
    yval = bar.get_height()
    # Adjust position slightly depending on if the bar is positive or negative
    offset = 0.1 if yval >= 0 else -0.25 
    plt.text(bar.get_x() + bar.get_width()/2, yval + offset, f'{yval:.2f}%', ha='center', fontweight='bold')

# Display the chart
plt.show()