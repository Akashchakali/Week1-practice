# Movie Ticket Booking Summary

customer_name = input("Enter customer name: ")
age = int(input("Enter age: "))
number_of_tickets = int(input("Enter number of tickets: "))

# Determine ticket price based on age
if age < 12:
    ticket_price = 120
elif age <= 59:
    ticket_price = 200
else:
    ticket_price = 150

# Calculate total before discount
total_before_discount = ticket_price * number_of_tickets

# Calculate discount
if number_of_tickets >= 5:
    discount = total_before_discount * 0.10
else:
    discount = 0

# Calculate final amount
final_amount = total_before_discount - discount

# Display booking summary
print("\n----- Movie Ticket Booking Summary -----")
print("Customer Name:", customer_name)
print("Ticket Price: ₹", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Total Before Discount: ₹", total_before_discount)
print("Discount: ₹", discount)
print("Final Amount: ₹", final_amount)

    
    

    
    