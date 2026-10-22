#James Caulder
#10/21/26
#P3HW2
#This program calculates the gross pay (including overtime) for an employee based on their hours worked and hourly wage.


#Gets the employee's name, hours worked, and pay rate from the user
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
#Finds how many hours are regular and how many are overtime, then calculates the overtime pay.
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
else:
    regular_hours = hours_worked
    overtime_hours = 0
    overtime_pay = 0
#Calculates the regular pay and gross pay.
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay
#prints the results.
print("-" * 37)
print(f"Employee name:   {employee_name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<12}")
print("-" * 97)
print(f"{hours_worked:<15.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<20.2f}${regular_pay:<19,.2f}${gross_pay:,.2f}")
