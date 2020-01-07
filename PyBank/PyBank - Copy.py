# import CSV

import csv

#read file in dictionary format

with open(r"C:\Users\david\Desktop\budget_file.csv", 'r') as budget_file:
    budget_file = csv.DictReader(budget_file)


   
# make loop 

#for line in budget_file:
    #print(line)

    date_list = []   

    for line in budget_file:
        date_list.append(line["Date"]) 

    print(len(date_list))
    
#need to do .append to add to list 

    for row in budget_file:

        total_month = len(total_month)

    
#need to convert data into dictionary
#need to summarize months

 


