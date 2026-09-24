#James Caulder
#09/23/26
#P1HW1
#Writing a program to calculate exponents and add and subtract values

print("-----Calculating Exponents----\n\n")
baseValue = input("Enter an integer as the base value: ")
exponentValue = input("Enter an integer as the exponent: ")
resultValue = int(baseValue)**int(exponentValue)
print("\n" + baseValue,"raised to the power of", exponentValue, "is", resultValue, "\n\n-----Addition and Subtraction----\n")
baseValue = input("Enter a starting integer: ")
additionValue = input("Enter an integer to add: ")
subtractionValue = input("Enter an integer to subtract: ")
resultValue = int(baseValue)+int(additionValue)-int(subtractionValue)
print("\n" + baseValue, "+", additionValue, "-", subtractionValue, "is equal to", str(resultValue))

