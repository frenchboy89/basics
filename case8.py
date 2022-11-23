"""A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not."""

number_of_classes_held = int(input("How many class was held? ")) # 100
number_of_classes_attended = int(input("How many class did you attend? ")) # 25

percentage_attendace = (number_of_classes_attended / number_of_classes_held) * 100 # 25


"""A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not."""

number_of_classes_held = int(input("How many class was held? ")) # 100
number_of_classes_attended = int(input("How many class did you attend? ")) # 25

percentage_attendace = (number_of_classes_attended / number_of_classes_held) * 100 # 25
"""A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not."""

number_of_classes_held = int(input("How many class was held? ")) # 100
number_of_classes_attended = int(input("How many class did you attend? ")) # 25
percentage_attendace = (number_of_classes_attended / number_of_classes_held) * 100 # 25

if percentage_attendace >= 75:
    print(percentage_attendace)
    print("Will attend the exam")
else:
    print(percentage_attendace)
    print("Will not attend the exam")
# Modify the above question to allow student to sit if he/she has medical cause. 
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

medical_cause = input("Do you have a medical cause? please choose 'y' for yes and 'n' for no. ")
print(medical_cause.capitalize())
"""A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not."""

number_of_classes_held = int(input("How many class was held? ")) # 100
number_of_classes_attended = int(input("How many class did you attend? ")) # 25

percentage_attendace = (number_of_classes_attended / number_of_classes_held) * 100 # 25


"""A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not."""

number_of_classes_held = int(input("How many class was held? ")) # 100
number_of_classes_attended = int(input("How many class did you attend? ")) # 25

percentage_attendace = (number_of_classes_attended / number_of_classes_held) * 100 # 25
"""A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not."""

number_of_classes_held = int(input("How many class was held? ")) # 100
number_of_classes_attended = int(input("How many class did you attend? ")) # 25
percentage_attendace = (number_of_classes_attended / number_of_classes_held) * 100 # 25

if percentage_attendace >= 75:
    print(percentage_attendace)
    print("Will attend the exam")
else:
    print(percentage_attendace)
    print("Will not attend the exam")
# Modify the above question to allow student to sit if he/she has medical cause. 
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

medical_cause = input("Do you have a medical cause? please choose 'y' for yes and 'n' for no. ")
print(medical_cause.capitalize())
if medical_cause.lower() == "y":
    print(medical_cause)
    print("User will sit for exam")
elif medical_cause.lower() == "n":
    print("User will not sit for exam")
else:
    print("Wrong input!")