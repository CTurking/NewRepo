"""
Your module description
# """
# lName = (1, "apple", "Doctor")
# for i in lName:
#     print(i)

# var1 = "print"
# var2 = "Charlie"    
# print("This statement will {} your name as {}.".format(var1, var2))

# # Files

# print("Working with Files")
# f = open('python1','w')
# f.write('Hello from Python!!\n')
# f.write('Working wih files is easy...\n')
# f.write('It is cool ...\n')
# f.close

# print("Reading file")
# f=open('python1','r')
# line1=f.readline()
# line2=f.readline()
# line3=f.readline()
# print('-----')
# print(line1, end='')
# print(line2, end='')
# print(line3, end='')
# f.close()
# # ##

# f=open('python1','r')
# i=0
# for line in f:
#     print(i,":", line, end='')
#     i=i+1
# f.close()
# # ##
# f=open('python1','r')
# l=[line.upper() for line in f]
# f.close()
# print(l)
# ##
# f=open('python1','r')
# try:
#     for line in f:
#         print(line, end='')
# finally:
#     f.close()
#
# with open('python1','r') as f:
#     print("Last example")
#     for line in f:
#         print(line, end='')



var1 = 0
print(var1)
var1 += 10
if var1 == 10:
    print("Yep its 10")
else:
    print("nope")
var1 = var1 + 1
print(var1)
var1 -= 1
print(var1)


