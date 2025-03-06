"""" 
I currently work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""

# program day of the week from computer.
from datetime import datetime

# The discount rate is 10% and the sales tax rate is 6%.
DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

# Get the subtotal from the user.
subtotal = float(input("Please enter the subtotal: "))

# now() method to get the current date and time as a datetime object from.
current_date_and_time = datetime.now()

# weekday() method to get the day of the week from the current date and time object.
weekday = current_date_and_time.weekday()

# if string.
if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * DISC_RATE, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount

# sales tax.
sales_tax = round(subtotal * SALES_TAX_RATE, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

# adding the subtotal and the sales tax.
total = subtotal + sales_tax

# after all calculations display the total for the user to see.
print(f"Total: {total:.2f}")