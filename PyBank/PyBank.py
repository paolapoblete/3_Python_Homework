import os
import csv

csvpath = os.path.join('budget_data.csv')

data_info = []
money_counter = 0
change_value = []

with open(csvpath, 'r') as csvfile:
    data_list = csv.reader(csvfile)
    h = csvfile.readline()
    for line in data_list:
        data_info.append(line)
print("Financial Analysis")

print("-----------------------------------")

#for month in data_info:
print("Months total: " + str(len(data_info)))

for entry in data_info:
    money_counter += int(entry[1])

#total amount of profit/losses
print("Total: $" + str(money_counter))


previous_value = 0
biggest_changevalue = -99999999999999999999999

opening_amount = data_info[0][1]
closing_amount = data_info[len(data_info) - 1][1]

average_change = (int(closing_amount) - int(opening_amount)) / (len(data_info) - 1)
print("Average Change: $" + str(round(average_change, 2)))


#Greatest Increase in Profits

biggest_month_info = ""

for entry in data_info:
    #calculate the difference in between the current month you are reading 
    #and the previous month
    change = int(entry[1]) - int(previous_value)
    #check if that change is the biggest change so far
    if change > biggest_changevalue:
        #if that change was the biggest, save the 
        biggest_month_info = entry[0]
        biggest_changevalue = change
    previous_value = entry[1]
    
#print(biggest_changevalue)
#print(biggest_month_info)
print("Greatest Increase in Profits: " + biggest_month_info + " " + "($" + str(biggest_changevalue) + ")")

#Greatest Decrease in Profits:

smallest_changevalue = 99999999999999999999999999999999
smallest_month_info = ""
previous_value = 0


for entry in data_info:
    change = int(entry[1]) - int(previous_value)
    if change < smallest_changevalue:
        smallest_month_info = entry[0]
        smallest_changevalue = change
    previous_value = entry[1]


#print(smallest_changevalue)
#print(smallest_month_info)
print("Greatest Decrease in Profits: " + smallest_month_info + " " + "($" + str(smallest_changevalue) + ")")

print("------------------------------------")













    
    
    
    
    
         

                
