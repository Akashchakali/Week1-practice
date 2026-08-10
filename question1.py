parking_hours = int(input("Enter the parking hours: "))

if parking_hours <= 2:
    parking_charge = parking_hours * 30
elif parking_hours <= 5:
    parking_charge = parking_hours * 25
else:
    parking_charge = parking_hours * 20

service_charge = 0
if parking_charge > 150:
    service_charge = 20

final_amount = parking_charge + service_charge

print(f"Parking Charge: {parking_charge}")
print(f"Service Charge: {service_charge}")
print(f"Total Charge: {final_amount}")