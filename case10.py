#Challenge = #1: Iterate through every number in a list to separate out even and odd numbers.Identify possible outlier values as well.
"""even_number = []
odd_number = []
my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
for number in my_list:
    if number % 2 == 0:
        even_number.append(number)
    else:
        odd_number.append(number)

print(even_number)
print(odd_number)"""
#Challenge #2: Find the sum of all numbers in a list
"""lists = [12, 54, 300, 99, 20]
sums = 0
for number in lists:
    sums += number
print(f"The sum of numbers  in a  {lists} is {sums}")"""

#Challenge 3= Calculate the sum of even numbers in a list
list3 = [300, 11, 22, 19, 190, 10, 15, 1]
even_number = []
for number in list3:
     if number % 2 == 0:
        even_number.append(number)
sums = 0
for number in even_number:
    sums += number
print(f"The sum of numbers  in a list to {even_number} is {sums}")

#Challenge 4: Count the number of even numbers in a list
"""list4 = [300, 11, 22, 19, 190, 10, 15, 1,7,8,10,44,88,100]
even_number = []
for number in list4:
    if number % 2 == 0:
        even_number.append(number)
        print(even_number)
        print(len(even_number))"""

        #Challenge 3= Calculate the sum of even numbers in a list
list3 = [300, 11, 22, 19, 190, 10, 15, 1]
even_number = []
# for number in list3:
#     if number % 2 == 0:
#         even_number.append(number)

# print(even_number)
# print(sum(even_number))
# total_even = 0

# for number in list3:
#     if number % 2 == 0:
#         total_even += number

# print(total_even)
# #Challenge 4: Count the number of even numbers in a list
list4 = [300, 11, 22, 19, 190, 10, 15, 1,7,8,10,44,88,100]

count = 0
for number in list4:
    if number % 2 == 0: # check even number
        count += 1

print(f'The total number of even number in {list4} is {count}')


