#Import OS module
import os

#Import module to read CSV
import csv

import sys

#Set path for source file
CSV_PATH = os.path.join ('Resources', 'budget_data.csv')

#Open and read CSV
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:

#Specify delimiter and CSV reader
    csvreader = csv.reader(csvfile, delimiter=",")

#Read header row, store it
    csv_header = next(csvreader)

#Declare variables
    months = 0
    net_total = 0
    previous_profit = ""
    change = 0
    total_change = 0
    change_periods = 0

#Declare and initiate lists and dictionaries
    date_list = []
    profit_loss_list = []
    changes_list = []
    increase = {"date":"", "amount":0}
    decrease = {"date":"", "amount":0}

#Loop though data
    for row in csvreader:

#Create lists to store individually
        date_list.append(row[0])
        profit_loss_list.append(row[0])

#Calculate Net Total Amount
        net_total += int(row[1])

#Calculate Profit Loss
        profit_loss = int(row[1])

#Exclude through if statement
        if previous_profit != "":

#Calculate change and add to list
            change = profit_loss - previous_profit
            changes_list.append(change)

#Calculate change by adding all change
            total_change += int(change)

        previous_profit = profit_loss

#Calculate greatest increase for entire period
        if change > increase["amount"]:
            increase["amount"] = change
            increase["date"] = row[0]

        if change < decrease["amount"]:
            decrease["amount"] = change
            decrease["date"] = row[0]

#Calculate number of months
months = len(date_list)

#Calculate averages of all changes
change_periods = len(changes_list)
average_change = round((total_change / change_periods), 2)

#Print results
print(f'Financial Advisor')
print(f'----------------------------')
print(f'Total Months: {months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {increase["date"]} (${increase["amount"]})')
print(f'Greatest Decrease in Profits: {decrease["date"]} (${decrease["amount"]})')

#Create output text file and set path
output = os.path.join("python-challenge", "PyBank", "Analysis", "budget_analysis.txt")

#Open file in write mode and write requested results
def writeNums(args: any):
    with open("python-challenge", "PyBank", "Analysis", "budget_analysis.txt", "a"):
        print(f"Financial Advisor\n\n")
        print(f"----------------------------\n\n")
        print(f"Total Months: {months}\n\n")
        print(f"Total: ${net_total}\n\n")
        print(f"Average Change: ${average_change}\n\n")
        print(f"Greatest Increase in Profits: {increase["date"]} (${increase["amount"]})\n\n")
        print(f"Greatest Decrease in Profits: {decrease["date"]} (${decrease["amount"]})\n\n")