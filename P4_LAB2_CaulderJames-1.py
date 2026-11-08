#Name: James Caulder
#Date: 11/07/2026
#P4 Lab Two
#Use a while loop and a for loop together

#Set the program to run
run_again = "yes"

#Continue running until the user enters no
while run_again != "no":

    #Get an integer from the user
    user_num = int(input("Enter an integer: "))

    #Determine if the integer is positive or negative
    if user_num >= 0:

        # Display multiplication table from 1 to 12
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")

    else:
        print("This program does not handle negative values.")

    #Ask the user if they want to run the program again
    run_again = input("Would you like to run the program again? ")

#The loop has ended because the user entered no
print("Program is ending...")