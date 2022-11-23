"""A company decided to give bonus of 12% to
employee if his/her year of service is more
than 3 years. Ask user for their salary and
year of service and print the net bonus amount
"""



"""salary=float(input("what is your salary?  "))
years=int(input("what is your years of services? "))

if years > 3:
    bonus=salary*0.12
    total=bonus+salary
    print(total)
else:
    print(salary)""" 
   
"""
Take values of length and breadth of a rectangle from user and check if it is square or not.


length=float(input("the value of length ? "))
breadth=float(input("the value of breadth ? "))

if length==breadth:
    print("this is a square")
else:
    print("this is not a square ")"""


# Take two int values from user and print greatest among them.

value1 = int(input("Enter the First Value here.. "))
value2 = int(input("Enter the Second Value here.. "))

if value1 > value2:
    print(value1, "is the Greatest")
elif value2 > value1:
    print(value2, "is the greatest")
else:
    print("Numbers are equal")

"""A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade."""


"""marks = int(input("Enter your mark here... "))

if marks <= 25:
    print("F")
elif marks > 25 and marks <= 45:
    print("E")
elif marks > 45 and marks <= 50:
    print("D")
elif marks > 50 and marks <= 60:
    print("C")
elif marks > 60 and marks <= 80:
    print("B")
else:
    print("A")"""

#Take input of age of 3 people by user and determine oldest and youngest among them.
age_1= int(input("enter first age"))
age_2=int(input("enter second age"))
age_3=int(input("enter third age"))


if age_1 > age_2:
    print("age_1 is oldest than age_2 ")
elif age_2 < age_1:
    print("age_2 is younger than age_1 ")
elif age_3 < age_1:
    print("age_3 is oldest than age_1 ")   
elif age_3 < age_2:
    print("age_2 is younger than age_1 ")
else:
    print("age equal")     
        