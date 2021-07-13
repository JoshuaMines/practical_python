expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = sum(expenses)

print("you spent $", total, "on lunch this week", sep='')

#letting user add 7 expenses
total = 0
expenses = [] 
for i in range (7): #for 7 expenses
    expenses.append(float(input("enter expenses:"))) #take the input and append it to the expense array

total = sum(expenses)

print("you spent $", total, sep='')

#total a varaibale amount of expenses
total = 0
expenses = []
num_expenses = int(input("enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("enter an expense:")))

total = sum(expenses)

print("you spent %", total, sep='')