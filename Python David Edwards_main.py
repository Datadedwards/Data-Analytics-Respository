import csv
import os

budget_df = os.path.join("Resources","budget_data.csv")

i = 0
diff = []
total = 0
change = 0
minvalue = 0
maxvalue = 0
average = 0
pandl = []



with open(budget_df, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    month_count = sum(1 for month in csvfile)


with open(budget_df, newline="") as csvfile:
    csv_header = next(csvfile)
    
    for row in csv.reader(csvfile):
        total += int(row[1])
        change -= int(row[1])

with open(budget_df, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv.reader(csvfile):
        value = float(row[1])
        minvalue = min(minvalue, value)
        maxvalue = max(maxvalue, value)

with open(budget_df, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    average = int(total/month_count)
       
#counter 

    
i = 0


with open(budget_df, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)   
    for row in (csvreader):
        
        pandl.append(row[1])

        if i > 0:
            diff.append(int(pandl[i]) - int(pandl[i-1]))
            
        i = i + 1

sum_diff = sum(diff)

avg_per_month = sum_diff/month_count

clean_avg = round(avg_per_month, 2)

        
print("Financial Analysis")
print("--------------------")       
print(f"Total Months: {month_count}")       
print(f"Total: ${total}")
print(f"Average per month: ${clean_avg}")
print(f"Greatest Increase in Profits: " + "${:}".format(maxvalue))
print("Greatest Decrease in Profits: " + "${:}".format(minvalue))
    

#file = open("main.txt", "w")
#file.write("Financial Analysis")
#file.write("\n")
#file.write("--------------------")
#file.write("\n")
#file.write(f"Total Months: {month_count}")
#file.write("\n")
#file.write(f"Total: ${total}")
#file.write("\n")
#file.write(f"Average per month: ${average}")
#file.write("\n")
#file.write("Greatest Increase in Profits: " + "${:}".format(maxvalue) +")")
#file.write("\n")
#file.write("Greatest Decrease in Profits: " + "${:}".format(minvalue) +")")
#file.write("\n")

#file.close()


