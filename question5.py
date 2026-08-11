# Bus Seat Availability Manager

seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]

# Display all seats
print("----- Current Seat Status -----")

for i in range(len(seats)):
    print("Seat", i + 1, ":", seats[i])

# Ask user to select a seat
seat_number = int(input("\nEnter seat number to book: "))

# Check whether seat number is valid
if seat_number < 1 or seat_number > len(seats):
    print("Invalid seat number.")

else:
    # Convert seat number to list index
    index = seat_number - 1

    if seats[index] == "Available":
        seats[index] = "Booked"
        print("Seat booked successfully.")

    else:
        print("Seat is already booked.")

# Count booked and available seats
booked_count = 0
available_count = 0

for seat in seats:
    if seat == "Booked":
        booked_count += 1
    else:
        available_count += 1

# Display final summary
print("\n----- Seat Summary -----")
print("Total Seats:", len(seats))
print("Booked Seats:", booked_count)
print("Available Seats:", available_count)