import os
import csv
#locate the file and read it         
budget_csv= os.path.join("Resources", "budget_data.csv")
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader (csvfile, delimiter=",")
    header = next(csvreader)
#Making sure I am actually in the file
    print(header)
# empty lists to count through
    total_months = []
    total_profit = []
    profit_change = []
  # Add the total months and total profit to the right lists
    for row in csvreader :
     total_months.append(row[0])
     total_profit.append(int(row[1]))
  #Print Total Months and Total Profit     
    print(total_months)
    print(total_profit)
    
    for i in range(len(total_profit)-1):
     profit_change.append(total_profit[i+1]-total_profit[i])
     max_increase_profit= max(total_profit)
     min_decrease_profit= min(total_profit)
     max_increase_month = profit_change.index(max(profit_change)) + 1
    max_decrease_month = profit_change.index(min(profit_change)) + 1 
  #Write it all out in the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(total_profit)}")
    print(f"Average Change:${round(sum(profit_change)/len(profit_change),2)}") 
    print(f"Greatest Increase in Profits:{total_months[max_increase_month]} (${(str(max_increase_profit))})")
    print(f"Greatest Decrease in Profits:{total_months[max_decrease_month]} (${(str(min_decrease_profit))})")
  #Print it out to text file
    Budget_text= os.path.join("Resources", "budget.text")
    with open (Budget_text, "w") as text_file:
      output = (
        "Financial Analysis"
        "----------------------------\n"
        f"Total Months: {len(total_months)}\n"
        f"Total: ${sum(total_profit)}\n"
        f"Average Change:${round(sum(profit_change)/len(profit_change),2)}\n" 
        f"Greatest Increase in Profits:{total_months[max_increase_month]} (${(str(max_increase_profit))})\n"
        f"Greatest Decrease in Profits:{total_months[max_decrease_month]} (${(str(min_decrease_profit))})\n")
      text_file.write(output)
    
    
    
  
    
    
    
          
    



  


  





    
    
    
     
  
    
  


  




