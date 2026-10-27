# Case 6 - Problem 14: Warehouse Inventory Reconciliation

target = int(input("Enter Minimum Stock Target: "))

# [Product ID, Name, Opening, Incoming, Dispatched, Closing]
inventory = [
    ["P101", "Keyboards", 120, 50, 60, 110],
    ["P102", "Monitors", 80, 40, 50, 65],
    ["P103", "Mouse", 150, 30, 40, 140],
    ["P104", "Cables", 90, 20, 35, 75],
    ["P105", "Headsets", 60, 25, 30, 58]
]

mismatch_cnt = 0
total_rep = 0

print("--- Inventory Reconciliation Report ---")
for item in inventory:
    pid = item[0]
    pname = item[1]
    open_s = item[2]
    inc_s = item[3]
    disp_s = item[4]
    close_s = item[5]

    expected = open_s + inc_s - disp_s
    diff = close_s - expected

    if diff == 0:
        status = "Matched"
    elif diff < 0:
        status = "Shortage"
        mismatch_cnt = mismatch_cnt + 1
    else:
        status = "Surplus"
        mismatch_cnt = mismatch_cnt + 1

    if close_s < target:
        rep = target - close_s
    else:
        rep = 0

    total_rep = total_rep + rep
    print(pid, pname, "-> Expected:", expected, "Actual:", close_s, "Status:", status, "Replenish:", rep)

print("Products with Discrepancy:", mismatch_cnt)
print("Total Units to Replenish:", total_rep)
