expenses = []
# Step 1: Ask the user to enter new expenses
while True:
    item = input("What did you spend money on? (or type 'done' to finish) ")
    
    if item == "done":
        break
    
    amount = int(input("How much did you spend? "))
    
    expense = {"name": item, "amount": amount}
    expenses.append(expense)

# Step 2: Show all expenses
print("\nHere are all your expenses:")
for expense in expenses:
    print(expense["name"], "-", expense["amount"])

# Step 3: Calculate and show total
total = 0
for expense in expenses:
    total = total + expense["amount"]

print("\nTotal spent:", total)

#Step 4: Save expenses to a file
file = open("expenses.txt", "w")
for expense in expenses:
    line = expense["name"] + " - " + str(expense["amount"]) + "\n"
    file.write(line)
file.close()

print("\nYour expenses have been saved!")