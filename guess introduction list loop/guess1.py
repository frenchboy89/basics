# Print First 10 natural numbers using for loop

# for number in range(0, 11):
#     print(number)

# Write a program to print the following number pattern using a loop.

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""

# for number in range(1, 6):
#     start = 1
#     for digit in range(start, number+1):
#         print(digit, end=" ")
#     print("\n")
# Calculate the sum of all numbers from 1 to a given number

# user_input = int(input("""Enter A Number Here..)
# and we will get the sum from 1 to the number for you\n"""))

# sums = 0

# for number in range(1, user_input+1): # 7
#     sums += number


# print(f"The sum of numbers from 1 to {user_input} is {sums}")

# Write a program to print multiplication table of a given number

# user_input = int(input("""
# Enter A number here and we will get you the
# multiplication Table from 1 to 5
# """))

# for number in range(1, 6): # 4
#     table = user_input * number
#     print(f'{user_input} multiplied by {number} is {table}')
"""
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
"""

list_number1 = [200, 140, 30, 400, 700]

for number in list_number1:
    if number < 150 and number % 5 == 0:
        print(number)
    elif number > 500:
        break
    elif number > 150:
        continue
    else:
          print("")
