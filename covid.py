# rate = input("What is the infection rate?")

# while(not rate.isdigit()):
#     rate = input("Not a digit. What is the infection rate?")

import math


def infections_at_x_days(infections, rate, x):
    for i in range (0, x):
        infections = infections * rate
        print(i, infections)
    return infections

students_at_14_days = infections_at_x_days(7, 1.2, 14)
print(math.floor(students_at_14_days) * 9972)
