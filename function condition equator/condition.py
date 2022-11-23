first_number = int(input("Enter a number here. ")) # str
second_number = int(input("Enter Another Number. "))

# if, elif and else

if first_number > second_number:
    print("First Number is greater than second Number")
elif first_number < second_number:
    print("Second Number is greater than first number")
    
else:
    print("Numbers equal")


# Write a Python
# Ask for users input and make it an integer.
# If user input is divisible by 2, print Super Nice
# If user input is divisible by 3, print Nice one
# if user input is divisible by 5, print Great
# if user input is divisible by 7, print awesome
# else print Weird Number

henry = int(input("Enter A number here... "))

if henry % 3 == 0:
    print("Nice one")
elif henry % 5 == 0:
    print("Great")
elif henry % 2 == 0:
    print("super nice")
elif henry % 7 == 0:
    print("Awesome")
else:
    print("Weird Number")
    