"""
Your module description
"""
# Exercise 1:

def multiplication_or_sum(num1, num2):
     product = num1 * num2     	# calculate product of two number
     if product <= 1000:       		# check if product is less then 1000
          return product
     else: 			# product is greater than 1000 calculate sum
          return num1 + num2

# first invocation 
# result = multiplication_or_sum(20, 30)
# print("The result is", result)

# # Second invocation
# result = multiplication_or_sum(result, 30)
# print("The result is", result)

print(multiplication_or_sum(1,1))

result = multiplication_or_sum(2,2)
print(result)


# def remove_chars(word, n):
#     print('Original string:', word)
#     x = word[n:]
#     return x

# print("Removing characters from a string")
# print(remove_chars("pynative", 4))
# print(remove_chars("pynative", 2))

