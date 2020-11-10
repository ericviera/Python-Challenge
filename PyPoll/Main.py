import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('Resources', 'election_data.csv')

votes_total = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        votes_total += 1
        candidate_in = (row[2])


print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes_total}")
print("-------------------------")
print("-------------------------")
#print(f"winner: {winner}")
print("-------------------------")


txtfile = open("Election_Results.txt", 'w')
txtfile.write("-------------------------\n")
txtfile.write("Election Results\n")
txtfile.write("-------------------------\n")
txtfile.write(f"Total Votes: {votes_total}\n")
txtfile.write("-------------------------\n")
txtfile.write("-------------------------\n")
#txtfile.write(f"winner: {winner}\n")
txtfile.write("-------------------------\n")
