# Import  Dependencies
import os
import csv
from decimal import Decimal


# Save path to csv file in a variable
election_csv_path=os.path.join("..","Resources","election_data.csv")

with open(election_csv_path,newline="")as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    election_list={}
    new_list={}
    winner_name=""
    winner_value=0
    total=0
    # Read the row
    for row in csv_reader:
        # compare each candidate if present in the election_list
        # candidates as key add the number of votes casted to each candidate
        if row[2] not in election_list:
            # candidates as key add the number of votes casted to each candidate
            election_list[row[2]]=1
        else:
            # candidates as key add the number of votes casted to each candidate
            election_list[row[2]]+=1
    # extract the number of votes casted which is stores as values to each key in the dictionary
    values=election_list.values()
    # add all the votes casted in the election poll
    total=sum(values)
    for name,value in election_list.items():
        percentage=""
        # compare the number of votes for each candidate to find the winner
        if winner_value < value :
            winner_name=name
            winner_value=value
        # calculate the percentage and add the value and percentage to dictionary with name as key
        percentage=str(round(Decimal(value/total*100),3))
        new_list[name]=(value,percentage)
#prints to results.txt file
output_file = os.path.join('Output', 'results' + '.txt')   
with open(output_file, 'w') as textfile:
    textfile.writelines('Election Results'+'\n')
    textfile.writelines('----------------------------'+'\n')
    textfile.writelines('Total Votes: '+str(total)+'\n')
    textfile.writelines('----------------------------'+'\n')
    for k,v in new_list.items():
        textfile.writelines(k+' : '+ str(v[1])+'% '+'('+str(v[0])+') \n')

    textfile.writelines('----------------------------'+'\n')
    textfile.writelines('Winner: '+ winner_name +'\n')
    textfile.writelines('----------------------------'+'\n')    
#print (str(total),new_list)
#prints file to terminal from result.txt file
with open(output_file, 'r') as readfile:
    print(readfile.read())