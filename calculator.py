#A simple calculator in Python!
# asking the user for input: the first number using 'float()'
num1 = float(input("Enter the first number: "))
#Input the second float number value
num2 = float(input("Enter the second number: "))

#addding, subtracting, multiplying(product) and dividing the two values
sum_result=num2+num1
difference_result = num1 - num2
product_result = num1 * num2
division_result = num2 / num1

#Output of the operations:
print(f"Results of the two values:..")
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient/ Division: {division_result}")
