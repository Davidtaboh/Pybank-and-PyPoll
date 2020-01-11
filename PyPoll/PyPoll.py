import csv
import os

with open(r"C:\Users\david\Desktop\Python Challenge\python-challenge\PyPoll\election_data.csv", 'r') as election_data:
    election_data = csv.DictReader(election_data)

#variables

    count = 1048575
    total_votes = []
    candidatelist = []
    unique_candidate = []
    vote_count = []
    vote_percent = []

    for line in election_data:
        total_votes.append(line["Voter ID"])

        candidatelist.append(line["Candidate"])

    for x in set(candidatelist):
        unique_candidate.append(x)
        y = candidatelist.count(x)
        vote_count.append(y)
        z = (y/count)*100
        vote_percent.append(z)



print(len(total_votes))
print(unique_candidate)
print(vote_count)
print(vote_percent)
