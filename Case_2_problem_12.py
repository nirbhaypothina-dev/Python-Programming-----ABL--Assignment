# Case 2 - Problem 12: Attendance Recovery Computation

held = int(input("Enter Total Classes Held: "))
attended = int(input("Enter Classes Attended: "))

if held <= 0 or attended < 0 or attended > held:
    print("Invalid attendance inputs")
else:
    curr_per = (attended / held) * 100
    print("Current Attendance Percentage:", round(curr_per, 2))

    if curr_per >= 75:
        print("Status: Eligible for exam")
    else:
        print("Status: Not Eligible (Below 75%)")
        extra = 0
        t_held = held
        t_att = attended

        while (t_att / t_held) * 100 < 75:
            extra = extra + 1
            t_held = t_held + 1
            t_att = t_att + 1

        print("Minimum consecutive classes needed to reach 75%:", extra)

    print("Future Attendance Scenarios:")
    scenarios = [5, 10, 15]
    for s in scenarios:
        new_per = ((attended + s) / (held + s)) * 100
        print("After attending next", s, "classes:", round(new_per, 2), "%")
