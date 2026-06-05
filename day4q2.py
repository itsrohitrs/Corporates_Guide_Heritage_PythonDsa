product_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Unit: "))

total_cost = quantity * price
gst = total_cost * 0.18
final_bill = total_cost + gst

print("\ BILL ")
print(f"Product Name : {product_name}")
print(f"Quantity     : {quantity}")
print(f"Price/Unit   : Rs.{price:.2f}")
print(f"Total Cost   : Rs.{total_cost:.2f}")
print(f"GST (18%)    : Rs.{gst:.2f}")
print(f"Final Bill   : Rs.{final_bill:.2f}")