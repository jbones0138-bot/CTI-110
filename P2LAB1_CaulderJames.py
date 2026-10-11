#James Caulder
#10/11/26
#P2LAB1
#writing a program to calculate the area, diameter, and circumference of a circle given the radius.

#Import the math module to use math.pi
import math

#Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

#Calculate the diameter
diameter = 2 * radius

#Calculate the circumference
circumference = 2 * math.pi * radius

#Calculate the area
area = math.pi * radius ** 2



#Display the results
print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")