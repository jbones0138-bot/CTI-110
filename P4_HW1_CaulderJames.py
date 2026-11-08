#James Caulder
#11/07/2026
#P4HW1
#Collect scores, drop the lowest, and display the average and letter grade.

#Ask how many scores the user wants to enter.
numScores = int(input("How many scores do you want to enter? "))

#Create an empty list to store valid scores.
gradeList = []

#Get each score and check that it is between 0 and 100.
for item in range(1, numScores + 1):
    score = float(input(f"Enter score #{item}: "))

    #Keep asking for the same score until it is valid.
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{item} again: "))

    gradeList.append(score)

#Find the lowest score and remove it from the list.
lowestScore = min(gradeList)
gradeList.remove(lowestScore)

#Calculate the average of the remaining scores.
average = sum(gradeList) / len(gradeList)

#Determine the letter grade for the average.
if average >= 90:
    letterGrade = "A"
elif average >= 80:
    letterGrade = "B"
elif average >= 70:
    letterGrade = "C"
elif average >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

#Display the results.
print("\n" + ("-" * 18) + "Results" + ("-" * 16))
print(f"{'Lowest Score':15}: {lowestScore:.1f}")
print(f"{'Modified List':15}: {gradeList}")
print(f"{'Scores Average':15}: {average:.2f}")
print(f"{'Grade':15}: {letterGrade}")
print("-" * 40)