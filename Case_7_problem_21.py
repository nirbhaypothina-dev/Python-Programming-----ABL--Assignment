# Case 7 - Problem 21: Traffic Violation Penalty Calculator

date = input("Enter Date: ")

# (Vehicle No, Vehicle Type, Offence, Previous Offences)
violations = [
    ("AP16AB1234", "BIKE", "HELMET", 0),
    ("AP39CD5678", "CAR", "SPEEDING", 1),
    ("AP16EF9012", "HEAVY", "SIGNAL", 2),
    ("AP07GH3456", "BIKE", "SIGNAL", 0),
    ("AP39JK7890", "CAR", "SPEEDING", 3)
]

total_fine = 0
disq_count = 0

print("--- Traffic Challan Report ---")
for v in violations:
    v_no, v_type, offence, prev = v

    if offence == "HELMET":
        fine = 1000
    elif offence == "SIGNAL":
        fine = 1500
    else:
        fine = 2000

    if v_type == "HEAVY":
        fine = fine * 1.5

    if prev >= 1:
        fine = fine * 1.5

    if (prev + 1) >= 3:
        lic_status = "Disqualified"
        disq_count = disq_count + 1
    else:
        lic_status = "Active"

    total_fine = total_fine + fine
    print(v_no, "|", v_type, "|", offence, "| Fine:", fine, "| License:", lic_status)

print("Total Penalty Collected:", total_fine)
print("Licenses Disqualified:", disq_count)
