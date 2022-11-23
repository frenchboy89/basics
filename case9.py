"""A 4 digit number is entered through keyboard. 
Write a program to print a new number with digits reversed as of orignal one. E.g.-
INPUT : 1234        OUTPUT : 4321
INPUT : 5982        OUTPUT : 2895"""

#new_number= int(input("new number"))




"""Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR"."""

age=input("what is your age?  ")
print(age)
sex=input("what is your sex status ? please choose 'm' for male and 'f' for female. ") 
print(sex.capitalize())
marital_status=input("what is your marital status ?")
print(marital_status.capitalize())
if sex.lower() == "f":
    print("then she will work only in urban areas.")





