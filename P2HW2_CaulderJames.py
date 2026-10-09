#James Caulder
#10/08/26
#P2HW2
#Writing a program to show stats related to grades input by the user.

#Grabbing the grades from the user and storing them in a list.
gradeList = [float(input("Enter grade for module 1: ")), float(input("Enter grade for module 2: ")), float(input("Enter grade for module 3: ")), float(input("Enter grade for module 4: ")), float(input("Enter grade for module 5: ")), float(input("Enter grade for module 6: "))]
#Making the top line and title for the output.
print(("-" * 11) + "Results" + ("-" * 11))
#Displaying the lowest grade of those input by the user. 
print(f"{'Lowest grade:':14} {min(gradeList):.2f}")
#Displaying the highest grade of those input by the user.
print(f"{'Highest grade:':14} {max(gradeList):.2f}")
#Displaying the sum of the grades input by the user.
print(f"{'Sum of grades:':14} {sum(gradeList):.2f}")
#Displaying the average of the grades input by the user.
print(f"{'Average:':14} {sum(gradeList) / len(gradeList):.2f}")
#Making the bottom line for the output.
print("-" * 29)