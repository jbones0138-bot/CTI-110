#James Caulder
#09/23/26
#P1HW2
#Writing a program to calculate a budget compared to expenses.

print("This program calculates and displays travel expenses")
budgetValue = input("Enter Budget: \n")
destinationString = input("Enter your travel destination: \n")
gasValue = input("How much do you think you'll spend on gas? \n")
accomodationValue = input("Approximately, how much will you need for accomodation/hotel? \n")
foodValue = input("Last, how much do you need for food? \n")
finalBalance = int(budgetValue) - int(gasValue) - int(foodValue) - int(accomodationValue)
print("------------Travel Expenses------------\nLocation: " + destinationString + "\nInitial Budget: " + budgetValue + "\n\nFuel: " + gasValue + "\nAccomodation: " + accomodationValue + "\nFood: " + foodValue + "\n\nRemaining Balance: " + str(finalBalance))