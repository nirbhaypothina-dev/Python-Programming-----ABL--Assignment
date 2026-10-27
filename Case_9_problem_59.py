# Case 9 - Problem 59: Campus Transport Allocation

capacity = int(input("Enter Bus Seating Capacity: "))

# [Route Name, Student Demand, Available Buses]
routes = [
    ["Route-1 Benz Circle", 185, 4],
    ["Route-2 Gannavaram", 140, 2],
    ["Route-3 Eluru Road", 210, 4],
    ["Route-4 Ibrahimpatnam", 95, 2],
    ["Route-5 Gudivada", 160, 3]
]

total_buses = 0
total_unserved = 0

print("--- Campus Bus Allocation ---")
for r in routes:
    r_name = r[0]
    demand = r[1]
    avail = r[2]

    needed = demand // capacity
    if (demand % capacity) > 0:
        needed = needed + 1

    if needed <= avail:
        alloc = needed
        unserved = 0
    else:
        alloc = avail
        unserved = demand - (alloc * capacity)

    total_buses = total_buses + alloc
    total_unserved = total_unserved + unserved
    print(r_name, "-> Demand:", demand, "Needed:", needed, "Allocated:", alloc, "Unserved:", unserved)

print("Total Buses Allocated:", total_buses)
print("Total Unserved Students:", total_unserved)
