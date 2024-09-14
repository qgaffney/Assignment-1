#Import OS module
import os

#Import module to read CSV
import csv

#Set path for source file
CSV_PATH = os.path.join ('Resources', 'election_data.csv')

#Open and read CSV
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:

#Specify delimiter and CSV reader
    csvreader = csv.reader(csvfile, delimiter=",")

#Read header row, store it
    csv_header = next(csvreader)

#Declare variables
    total_vote_count = 0
    candidate_vote_count = 0
    winner_vote_count = 0
    winner = ""

#Declare and initiate lists and dictionaries
    total_candidate_list = []
    unique_candidate_list = []
    count_list = []
    percentage_list = []

#Loop though data
    for row in csvreader:

#Create lists to store
        total_candidate_list.append(row[2])

#Calculate total votes
        total_vote_count += 1

#Create list of unique candidate names
        candidate = row[2]
        if candidate not in unique_candidate_list:
            unique_candidate_list.append(candidate)

#Calculate total and percentage votes per candidate; name winner
    for candidate_name in unique_candidate_list:
        for value in total_candidate_list:

#Calculate total and percentage votes per unique candidate name
            if value == candidate_name:
                candidate_vote_count += 1

        candidate_vote_percentage = round(((candidate_vote_count / total_vote_count)* 100), 3)

#Create lists to store total and percentage votes
        count_list.append(candidate_vote_count)
        percentage_list.append(candidate_vote_percentage)

#Identify winner based on poular vote
        if candidate_vote_count > winner_vote_count:
            winner_vote_count = candidate_vote_count
            winner = candidate_name

#Reset vote count
        candidate_vote_count = 0

#Print results
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_vote_count}')
print(f'-------------------------')
#Print stats for each unique candidate
for (name, percentage, count) in zip(unique_candidate_list, percentage_list, count_list):
    print(f'{name}: {percentage}% ({count})')
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')

#Create output text file and set path
output = os.path.join('python-challenge', 'PyPoll', "Analysis", "election_data.txt")

#Open file in write mode and write requested results
def writeNums(args: any):
    with open('python-challenge', 'PyPoll', "Analysis", "election_data.txt", "w") as datafile:
        datafile.write(f'Election Results\n\n')
        datafile.write(f'-------------------------\n\n')
        datafile.write(f'Total Votes: {total_vote_count}\n\n')
        datafile.write(f'-------------------------\n\n')
#Print stats for each unique candidate
        for (name, percentage, count) in zip(unique_candidate_list, percentage_list, count_list):
            datafile.write(f'{name}: {percentage}% ({count})\n\n')
        datafile.write(f'-------------------------\n\n')
        datafile.write(f'Winner: {winner}\n\n')
        datafile.write(f'-------------------------\n\n')