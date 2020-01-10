# import CSV

import csv
import os

#read file in dictionary format

#variables



  
    

with open(r"C:\Users\david\Desktop\budget_file.csv", 'r') as budget_file:
    budget_file = csv.DictReader(budget_file)

#variables
    
    total_change_profits = 0
    greatest_increase = 0
    initial_profit = 0
    monthly_changes = []

#Total Month

    totalrevenue = 0
    date_list = [] 

    for line in budget_file:
        date_list.append(line["Date"]) 

    
#Total Revenue

        totalrevenue += int(line["Profit/Losses"])

        
#Profit/Losses Average Change
#average_revenue = totalrevenue/len(date_list)   
         
monthly_change_profits = totalrevenue - initial_profit
# N/A = 38 million - 0

monthly_changes.append(monthly_change_profits)
#list

total_change_profits += monthly_change_profits
# 38 million

initial_profit = totalrevenue
# 38 million

average_change_profits = (total_change_profits/86)


#net_revenue = totalrevenue - sum(int("Profit/Losses" < 0))

#Greatest Profit Increase

#greatest_increase = max((line["Profit/Losses"])

#Greatest Profit Decrease

#greatest_decrease = min("Profit/Losses")


print(len(date_list))
print(totalrevenue)
#print(average_revenue)
print(average_change_profits)