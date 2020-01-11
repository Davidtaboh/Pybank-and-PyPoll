import csv
import os

file_to_write = "C:/Users/david/Desktop/Python Challenge/python-challenge/PyPoll/election_results.txt"

with open(r"C:\Users\david\Desktop\Python Challenge\python-challenge\PyPoll\election_data.csv", 'r') as election_data:
    election_data = csv.DictReader(election_data)

#variables

    total_votes = []
    candidatelist = []
    unique_candidate = []
    vote_count = []
    vote_percent = []

#loop

    for line in election_data:
        total_votes.append(line["Voter ID"])

        candidatelist.append(line["Candidate"])

#calculations

    for b in set(candidatelist):
        unique_candidate.append(b)
        c = candidatelist.count(b)
        vote_count.append(c)
        d = (c/len(candidatelist))*100
        vote_percent.append(d)
    
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

#print statements

print("Election Results")

print("Total Votes: " + str(len(total_votes)))

print("Candidates on ballot: " + str(unique_candidate))
print("Vote Totals: " + str(vote_count))
print("Candidate Vote Percentage: " + str(vote_percent))
print(winner + " is the winning candidate")

#output calculations

with open(file_to_write, "w") as txt_file:
    txt_file.write("Election Results" + "\n")
    txt_file.write("Total Votes: " + str(len(total_votes)) + "\n")
    txt_file.write("Candidates on ballot: " + str(unique_candidate) + "\n")
    txt_file.write("Candidate Vote Percentage: " + str(vote_percent)+ "\n")
    txt_file.write(winner + " is the winning candidate" + "\n")



    
    
