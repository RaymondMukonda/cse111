import math

# Get user input for width, aspect ratio, and diameter
width = float(input("Enter the width of the tire in millimeters (e.g., 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

# Calculate the volume using the formula
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display the result
print(f"\nThe approximate volume of the tire is {volume:.2f} liters.")