# Case 3 - Problem 13: ATM Transaction Sequence Simulation

balance = float(input("Enter Opening Balance: "))

transactions = [
    ("DEPOSIT", 5000),
    ("WITHDRAW", 3000),
    ("WITHDRAW", 25000),
    ("WITHDRAW", 12000),
    ("DEPOSIT", -500),
    ("DEPOSIT", 2500)
]

total_dep = 0
total_with = 0
valid_cnt = 0
reject_cnt = 0

print("--- Processing Transactions ---")
for txn in transactions:
    t_type, amt = txn

    if amt <= 0:
        print(t_type, amt, "-> Rejected (Invalid amount)")
        reject_cnt = reject_cnt + 1
    elif t_type == "DEPOSIT":
        balance = balance + amt
        total_dep = total_dep + amt
        valid_cnt = valid_cnt + 1
        print("DEPOSIT", amt, "-> Approved, Balance:", balance)
    elif t_type == "WITHDRAW":
        if amt > 20000:
            print("WITHDRAW", amt, "-> Rejected (Exceeds 20000 limit)")
            reject_cnt = reject_cnt + 1
        elif (balance - amt) < 1000:
            print("WITHDRAW", amt, "-> Rejected (Minimum balance 1000 required)")
            reject_cnt = reject_cnt + 1
        else:
            balance = balance - amt
            total_with = total_with + amt
            valid_cnt = valid_cnt + 1
            print("WITHDRAW", amt, "-> Approved, Balance:", balance)

print("--- Transaction Summary ---")
print("Total Deposited:", total_dep)
print("Total Withdrawn:", total_with)
print("Approved Transactions:", valid_cnt)
print("Rejected Transactions:", reject_cnt)
print("Closing Balance:", balance)
