# import CSV

import csv

#read file in dictionary format

with open(r"C:\Users\david\Desktop\budget_file.csv", 'r') as budget_file:
    budget_file = csv.DictReader(budget_file)

#variables



#Total Month

    totalrevenue = 0
    date_list = []   

    for line in budget_file:
        date_list.append(line["Date"]) 

        print(len(date_list))
    
#Total Revenue

        totalrevenue = totalrevenue + int(line["Profit/Losses"])

        print(totalrevenue)



#Greatest Increase and Decrease

#Greatest Profit Increases

#Greatest Loss Decrease



