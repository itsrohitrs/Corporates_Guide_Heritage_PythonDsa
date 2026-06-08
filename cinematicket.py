# Take input
age = int(input("Enter age: "))
group_size = int(input("Enter group size: "))

# Determine ticket price using nested if
if age >= 18:
    if age >= 60:
        ticket_price = 100
        print("Senior Citizen Ticket")
    else:
        ticket_price = 200
        print("Adult Ticket")
else:
    if age < 5:
        ticket_price = 0
        print("Free Entry")
    else:
        ticket_price = 80
        print("Child Ticket")

# Calculate total bill
total_bill = ticket_price * group_size

# Apply group discount
if group_size > 10:
    discount = total_bill * 0.20
    total_bill = total_bill - discount
    print("20% Group Discount Applied")

# Display bill
print("Ticket Price per Person:", ticket_price)
print("Group Size:", group_size)
print("Final Bill:", total_bill)