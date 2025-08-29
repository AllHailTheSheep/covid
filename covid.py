# rate = input("What is the infection rate?")

# while(not rate.isdigit()):
#     rate = input("Not a digit. What is the infection rate?")

import math

def infections_at_x_days(infections, rate, x):
    for i in range (0, x):
        math.floor(infections) = infections * rate

        #print(i, infections)
    return infections

def money_lost(n):
    return n*9972

def percentage(n):
    return n/39740

students_at_14_days = infections_at_x_days(7, 1.2, 14)
#print(math.floor(students_at_14_days) * 9972)
print("money lost: " + money_lost(students_at_14_days))
print("percentage: {0:2f}".format(percentage(students_at_14_days)))

