import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('Resources', 'budget_data.csv')

# variables
total_months = 0
net_prof_loss = 0
count = 0
avg_change = 0
high = 0
low = 0
month = []
monthly_change = []
monies = []
change = []
best_date = ""
worst_date = ""


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        # Looping through file to count the number of months
        total_months += 1
        # looping through the first index of the file to find the net profit/loss
        net_prof_loss += int(row[1])

        if count == 0:
            count += 1
            newmoney = int(row[1])
            monies.append(int(row[1]))
            month.append(str(row[0]))

        else:
            monies.append(int(row[1]))
            month.append(str(row[0]))
            change.append(int(int(row[1])-newmoney))
            monthly_change.append(str(row[0]))
            newmoney = int(row[1])

    # Find average change
    avg_change = round(sum(change) / len(monthly_change), 2)
    # Find Greatest increase in profits and date
    high = max(change)
    best_date = change.index(high)
    # Find Greatest Decrease in losses and date
    low = min(change)
    worst_date = change.index(low)


print("---------------------------------")
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_prof_loss}")
print(f"Average Change:  ${avg_change}")
print(f"Greatest Increase in Profits:  {monthly_change[best_date]} (${high})")
print(f"Greatest Decrease in Losses:  {monthly_change[worst_date]} (${low})")
