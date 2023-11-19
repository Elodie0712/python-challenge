import os
import csv
#locate the file and read it
election_csv= os.path.join("Resources", "C:\\Users\\HP\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv")

Ballot_ID=0
County=0
Candidate=0
Charles_vote=0
Charles_vote_count=[]
Diana_vote=0
Diana_vote_count=[]
Raymon_vote=0
Raymon_vote_count=[]

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter=",")
    header = next(csvreader)
    print(header)
    
#Total number of votes by looking at the total number of row
    for row in csvreader:
        Ballot_ID+=1
#identifying row 2 as candidate name row
        Candidate_name=row[2]  
#setting conditionals to calculate the count of each candidate    
        if Candidate_name=="Charles Casper Stockham":
             Charles_vote=Charles_vote+1
        elif Candidate_name=="Diana DeGette":
            Diana_vote=Diana_vote+1
        elif Candidate_name=="Raymon Anthony Doane":
            Raymon_vote=Raymon_vote+1
#Getting that in percentages
Charles_percentage= (Charles_vote/Ballot_ID)*100
Raymon_percentage= (Raymon_vote/Ballot_ID)*100
Diana_percentage= (Diana_vote/Ballot_ID)*100

#determine max vote
winner=max([(Charles_vote,"Charles Casper Stockham"), (Raymon_vote, "Raymon Anthony Doane"), (Diana_vote,"Diana DeGette")])
#printing out the results           
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: ",Ballot_ID) 
print(f"----------------------------")       
print(f"Charles Casper Stockham:",f"{Charles_percentage:.3f}%",f"({Charles_vote})")
print(f"Diana DeGette:",f"{Diana_percentage:.3f}%",f"({Diana_vote})")
print(f"Raymon Anthony Doane:",f"{Raymon_percentage:.3f}%",f"({Raymon_vote})")  
print(f"----------------------------") 
print("Wnner:",winner[1]) 
print(f"----------------------------") 
election_text= os.path.join("Resources", "C:\\Users\\HP\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.text")
with open (election_text, "w") as text_file:
    output = (
        "Election Results\n"
        "----------------------------\n"
        "Total Votes: " + str(Ballot_ID) + "\n"  # we corrected this line
        "----------------------------\n"
        "Charles Casper Stockham:" + f"{Charles_percentage:.3f}%" + f"({Charles_vote})\n"
        "Diana DeGette:" + f"{Diana_percentage:.3f}%" + f"({Diana_vote})\n"
        "Raymon Anthony Doane:" + f"{Raymon_percentage:.3f}%" + f"({Raymon_vote})\n"
        "----------------------------\n"
        "Winner: "+ (winner[1])+"\n" # we corrected this line
        "----------------------------\n"
    )
    text_file.write(output)
