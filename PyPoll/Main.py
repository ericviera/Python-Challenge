import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join('Resources', 'election_data.csv')

votes_total = 0
cand_1 = 0
cand_2 = 0
cand_3 = 0
cand_4 = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        votes_total += 1
        if row[2] == "Khan":
            cand_1 += 1
        elif row[2] == "Correy":
            cand_2 += 1
        elif row[2] == "Li":
            cand_3 += 1
        elif row[2] == "O'Tooley":
            cand_4 += 1

        Khan = round((cand_1/votes_total)*100, 3)
        Correy = round((cand_2/votes_total)*100, 3)
        Li = round((cand_3/votes_total)*100, 3)
        OTooley = round((cand_4/votes_total)*100, 3)

        if cand_1 > cand_2 and cand_1 > cand_3 and cand_1 > cand_4:
            winner = "Khan"
        elif cand_2 > cand_1 and cand_2 > cand_3 and cand_2 > cand_4:
            winner = "Correy"
        elif cand_3 > cand_1 and cand_3 > cand_2 and cand_3 > cand_4:
            winner = "Li"
        elif cand_4 > cand_1 and cand_4 > cand_2 and cand_4 > cand_3:
            winner = "O'Tooley"


print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes_total}")
print("-------------------------")
print(f"Khan: {Khan}% ({cand_1})")
print(f"Correy: {Correy}% ({cand_2})")
print(f"Li: {Li}% ({cand_3})")
print(f"O'Tooley: {OTooley}% ({cand_4})")
print("-------------------------")
print(f"winner: {winner}")
print("-------------------------")


txtfile = open("Election_Results.txt", 'w')
txtfile.write("-------------------------\n")
txtfile.write("Election Results\n")
txtfile.write("-------------------------\n")
txtfile.write(f"Total Votes: {votes_total}\n")
txtfile.write("-------------------------\n")
txtfile.write(f"Khan: {Khan}% ({cand_1})\n")
txtfile.write(f"Correy: {Correy}% ({cand_2})\n")
txtfile.write(f"Li: {Li}% ({cand_3})\n")
txtfile.write(f"O'Tooley: {OTooley}% ({cand_4})\n")
txtfile.write("-------------------------\n")
txtfile.write(f"winner: {winner}\n")
txtfile.write("-------------------------\n")
