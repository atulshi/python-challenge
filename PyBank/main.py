# import modules
import os
import csv

# Define file paths
csv_resource_path = os.path.join('PyBank','Resources','budget_data.csv') 
txt_analysis_path = os.path.join('PyBank','analysis','financial_analysis.txt')

# Assign variables
dates = []
revenue = []
total_months = 0
total_revenue = 0

 #  Empty List to store the new values in revenue per month
Monthly_change = []
 
 # List to track the corresponding dates for the changes
new_date = []

# Finding the average change in revenue
def calculate_average_change(revenue):

    for i in range(len(revenue)-1):
        Monthly_change.append(revenue[i+1] - revenue[i])
    
        new_date.append(dates[i+1])

    return sum(Monthly_change) / len(Monthly_change)

# Open the CSV file and read
with open(csv_resource_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ',')

     # Skip the header row 
    next(csv_reader)
    
    # Read each row of data after the header
    for row in csv_reader:        
        dates.append(row[0])
        revenue.append(int(row[1]))

# Calculate total months and total revenue
total_months = len(dates)
total_revenue = sum(revenue)

# Calculate average change
average_change = round(calculate_average_change(revenue), 2)

# Find the greatest increase and decrease in revenue
greatest_increase = max(Monthly_change)
greatest_decrease = min(Monthly_change)
greatest_increase_date = new_date[Monthly_change.index(greatest_increase)]
greatest_decrease_date = new_date[Monthly_change.index(greatest_decrease)]

# Write the analysis results into text file
with open(txt_analysis_path, 'w', newline='') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_revenue}\n")
    txt_file.write(f"Average Change: ${average_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Print results to the terminal
print("")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
print("")