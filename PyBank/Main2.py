# import CSV

import csv

#read file in dictionary format

with open('/Users/davidtaboh/Desktop/Python Budget Data.csv', 'r') as budget_file:
    budget_file = csv.DictReader(budget_file)

   
# make loop 

    for line in budget_file:
        print(line)

    for row in budget_file:

        total_month = 0
        total_month = total_month + 1

    

#need to convert data into dictionary
#need to summarize months

 


