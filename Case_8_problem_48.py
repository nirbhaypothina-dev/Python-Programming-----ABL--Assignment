# Case 8 - Problem 48: Tuple-Based Employee Shift Conflict Detection

dept = input("Enter Department Name: ")

# (Shift ID, Employee Name, Day, Start Hour, End Hour)
shifts = (
    ("SH101", "Arjun", "Monday", 9, 13),
    ("SH102", "Divya", "Monday", 10, 14),
    ("SH103", "Arjun", "Monday", 12, 16),
    ("SH104", "Kiran", "Tuesday", 8, 12),
    ("SH105", "Divya", "Monday", 13, 17),
    ("SH106", "Kiran", "Tuesday", 12, 16)
)

print("--- Checking Shift Conflicts for", dept, "---")
conflicts = 0
emp_list = []

n = len(shifts)
for i in range(n):
    id1, name1, day1, s1, e1 = shifts[i]
    for j in range(i + 1, n):
        id2, name2, day2, s2, e2 = shifts[j]

        if name1 == name2 and day1 == day2:
            if s1 < e2 and s2 < e1:
                conflicts = conflicts + 1
                print("Conflict:", name1, "on", day1, "between", id1, "and", id2)
                if name1 not in emp_list:
                    emp_list.append(name1)

print("Total Overlapping Shifts:", conflicts)
print("Employees with Conflicts:", emp_list)
