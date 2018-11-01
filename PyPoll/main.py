import csv
import os

csvfile = os.path.join("Py_Poll.csv")

voter_id_list = []
county_list = []
candidates_list = []

with open(csvfile,newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        voter_id_list.append(row[0])
        county_list.append(row[1])
        candidates_list.append(row[2])

print("Election Results")
print ("-------------------------------------")

#total votes
total_votes = len(voter_id_list)

print(f"Total Votes: " + str(total_votes))
print("-------------------------------------")

#list of candidates
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
total_votes_range = range(total_votes)

for vote in total_votes_range:
    if candidates_list[vote] == "Khan":
        khan_votes = khan_votes +1
    elif candidates_list[vote] == "Correy":
            correy_votes = correy_votes + 1
    elif candidates_list[vote] == "Li":
                li_votes = li_votes + 1
    elif candidates_list[vote] == "O\'Tooley":
                    otooley_votes = otooley_votes + 1

khan_percent = '{0:.2%}'.format((khan_votes/total_votes))
correy_percent = '{0:.2%}'.format((correy_votes/total_votes))
li_percent = '{0:.2%}'.format((li_votes/total_votes))
otooley_percent = '{0:.2%}'.format((otooley_votes/total_votes))


print("Khan: " + str(khan_percent) + " (" + str(khan_votes) +")")
print("Correy: " + str(correy_percent) + " (" + str(correy_votes)+")")
print("Li: " + str(li_percent) + " (" + str(li_votes) + ")")
print("O'Tooley: " + str(otooley_percent) + " (" + str(otooley_votes)+ ")")

print("-------------------------------------")

output_file = os.path.join('poll_data.txt')
with open('poll_data.txt', 'w') as f:
        f.write("Election Results ")
        f.write(" ---------------------- ")
        f.write(" Total Votes: " + str(total_votes))
        f.write("Khan: " + str(khan_percent) + " (" + str(khan_votes) +")")
        f.write("Correy: " + str(correy_percent) + " (" + str(correy_votes)+")")
        f.write("Li: " + str(li_percent) + " (" + str(li_votes) + ")")
        f.write("O'Tooley: " + str(otooley_percent) + " (" + str(otooley_votes)+ ")")

