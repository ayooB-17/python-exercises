# TASK 1: accept an input and display
# Hello {name}! How are you?
# Where: {name}-is the input

# TASK 2: accept an input of the radius of a circle and print the circumference
# Example
# Radius: 5 //input
# Circumference: 31.1415 //output
# Formula: 2*radius*3.1415


#TASK 1:

student_name = input("What is your name: ")

print("Hello " + student_name + "! How are you?")

#TASK 2:

print("Enter 'x' for exit.")
radius = input("Enter radius of circle: ")
if radius == 'x': exit()
else: radius = float(radius)
circumference = 2*radius*3.1415
print("\nCircumference of Circle =",circumference)