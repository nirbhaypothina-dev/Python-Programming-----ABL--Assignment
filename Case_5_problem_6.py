# Case 5 - Problem 6: Railway Fare and Reservation Calculator

dist = float(input("Enter Travel Distance (km): "))

if dist <= 300:
    base_fare = dist * 1.5
else:
    base_fare = dist * 1.2

passengers = [
    ("Suresh", 34, "3AC", "NO"),
    ("Lakshmi", 65, "3AC", "NO"),
    ("Chintu", 9, "SL", "NO"),
    ("Vikram", 42, "2AC", "YES")
]

total_amount = 0
print("-- Passenger Fare Details ---")

for p in passengers:
    name, age, p_class, cancel = p

    if p_class == "SL":
        mult = 1.0
        res_fee = 40
    elif p_class == "3AC":
        mult = 2.0
        res_fee = 60
    else:
        mult = 3.0
        res_fee = 80

    fare = base_fare * mult

    if age < 12:
        fare = fare * 0.50
    elif age >= 60:
        fare = fare * 0.60

    ticket_cost = fare + res_fee

    if cancel == "YES":
        final_pay = ticket_cost * 0.25
        status = "Cancelled"
    else:
        final_pay = ticket_cost
        status = "Confirmed"

    total_amount = total_amount + final_pay
    print(name, "| Class:", p_class, "| Booked:", round(ticket_cost, 2), "| Status:", status, "| Payable:", round(final_pay, 2))

print("Total Amount Payable:", round(total_amount, 2))
