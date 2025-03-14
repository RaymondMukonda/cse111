import math

# Get user input for width, aspect ratio, and diameter
width = float(input("Enter the width of the tire in millimeters (e.g., 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

# Calculate the volume using the formula
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display the result
print(f"\nThe approximate volume of the tire is {volume:.2f} liters.")

from datetime import datetime

# Function to calculate the volume of air in a tire
def calculate_tire_volume(width, aspect_ratio, diameter):
    import math
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return round(volume, 2)

# Get user input
width = int(input("Enter the width of the tire in mm: "))
aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
diameter = int(input("Enter the diameter of the wheel in inches: "))

# Compute volume
volume = calculate_tire_volume(width, aspect_ratio, diameter)

# Get current date (without time)
current_date = datetime.today().strftime('%Y-%m-%d')

# Append to volumes.txt
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}\n")

print("Tire volume calculated and saved successfully!")
