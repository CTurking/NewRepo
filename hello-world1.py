"""
Your module description
"""
# print("hello World")
# Variables declared here
# string_to_print = "Variable a"
# print("string_to_print")
# int_to_print = 10
# print(int_to_print)
# # print("10")

# intVar = 10
# charvar = "Charlie"
# boolVar = True
# floatVar = 100.50

# print(type(intVar), intVar)
# print(type(charvar), charvar)
# print(type(boolVar), boolVar)
# print(type(floatVar), floatVar)
#-------------------------------------

# apples = 2
# oranges = 4
# apples = oranges
# print(apples)

# -------------------------------
#Lists (Lists are mutable - they can be changed)

class_roster = ["Xiulan","Kwaku","Shirley"] 
test_scores = [86,93,80]
print(class_roster) 
print(test_scores)
print("class_roster is a type of ", type(class_roster))
print("Printing first element of class_rooster: ", class_roster[0])


#-----------------------------
#loop thru lists

for student in class_roster: 
    print(student)
print()
for score in test_scores: 
    print(score)
print()
#-----------------------------
# add new elements to list

class_roster.append(("Charlie"))
for student in class_roster: 
    print(student)
print()
class_roster.insert(2,"Natacha")
for student in class_roster: 
    print(student)

# update a list element

print(class_roster[1])
class_roster[1]= "Freddie"
print(class_roster[1])

# -------------------------------
# Touples (Touples are immutable - they can NOT be changed)

# class_roster = ("Xiulan","Kwaku","Shirley")
# test_scores = (86,93,80)
# print(class_roster) 
# print(test_scores)
# print("class_roster is a type of ", type(class_roster))
# print("Printing first element of class_rooster: ", class_roster[0])


# -----------------------------
# Dictionaries

# myDict = {} 
# myDict["one"] = 1 
# myDict["two"] = 2 
# myDict[3] = "three" 
# myDict["four"] = 4.4

# print(myDict[3])
# for key, value in myDict.items(): 
#     print(key, value)
