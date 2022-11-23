#Write a program to use for loop to print the following reverse number pattern
"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""

for number in range(6, 1):
    start = 6
    for digit in range(start, number-1):
         print(digit,end=(""))
         print("\n")

 #Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

