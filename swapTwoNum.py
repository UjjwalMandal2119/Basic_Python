num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp=num1
num1=num2
num2=temp
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)

#without using third variable
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("After swapping (without third variable):")
print("First number:", num1)
print("Second number:", num2)

# Pythonic Way (Best)

# Python provides a built-in way to swap variables:
num1, num2 = num2, num1
print("After swapping (Pythonic way):")
print("First number:", num1)
print("Second number:", num2)