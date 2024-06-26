# import modules
import os
import csv

# Locate the file paths
csv_resource_path = os.path.join('PYPOLL','Resources','election_data.csv') 
txt_analysis_path = os.path.join('PYPOLL','analysis', 'election_results.txt') 

# Assign the variables for vote counting
total_votes = 0
candidate_1 = "Charles Casper Stockham"
candidate_1_votes = 0
candidate_2 = "Diana DeGette"
candidate_2_votes = 0
candidate_3 = "Raymon Anthony Doane"
candidate_3_votes = 0

#Read the CSV file
with open(csv_resource_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    next(csv_reader)

    # Read each row of data after the header and just count the data
    for row in csv_reader:
        total_votes += 1
        if (row[2] == candidate_1):
            candidate_1_votes += 1
        if (row[2] == candidate_2):
            candidate_2_votes += 1
        if (row[2] == candidate_3):
            candidate_3_votes += 1

# Calculate percentage of votes for each candidate
canidate_1_votes_percentage = round((candidate_1_votes/total_votes)*100, 3)
canidate_2_votes_percentage = round((candidate_2_votes/total_votes)*100, 3)
canidate_3_votes_percentage = round((candidate_3_votes/total_votes)*100, 3)

# Determine the winner for the election poll
def determine_election_winner():
  
    candidates = [candidate_1, candidate_2, candidate_3]
    candidates_votes = [candidate_1_votes, candidate_2_votes, candidate_3_votes]
    election_winner = candidates[candidates_votes.index(max(candidates_votes))]
    return f"Winner: {election_winner}"

# Export the results to a text file
with open(txt_analysis_path, 'w', newline='') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"{candidate_1}: {canidate_1_votes_percentage}% ({candidate_1_votes})\n")
    txt_file.write(f"{candidate_2}: {canidate_2_votes_percentage}% ({candidate_2_votes})\n")
    txt_file.write(f"{candidate_3}: {canidate_3_votes_percentage}% ({candidate_3_votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"{determine_election_winner()}\n")
    txt_file.write("-------------------------\n")

# Print results to the terminal
print("")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidate_1}: {canidate_1_votes_percentage}% ({candidate_1_votes})")
print(f"{candidate_2}: {canidate_2_votes_percentage}% ({candidate_2_votes})")
print(f"{candidate_3}: {canidate_3_votes_percentage}% ({candidate_3_votes})")
print("-------------------------")
print(f"{determine_election_winner()}")
print("-------------------------")