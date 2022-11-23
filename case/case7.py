
# Take input of age of 3 people by user and determine oldest and youngest among them.

userA = int(input("Enter Your Age here... ")) # 30
userB = int(input("Enter Your Age here... ")) # 22
userC = int(input("Enter Your Age here... ")) # 24


if userA > userB and userA > userC:
    if userC > userB:
        print(userA,"is the oldest")
        print(userB,"is the youngest")
    else:
        print(userA,"is the oldest")
        print(userC, "is the youngest")
elif userB > userA and userB > userC:
    if userA > userC:
        print(userB,"is the oldest")
        print(userC,"is the youngest")
    else:
        print(userB,"is the oldest")
        print(userC, "is the youngest")
else:
    if userA > userB:
        print(userC, "is the oldest")
        print(userB, "is the youngest")
    else:
        print(userC, "is the oldest")
        print(userA, "is the youngest")


"""Write a program to print absolute vlaue of a number entered by user. E.g.
INPUT: 1        OUTPUT: 1
INPUT: -1        OUTPUT: 1
"""

user_input = int(input("Enter A number here... ")) # -2

if user_input < 0:
    print(user_input * -1)
else:
    print(user_input)





    