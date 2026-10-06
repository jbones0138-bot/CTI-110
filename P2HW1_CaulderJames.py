#James Caulder
#10/06/26
#P2HW1
#Formatting my previous program to make it look better.

print("This program calculates and displays travel expenses")
budgetValue = int(input("Enter Budget: \n"))
destinationString = input("Enter your travel destination: \n")
gasValue = int(input("How much do you think you'll spend on gas? \n"))
accomodationValue = int(input("Approximately, how much will you need for accomodation/hotel? \n"))
foodValue = int(input("Last, how much do you need for food? \n"))
finalBalance = budgetValue - gasValue - foodValue - accomodationValue
print("-" * 9 + "Travel Expenses" + "-" * 9)
print(f'{"Location:":18s} {destinationString}')
print(f'{"Initial Budget:":18s} ${budgetValue:.2f}')
print(f'{"Fuel:":18s} ${gasValue:.2f}')
print(f'{"Accomodation:":18s} ${accomodationValue:.2f}')
print(f'{"Food:":18s} ${foodValue:.2f}')
print("-" * 33)
print(f'{"Remaining Balance:":18s} ${finalBalance:.2f}')