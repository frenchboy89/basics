
#add_two_numbers
def add_two_numbers(number1,number2):
    total=number1+number2
    print(f"the total number for {number1} and {number2} is {total}")
# add_two_numbers(60,27) 

 #multiply_two_numbers
def multiply_two_numbers (number4,number5):
    total=number4*number5
    print(f"the total number for {number4} and {number5} is {total}")
# multiply_two_numbers(60,20)

 #divide_two_numbers
def divide_two_numbers(number2,number7):
    total=number2*number7
    print(f"the total number for {number2} and {number7} is {total}")
# divide_two_numbers(2,20)

  #get_square 
def get_square(number11):
    total=number11**2
    print(f"the total number for {number11} and  is {total}")
# get_square(60)

#get_square_of_total_number
def get_square(number11,number12):
    total=number11**2,number12**2
    print(f"the total number for {number11} and  {number12}  is {total}")
# get_square(60,20)

def add_and_substract_numbers (number1,number2,number3):
    total=number1+number2-number3
    print(f"the total number for {number1} plus {number2} minus {number3} is {total}")
# add_and_substract_numbers(60,20,5)


"""write a function to find the square root of a number
using python"""

def square_root_a_number(digit):
    square_root_a_number=digit**0.5
    print(f"the square root of  {digit}  is {square_root_a_number}")
#square_root_a_number(25)

#function with default argument

def addition_of_two_number(figure,digit=3):
    addition_of_two_number=figure+digit
    print(f"The total number for {figure} plus {digit} is {addition_of_two_number} ")
#addition_of_two_number(4)  


#another example 1 of addition_of_two_number
def addition_of_two_number(figure=5,digit=3):
    addition_of_two_number=figure+digit
    print(f"The total number for {figure} plus {digit} is {addition_of_two_number} ")
#addition_of_two_number(4) 


#another example 2 of addition_of_two_number
def addition_of_two_number(figure=7,digit=8):
    addition_of_two_number=figure+digit
    print(f"The total number for {figure} plus {digit} is {addition_of_two_number} ")
addition_of_two_number(4,9)





















