import os
import csv

csvfile = os.path.join("Py_Bank.csv")


date=[]
profit_loss=[]

with open(csvfile, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) 
    for row in csvreader:
            date.append(row[0])
            profit_loss.append(row[1])

print ("Financial Analysis")
print ("----------------------------")

#Total months
total_months = len(date)

print (f"Total Months: " + str(total_months))

#total profit
profit_loss = [int(i) for i in profit_loss]
total_profit = sum(profit_loss)
total_formated='${:,.2f}'.format(total_profit)

print (f"Total: "+ str(total_formated))

#average change

monthly_change = []
months = range(len(date)-1)
for month in months:
    monthly_change.append(int(profit_loss[month+1]) - int(profit_loss[month]))
count_months = len(date)-1
avg_change = sum(monthly_change) / count_months
avg_change_formatted = '${:,.2f}'.format(avg_change)
print("Average change: " + str(avg_change_formatted))

#greatest increase

greatest_increase = 0
greatest_increase_month_index = 0

for month in months:
    if monthly_change[month]>greatest_increase:
        greatest_increase = monthly_change[month]
        greatest_increase_month_index = month + 1

greatest_increase_month = date[greatest_increase_month_index]
greatest_increase_formatted = '${:,.2f}'.format(greatest_increase)
print(f"Greatest increase: {greatest_increase_formatted} ({greatest_increase_month})")

#greatest decrease
greatest_decrease = 0
greatest_decrease_month_index = 0

for month in months:
    if monthly_change[month]<greatest_decrease:

        greatest_decrease = monthly_change[month]
        greatest_decrease_month_index = month + 1
        
greatest_decrease_month = date[greatest_decrease_month_index]
greatest_decrease_formatted = '${:,.2f}'.format(greatest_decrease)
print(f"Greatest increase: {greatest_decrease_formatted} ({greatest_decrease_month})")
print("------------------------------------")   


output_file = os.path.join("bank1_data.txt")
with open('bank_data.txt', 'w') as f:
         f.write('Finansial Analysis')
         f.write('---------------------')
         f.write(" Total Months: " + str(total_months))
         f.write(" Total: "+ str(total_formated) )
         f.write(" Average change: " + str(avg_change_formatted))
         f.write(" Greatest increase: " + str(greatest_increase_formatted)+ str({greatest_increase_month}))
         f.write(" Greatest increase: "+ str(greatest_decrease_formatted)+ str({greatest_decrease_month}))