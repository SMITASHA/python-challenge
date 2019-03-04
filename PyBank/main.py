import os
import csv
#from datetime import datetime as dt
from decimal import Decimal


# Define the function 
#def getMonth(date0):

#Declare the path

budget_csv_path = os.path.join("..","Resources","budget_data.csv")

with open(budget_csv_path,newline="") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    # initilize the variables
    date1=""
    total=0
    max_profit_increase=0
    date_max=""
    min_profit_decrease=0
    date_min=""
    for row in csv_reader:
        # for every row, capture income change, income change total,previous income
        if  date1=="":
            #date1= str(dt.strptime(row[0],"%b-%y"))
             date1= row[0]
             month=1
             cnt=0
             prev_income=int(row[1])
             income_change=0
             avg_change_total=0
        else:
            # for every new date , add months
            date2=row[0]
            if date1!=date2:
                month+=1
                date1=date2
                date2=""
            # capture income change by substracting previous income from current income
            income_change=int(row[1])-prev_income
            avg_change_total=income_change+avg_change_total
            cnt+=1
            prev_income=int(row[1])
            if income_change>max_profit_increase:
                max_profit_increase=income_change
                date_max=row[0]
            if income_change<min_profit_decrease:
                min_profit_decrease=income_change
                date_min=row[0]
            

        # sum all the profit/loss in the file
        profit_Loss=row[1]
        total=total+int(profit_Loss)
             
    # After all the rows are average change is captures 
    # average change= sum of(all the changes)  devided by (tatal number of changes ie. count of tatal rows-1)
    avg_change=round(Decimal(avg_change_total/cnt),2)

#prints to output folder in results.txt file
output_file = os.path.join('Output', 'results' + '.txt')   
with open(output_file, 'w') as textfile:
    textfile.writelines("\n")
    textfile.writelines ("Financial Analysis"+'\n')
    textfile.writelines ("----------------------------"+'\n')
    textfile.writelines("Total Months: "+ str(month)+'\n')
    textfile.writelines("Total: $"+ str(total)+'\n' )
    textfile.writelines("Average  Change: $"+ str(avg_change)+'\n' )
    textfile.writelines("Greatest Increase in Profits: "+str(date_max)+" ($" +str(max_profit_increase)+")"+'\n')
    textfile.writelines("Greatest Decrease in Profits: "+str(date_min)+" ($"+str(min_profit_decrease)+")" +'\n')

#prints file to terminal from result.txt file
with open(output_file, 'r') as readfile:
    print(readfile.read())

