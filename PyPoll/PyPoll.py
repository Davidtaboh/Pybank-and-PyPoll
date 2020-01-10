import csv
import os

with open(r"C:\Users\david\Desktop\election_data.csv", 'r') as election_data:
    election_data = csv.DictReader(election_data)

#variables

    total_votes = []
    candidatelist = []
    unique_candidate = []

    for line in election_data:
        total_votes.append(line["Voter ID"])

        candidatelist.append(line["Candidate"])

    for x in set(candidatelist):
        unique_candidate.append(x)
        y = candidatelist.count(x)



print(len(total_votes))
print(unique_candidate)

