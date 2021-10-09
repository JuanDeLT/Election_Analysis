# The data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
print("----------------------------------------")

#add our dependencies
import csv
import os

#assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a variable to save the file to a path.
file_to_save = os.path.join ("analysis", "election_analysis.txt")

# 1. initialize a total vote counter
total_votes = 0
#candidate options
candidate_options = []
#declare the empty dictionary {}
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file.
with open(file_to_load) as election_data:
        #to do:read and analyze the data here.
        #Read the file object with the reader function.
        file_reader = csv.reader(election_data)
        #read the header row.
        headers = next(file_reader)
        #Print each row in the CSV file.
        for row in file_reader:
               # 2. add to the total vote count.
                total_votes += 1
                #print the candidate name from each row.
                candidate_name = row[2]
                #if the candidate does not match any existing candidate...
                if candidate_name not in candidate_options:
                        #add the candidate name to the candidate list
                        candidate_options.append(candidate_name)
                        #begin tracking that candidate's vote count
                        candidate_votes[candidate_name] =0
                #add a vote to that candidate's count
                candidate_votes[candidate_name] += 1

#save the results to our text file.
with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------\n")
        print(election_results, end="")
                # Save the final vote count to the text file.
        txt_file.write(election_results)
        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
                # 2. Retrieve vote count of a candidate.
                votes = candidate_votes[candidate_name]
                # 3. Calculate the percentage of votes.
                vote_percentage = float(votes) / float(total_votes) * 100
                #to do: print out each candidate's name, vote count, and percentage of votes to the terminal.
                candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                #print each candidate's voter count and percentgae to the terminal
                print(candidate_results)
                # save the canidate results to our text file.
                txt_file.write(candidate_results)
                        #determine winning vote count, winning percentage, and winning candidate
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                        winning_count = votes
                        winning_candidate = candidate_name
                        winning_percentage = vote_percentage
        # print the winning candidate' results to the terminal
        winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
        print(winning_candidate_summary) 
        # save the winning candidate's results to the text file
        txt_file.write(winning_candidate_summary)
