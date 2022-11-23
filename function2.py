""" Write a Python function to find the Max of four numbers
Write a Python function to sum all the numbers in a list
Write a Python function to multiply all the numbers in a list
Write a Python function to check whether a number falls in a given range
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
"""






# Write a Python function to find the Max of four numbers 

four_number=[30,40,20,10]
print(max(four_number))  

#using def in max
def four_number(digit):
    print(max(digit))

four_number([2,70,20,10])

#using def in min
def Max_of_four_numbers(figures):
    print(min(figures))

Max_of_four_numbers([59,21,12,60])

#Write a Python function to sum all the numbers in a list
lists = [12, 54, 300, 99, 20]
sums = 0
for number in lists:
    sums += number
#print(f"The sum of numbers  in a list to {lists} is {sums}")

def sum_list(number):
    sum_item=0
    for i in number:
        sum_item+=i
    print( sum_item)

sum_list([35,70,2])


#another method to check the sum of number in a list
def sum_numbers(numbers):
     total = 0
     for number in numbers:
        total += number
     return total


print(sum_numbers([1, 2, 3, 4, 5]))

#Write a Python function to multiply all the numbers in a list 
def lists_multiply(numbers):
    variable=1
    for number in numbers:
        variable=variable*number
    return variable
print(lists_multiply([2,3,4,4]))


#Write a Python function to multiply all the numbers in a list (another method)

def lists_multiply(numbers):
    variable=1
    for number in numbers:
        variable=variable*number
    print(variable)
lists_multiply([2,3,4,4])

"""Write a Python function to check whether a number falls in a given range
 input=>[1,2,2,3,4,5,7,5,4,4,4,7,9] output=>[1,2,3,4,5,7,9]""" 
common_occurences = {1,2,2,3,4,5,7,5,4,4,4,7,9}
print(common_occurences)


    











