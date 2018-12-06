
import os
import csv
from collections import Counter

#variables/lists/dicts
voter = []
county = []
candidates = []
candidate_name = []
candidate_dict = {}
candidate_counter = 0

#csv path
csvpath = os.path.join("election_data.csv") 

print("Election Results")
print("----------------------------------")

#open and read file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
    candidate = set(candidates)    
    total_vote = len(voter)
    candidate_count = Counter(candidates)

    
    for row in candidate:  
        candidate_name.append(row)

    print(f"The total number of votes is {total_vote}")
    print("----------------------------------")

    #can_count = 0
    for row in candidate_name:
        candidate_name_each = str(candidate_name[candidate_counter])
        votes = candidates.count(candidate_name)
        votes = int(votes)
        percentage = round(votes / total_vote * 100, 2)
        candidate_dict.update({candidate_name_each : votes})
        
        print(f"{candidate_name_each}: {percentage}%  ({votes} votes)" )
        
        candidate_counter = candidate_countcounter + 1

    import operator

    winner = max(candidate_dict, key=lambda key: candidate_dict[key])
    
print("Winner: ", winner)