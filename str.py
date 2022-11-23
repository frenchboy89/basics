
# name = "Hakeem"

# # + concatenation
# sentence = "My Name is " + name
# desc = "I am " + name + " by name"
# print(sentence)
# print(desc)

# # , concatenation
# details = "I am", name, "again"
# print(details)
# print("I am", name, "again")

new_name = "Henry"
new_age = 30
new_sentence = "My name is"
age_sentence = "I am"
year = "Years Old"

# My name is Henry. I am 30 years old
# Task 1
first_sentence = new_sentence + " " + new_name + ". "
second_sentence = age_sentence + " " + str(new_age)
# Empty string Variable
real_sentence = ""

# Extended or joined Variable
real_sentence += first_sentence
print(real_sentence)

# Extended Variable
real_sentence += second_sentence
print(real_sentence)