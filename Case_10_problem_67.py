# Case 10 - Problem 67: Retail Order Dispatch and Return Analysis

branch = input("Enter Branch Name: ")

# [Order ID, Item, Stock, Ordered, Dispatched, Returned]
orders = [
    ["ORD501", "Laptop Bag", 100, 40, 35, 5],
    ["ORD502", "USB Drive", 80, 50, 50, 2],
    ["ORD503", "Webcam", 60, 30, 35, 0],
    ["ORD504", "HDMI Cable", 120, 45, 40, 8],
    ["ORD505", "Power Bank", 50, 25, 20, 25]
]

bad_orders = []
total_pending = 0

print("--- Order Dispatch & Return Audit ---")
for rec in orders:
    oid = rec[0]
    item = rec[1]
    stock = rec[2]
    ordered = rec[3]
    disp = rec[4]
    ret = rec[5]

    if disp > ordered or disp > stock or ret > disp:
        print(oid, item, "-> Inconsistent Record")
        bad_orders.append(oid)
    else:
        pending = ordered - disp
        new_stock = stock - disp + ret
        total_pending = total_pending + pending
        print(oid, item, "-> Valid | Pending:", pending, "| Closing Stock:", new_stock)

print("Total Pending Units:", total_pending)
print("Inconsistent Order IDs:", bad_orders)
