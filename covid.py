#Julia Fasick, Logan Small, Chili Ramgolam, Nick Simons

import math

days = input("How many days should be calculated for? ")

while(not days.isdigit() or int(days) < 14):
     days = input("Not a digit or less than 14 entered. What is the number of days to calculate for?")

def infections_at_x_days(infections, rate, x):
    for i in range (0, x):
        infections = math.floor(infections) * rate
    return math.floor(infections)

def money_lost(n):
    return n*9972

def percentage(n):
    return n/39740

students_at_14_days = infections_at_x_days(7, 1.2, 14)
print("After 14 days, there will be " + str(students_at_14_days) + " infections. This is {0:.2f}% of the Temple student population.".format(percentage(students_at_14_days) * 100))
print("This costs Temple ${0:.2f} in refunds.".format(money_lost(students_at_14_days)))

students_after_14_days = infections_at_x_days(students_at_14_days, 1.2, int(days) - 14)
print("At {0:f} days, there will be ".format(int(days)) + str(students_after_14_days) + " infections. This is {0:.2f}% of the Temple student population.".format(percentage(students_after_14_days) * 100))


