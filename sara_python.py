"""
Your module description
"""

# This is part1 which will not include function



# Asking for name + verifying that the name isn't empty:

name = ""

while name == "":

    name = input("What's your name ? ")



# Asking for age + only accepting numbers as a value:

age = 0

while age == 0:

    age_str = input("How old are you ? ")

    try:

        age = int(age_str)

    except:

        print(" Error: your age should be a number, please provide your age ")



# Display results :

print(" Your name is " + name + ", you are " + str(age) + " years old")

print(" Next year you will be " + str(age + 1) + " years old")



# This is part2 with functions : same previous program but with functions



# # Introducing a function

# # The functions

# 

# def ask_name():

#     name_answer = ""

#     while name_answer == "":

#         name_answer = input("What's your name ? ")

#     return name_answer

# 

# 

# def ask_age(person_name):

#     age_int = 0

#     while age_int == 0:

#         age_str = input(person_name + " How old are you ? ")

#         try:

#             age_int = int(age_str)

#             # if age_int > 18:

#             #     print("Welcome on board")

#             # elif age_int == 17:

#             #     print("Come back after your next birthday")

#             # else:

#             #     print("Please provide your parental allowance")

#         except:

#             print(" Error: your age should be a number, please provide your age ")

#     return age_int

# 

# 

# # Display personal infos

# # Parameters = name, age

# def display_personal_info(name, age):

#     print(" Hi " + name + ", you are " + str(age) + " years old")

#     print(" Next year you will be " + str(age + 1) + " years old")

#     # print(name1, age1)

#     # print(name2, age2)

#     if age > 18:

#         print("Welcome on board")

#     elif age == 17:

#         print("Come back after your next birthday")

#     else:

#         print("Please provide your parental allowance")

# 

# 

# # Asking for name + verifying that the name isn't empty:

# name1 = ask_name()

# name2 = ask_name()

# 

# # Asking for age + only accepting numbers as a value:

# age1 = ask_age(name1)

# age2 = ask_age(name2)

# 

# 

# # Display results :

# display_personal_info(name1, age1)

# print()

# display_personal_info(name2, age2)

# print()

