import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('Resources', 'budget_data.csv')

# variables
total_months = 0
net_prof_loss = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        # Looping through file to count the number of months
        total_months += 1
        # looping through the first index of the file to find the net profit/loss
        net_prof_loss += int(row[1])


print("---------------------------------")
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_prof_loss}")
#print(f"Average Change:  ${avg_change}")
#print(f"Greatest Increase in Profits:  {best_date} (${high})")
#print(f"Greatest Decrease in Losses:  {worst_date} (${low})")
